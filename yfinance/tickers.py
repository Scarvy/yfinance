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
from typing import Any, Dict, List, Union

from pandas import DataFrame

from . import Ticker, multi


# from collections import namedtuple as _namedtuple


class Tickers:
    """A class to retrieve stock-level information for multiple ticker symbols from Yahoo! Finance APIs.

    For a list of ticker symbols (ex. "goog aapl msft") download price history and/ or news articles.
    """

    def __repr__(self):
        return f"yfinance.Tickers object <{','.join(self.symbols)}>"

    def __init__(self, tickers: Union[str, List], session=None):
        tickers = (
            tickers if isinstance(tickers, list) else tickers.replace(",", " ").split()
        )
        self.symbols = [ticker.upper() for ticker in tickers]
        self.tickers = {
            ticker: Ticker(ticker, session=session) for ticker in self.symbols
        }
        """
        Initializes a `Tickers` object for a specific list of ticker symbols.

        Attributes:
            symbols: A list of ticker symbols.
            tickers: A dictionary of `Ticker` objects.
            session: A client session object. Defaults is None.
        """

        # self.tickers = _namedtuple(
        #     "Tickers", ticker_objects.keys(), rename=True
        # )(*ticker_objects.values())

    def history(
        self,
        period: str = "1mo",
        interval: str = "1d",
        start: str = None,
        end: str = None,
        prepost: bool = False,
        actions: bool = True,
        auto_adjust: bool = True,
        repair: bool = False,
        proxy: str = None,
        threads: Union[bool, int] = True,
        group_by: str = "column",
        progress: bool = True,
        timeout: Union[None, float] = 10,
        **kwargs,
    ) -> DataFrame:
        """Download stock price history for the set of `tickers`.

        Parameters:
            period:
                Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                Either Use period parameter or use start and end
            interval:
                Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                Intraday data cannot extend last 60 days
            start:
                Download start date string (YYYY-MM-DD) or _datetime, inclusive.
                Default is 99 years ago
                E.g. for start="2020-01-01", the first data point will be on "2020-01-01"
            end:
                Download end date string (YYYY-MM-DD) or _datetime, exclusive.
                Default is now
                E.g. for end="2023-01-01", the last data point will be on "2022-12-31"
            prepost:
                Include Pre and Post market data in results?
                Default is False
            actions:
                Download dividend + stock splits data. Default is False
            auto_adjust:
                Adjust all OHLC automatically? Default is False
            repair:
                Detect currency unit 100x mixups and attempt repair
                Default is False
            proxy:
                Optional. Proxy server URL scheme. Default is None
            threads:
                How many threads to use for mass downloading. Default is True
            group_by:
                Group by 'ticker' or 'column'. Defaults to "column".
            progress (bool, optional): Show progress bar when downloading data. Defaults to True.
            timeout:
                If not None stops waiting for a response after given number of
                seconds. (Can also be a fraction of a second e.g. 0.01)
                Defaults to 10.

        Returns:
            dataframe: Stock price history for set of `tickers`
        """

        return self.download(
            period,
            interval,
            start,
            end,
            prepost,
            actions,
            auto_adjust,
            repair,
            proxy,
            threads,
            group_by,
            progress,
            timeout,
            **kwargs,
        )

    def download(
        self,
        period: str = "1mo",
        interval: str = "1d",
        start: str = None,
        end: str = None,
        prepost: bool = False,
        actions: bool = True,
        auto_adjust: bool = True,
        repair: bool = False,
        proxy: str = None,
        threads: Union[bool, float] = True,
        group_by: str = "column",
        progress: bool = True,
        timeout: Union[None, float] = 10,
        **kwargs,
    ) -> DataFrame:
        """Download stock price data.

        Parameters:
            period:
                Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                Either Use period parameter or use start and end
                Defaults to "1mo".
            interval:
                Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                Intraday data cannot extend last 60 days
                Defaults to "1d".
            start:
                Download start date string (YYYY-MM-DD) or _datetime, inclusive.
                Default is 99 years ago
                E.g. for start="2020-01-01", the first data point will be on "2020-01-01"
            end:
                Download end date string (YYYY-MM-DD) or _datetime, exclusive.
                Default is now
                E.g. for end="2023-01-01", the last data point will be on "2022-12-31"
            prepost:
                Include Pre and Post market data in results?
                Default is False.
            actions:
                Download dividend + stock splits data. Default is False
            auto_adjust:
                Adjust all OHLC automatically? Default is False
            repair:
                Detect currency unit 100x mixups and attempt repair
                Default is False
            proxy:
                Optional. Proxy server URL scheme. Default is None
            threads:
                How many threads to use for mass downloading. Default is True
            group_by (str, optional): Group by 'ticker' or 'column'. Defaults to "column".
            progress (bool, optional): Show progress bar when downloading data. Defaults to True.
            timeout:
                If not None stops waiting for a response after given number of
                seconds. (Can also be a fraction of a second e.g. 0.01)
                Defauls to 10.

        Returns:
            data: Stock price history for set of `tickers`
        """
        data = multi.download(
            self.symbols,
            start=start,
            end=end,
            actions=actions,
            auto_adjust=auto_adjust,
            repair=repair,
            period=period,
            interval=interval,
            prepost=prepost,
            proxy=proxy,
            group_by="ticker",
            threads=threads,
            progress=progress,
            timeout=timeout,
            **kwargs,
        )

        for symbol in self.symbols:
            self.tickers.get(symbol, {})._history = data[symbol]

        if group_by == "column":
            data.columns = data.columns.swaplevel(0, 1)
            data.sort_index(level=0, axis=1, inplace=True)

        return data

    def news(self) -> Dict[str, List[Dict[str, Any]]]:
        """Get news for a set of `tickers`

        Returns:
            news: List of articles for a set of `tickers`
        """
        return {
            ticker: [item for item in Ticker(ticker).news] for ticker in self.symbols
        }
