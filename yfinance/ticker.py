#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# yfinance - market data downloader
# https://github.com/ranaroussi/yfinance
#
# Copyright 2017-2019 Ran Aroussi
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from __future__ import print_function

import datetime as _datetime
from collections import namedtuple as _namedtuple
from typing import Any, Dict, List, Optional

import pandas as _pd
import requests

from .base import TickerBase


class Ticker(TickerBase):
    """
    A class representing a single stock ticker, providing access to various data
    through Yahoo! Finance APIs.

    Attributes:
        ticker (str): The stock ticker symbol.
        session (optional): An optional session object to use for requests.
    """

    def __init__(self, ticker: str, session: Optional[requests.Session] = None) -> None:
        """
        Initialize the Ticker object with a specific ticker symbol and an optional session.

        Args:
            ticker: The ticker symbol to retrieve data for.
            session: An optional session object to use for making HTTP requests.
                     If not provided, the default `requests` library session is used.
        """
        super(Ticker, self).__init__(ticker, session=session)
        self._expirations = {}
        self._underlying = {}

    def __repr__(self):
        return f"yfinance.Ticker object <{self.ticker}>"

    def _download_options(self, date=None, proxy=None):
        if date is None:
            url = f"{self._base_url}/v7/finance/options/{self.ticker}"
        else:
            url = f"{self._base_url}/v7/finance/options/{self.ticker}?date={date}"

        r = self._data.get(url=url, proxy=proxy).json()
        if len(r.get("optionChain", {}).get("result", [])) > 0:
            for exp in r["optionChain"]["result"][0]["expirationDates"]:
                self._expirations[
                    _datetime.datetime.utcfromtimestamp(exp).strftime("%Y-%m-%d")
                ] = exp

            self._underlying = r["optionChain"]["result"][0].get("quote", {})

            opt = r["optionChain"]["result"][0].get("options", [])

            return dict(**opt[0], underlying=self._underlying) if len(opt) > 0 else {}
        return {}

    def _options2df(self, opt, tz=None):
        data = _pd.DataFrame(opt).reindex(
            columns=[
                "contractSymbol",
                "lastTradeDate",
                "strike",
                "lastPrice",
                "bid",
                "ask",
                "change",
                "percentChange",
                "volume",
                "openInterest",
                "impliedVolatility",
                "inTheMoney",
                "contractSize",
                "currency",
            ]
        )

        data["lastTradeDate"] = _pd.to_datetime(
            data["lastTradeDate"], unit="s", utc=True
        )
        if tz is not None:
            data["lastTradeDate"] = data["lastTradeDate"].dt.tz_convert(tz)
        return data

    def option_chain(
        self,
        date: Optional[str] = None,
        proxy: Optional[str] = None,
        tz: Optional[str] = None,
    ) -> _namedtuple:
        """
        Retrieve the options chain for the ticker.

        Args:
            date (Optional[str]): Specific expiration date to retrieve the options chain for.
            proxy (Optional[str]): Proxy configuration for the request.
            tz (Optional[str]): Timezone for the last trade dates in the options data.

        Returns:
            namedtuple: A named tuple containing the calls, puts, and underlying data as DataFrames.

        Raises:
            ValueError: If the specified date is not available in the expirations.
        """
        if date is None:
            options = self._download_options(proxy=proxy)
        else:
            if not self._expirations:
                self._download_options()
            if date not in self._expirations:
                raise ValueError(
                    f"Expiration `{date}` cannot be found. "
                    f"Available expirations are: [{', '.join(self._expirations)}]"
                )
            date = self._expirations[date]
            options = self._download_options(date, proxy=proxy)

        return _namedtuple("Options", ["calls", "puts", "underlying"])(
            **{
                "calls": self._options2df(options["calls"], tz=tz),
                "puts": self._options2df(options["puts"], tz=tz),
                "underlying": options["underlying"],
            }
        )

    # ------------------------

    @property
    def isin(self) -> str:
        """
        Get the International Securities Identification Number (ISIN) of the security.

        Returns:
            str: The ISIN code.
        """
        return self.get_isin()

    @property
    def major_holders(self) -> _pd.DataFrame:
        """
        Retrieve a DataFrame containing major holders of a specific ticker.

        Returns:
            _pd.DataFrame: Major holders data with percentage of holdings.
        """
        return self.get_major_holders()

    @property
    def institutional_holders(self) -> _pd.DataFrame:
        """
        Retrieve a DataFrame containing institutional holders of a specific ticker.

        Returns:
            _pd.DataFrame: Institutional holders data with share details and ownership.
        """
        return self.get_institutional_holders()

    @property
    def mutualfund_holders(self) -> _pd.DataFrame:
        """
        Retrieve a DataFrame containing mutual fund holders of a specific ticker.

        Returns:
            _pd.DataFrame: Mutual fund holders data with share details and ownership.
        """
        return self.get_mutualfund_holders()

    @property
    def dividends(self) -> _pd.Series:
        """
        Retrieve a Series containing historical dividend payments of a specific ticker.

        Returns:
            _pd.Series: Historical dividends data.
        """
        return self.get_dividends()

    @property
    def capital_gains(self):
        """
        Retrieve a Series containing historical capital gains distributions of a specific ticker.

        Returns:
            _pd.Series: Historical capital gains data.
        """
        return self.get_capital_gains()

    @property
    def splits(self) -> _pd.Series:
        """
        Retrieve a Series containing historical stock splits of a specific ticker.

        Returns:
            _pd.Series: Historical stock splits data.
        """
        return self.get_splits()

    @property
    def actions(self) -> _pd.DataFrame:
        """
        Retrieve a DataFrame containing corporate actions like dividends and stock splits.

        Returns:
            _pd.DataFrame: Corporate actions data.
        """
        return self.get_actions()

    @property
    def shares(self) -> _pd.DataFrame:
        """
        Retrieve a DataFrame containing share-related data for a specific ticker.

        Returns:
            _pd.DataFrame: Shares data including outstanding shares and float.
        """
        return self.get_shares()

    @property
    def info(self) -> dict:
        """
        Retrieve general information about a specific ticker as a dictionary.

        Returns:
            dict: General information including company description, sector, and more.
        """
        return self.get_info()

    @property
    def fast_info(self):
        """
        Retrieve a subset of general information about a specific ticker, optimized for speed.

        Returns:
            dict: A subset of general information data.
        """
        return self.get_fast_info()

    @property
    def calendar(self) -> _pd.DataFrame:
        """
        Retrieve a DataFrame containing scheduled events like earnings dates and dividend dates.

        Returns:
            _pd.DataFrame: Calendar events data.
        """
        return self.get_calendar()

    @property
    def recommendations(self) -> _pd.DataFrame:
        """
        Retrieve a DataFrame containing analyst recommendations for a specific ticker.

        Returns:
            _pd.DataFrame: Analyst recommendations with ratings and price targets.
        """
        return self.get_recommendations()

    @property
    def earnings(self) -> _pd.DataFrame:
        """
        Retrieve a DataFrame containing historical earnings data for a specific ticker.

        Returns:
            _pd.DataFrame: Historical earnings data with EPS and revenue figures.
        """
        return self.get_earnings()

    @property
    def quarterly_earnings(self) -> _pd.DataFrame:
        """
        Retrieve a DataFrame containing quarterly earnings data for a specific ticker.

        Returns:
            _pd.DataFrame: Quarterly earnings data with EPS and revenue figures.
        """
        return self.get_earnings(freq="quarterly")

    @property
    def income_stmt(self) -> _pd.DataFrame:
        """
        Retrieve a DataFrame containing the annual income statement for a specific ticker.

        Returns:
            _pd.DataFrame: The annual income statement with detailed financial information.
        """
        return self.get_income_stmt(pretty=True)

    @property
    def quarterly_income_stmt(self) -> _pd.DataFrame:
        """
        Retrieve a DataFrame containing the quarterly income statement for a specific ticker.

        Returns:
            _pd.DataFrame: The quarterly income statement with detailed financial information.
        """
        return self.get_income_stmt(pretty=True, freq="quarterly")

    @property
    def incomestmt(self) -> _pd.DataFrame:
        """
        Alias to income_stmt. Retrieve the annual income statement for a specific ticker.

        Returns:
            _pd.DataFrame: The annual income statement with detailed financial information.
        """
        return self.income_stmt

    @property
    def quarterly_incomestmt(self) -> _pd.DataFrame:
        """
        Alias to quarterly_income_stmt. Retrieve the quarterly income statement for a specific ticker.

        Returns:
            _pd.DataFrame: The quarterly income statement with detailed financial information.
        """
        return self.quarterly_income_stmt

    @property
    def financials(self) -> _pd.DataFrame:
        """
        Alias to income_stmt. Retrieve the annual financials for a specific ticker.

        Returns:
            _pd.DataFrame: The annual financials with detailed financial information.
        """
        return self.income_stmt

    @property
    def quarterly_financials(self) -> _pd.DataFrame:
        """
        Alias to quarterly_income_stmt. Retrieve the quarterly financials for a specific ticker.

        Returns:
            _pd.DataFrame: The quarterly financials with detailed financial information.
        """
        return self.quarterly_income_stmt

    @property
    def balance_sheet(self) -> _pd.DataFrame:
        """
        Retrieve a DataFrame containing the annual balance sheet for a specific ticker.

        Returns:
            _pd.DataFrame: The annual balance sheet with assets, liabilities, and equity.
        """
        return self.get_balance_sheet(pretty=True)

    @property
    def quarterly_balance_sheet(self) -> _pd.DataFrame:
        """
        Retrieve a DataFrame containing the quarterly balance sheet for a specific ticker.

        Returns:
            _pd.DataFrame: The quarterly balance sheet with assets, liabilities, and equity figures.
        """
        return self.get_balance_sheet(pretty=True, freq="quarterly")

    @property
    def balancesheet(self) -> _pd.DataFrame:
        """
        Alias to balance_sheet. Retrieve the annual balance sheet for a specific ticker.

        Returns:
            _pd.DataFrame: The annual balance sheet with assets, liabilities, and equity.
        """
        return self.balance_sheet

    @property
    def quarterly_balancesheet(self) -> _pd.DataFrame:
        """
        Alias to quarterly_balance_sheet. Retrieve the quarterly balance sheet for a specific ticker.

        Returns:
            _pd.DataFrame: The quarterly balance sheet with detailed financial information.
        """
        return self.quarterly_balance_sheet

    @property
    def cash_flow(self) -> _pd.DataFrame:
        return self.get_cash_flow(pretty=True, freq="yearly")

    @property
    def quarterly_cash_flow(self) -> _pd.DataFrame:
        return self.get_cash_flow(pretty=True, freq="quarterly")

    @property
    def cashflow(self) -> _pd.DataFrame:
        """
        Retrieve a DataFrame containing the annual cash flow statement for a specific ticker.

        Returns:
            _pd.DataFrame: The annual cash flow statement with cash flow activities details.
        """
        return self.cash_flow

    @property
    def quarterly_cashflow(self) -> _pd.DataFrame:
        """
        Retrieve a DataFrame containing the quarterly cash flow statement for a specific ticker.

        Returns:
            _pd.DataFrame: The quarterly cash flow statement with cash flow activities details.
        """
        return self.quarterly_cash_flow

    @property
    def recommendations_summary(self):
        """
        Retrieve a summary of analyst recommendations for a specific ticker.

        Returns:
            A data structure containing a summary of recommendations, such as buy, hold, sell ratings.
        """
        return self.get_recommendations_summary()

    @property
    def analyst_price_target(self) -> _pd.DataFrame:
        """
        Retrieve a DataFrame containing analysts' price targets for a specific ticker.

        Returns:
            _pd.DataFrame: Analysts' price targets with details such as mean, high, and low targets.
        """
        return self.get_analyst_price_target()

    @property
    def revenue_forecasts(self) -> _pd.DataFrame:
        """
        Retrieve a DataFrame containing revenue forecasts for a specific ticker.

        Returns:
            _pd.DataFrame: Revenue forecasts with estimates and historical data.
        """
        return self.get_rev_forecast()

    @property
    def sustainability(self) -> _pd.DataFrame:
        """
        Retrieve a DataFrame containing sustainability metrics for a specific ticker.

        Returns:
            _pd.DataFrame: Sustainability data including environmental, social, and governance scores.
        """
        return self.get_sustainability()

    @property
    def options(self) -> tuple:
        """
        Retrieve a tuple of option expiration dates available for a specific ticker.

        Returns:
            tuple: A tuple containing option expiration dates.
        """
        if not self._expirations:
            self._download_options()
        return tuple(self._expirations.keys())

    @property
    def news(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Retrieve news articles related to a specific ticker.

        Returns:
            A data structure containing news articles, each with a headline, source, and publication date.
        """
        return self.get_news()

    @property
    def trend_details(self) -> _pd.DataFrame:
        """
        Retrieve a DataFrame containing trend details for a specific ticker.

        Returns:
            _pd.DataFrame: Data on trend metrics, possibly including sentiment and momentum indicators.
        """
        return self.get_trend_details()

    @property
    def earnings_trend(self) -> _pd.DataFrame:
        """
        Retrieve a DataFrame containing the earnings trend for a specific ticker.

        Returns:
            _pd.DataFrame: Earnings trend data with estimates and revisions.
        """
        return self.get_earnings_trend()

    @property
    def earnings_dates(self) -> _pd.DataFrame:
        """
        Retrieve a DataFrame containing historical and projected earnings dates for a specific ticker.

        Returns:
            _pd.DataFrame: Earnings dates with past earnings dates and future estimates.
        """
        return self.get_earnings_dates()

    @property
    def earnings_forecasts(self) -> _pd.DataFrame:
        """
        Retrieve a DataFrame containing earnings forecasts for a specific ticker.

        Returns:
            _pd.DataFrame: Earnings forecasts with analyst estimates and projections.
        """
        return self.get_earnings_forecast()

    @property
    def history_metadata(self) -> dict:
        """
        Retrieve metadata about the historical data for a specific ticker.

        Returns:
            dict: Metadata providing details about the historical data, such as date ranges and data availability.
        """
        return self.get_history_metadata()
