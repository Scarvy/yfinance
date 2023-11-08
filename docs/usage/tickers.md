# Multiple Tickers

To initialize multiple `Ticker` objects, use `Tickers`

```py title="Multiple Ticker Example"
import yfinance as yf

# Pass a str of ticker symbols 
tickers = yf.Tickers(tickers='msft aapl goog')
# Or a list
symbols = ['msft', 'aapl', 'goog']
tickers = yf.Tickers(tickers=symbols)

tickers.tickers
{
    'MSFT': yfinance.Ticker object <MSFT>,
    'AAPL': yfinance.Ticker object <AAPL>,
    'GOOG': yfinance.Ticker object <GOOG>
}

tickers.symbols
['MSFT', 'AAPL', 'GOOG']
```

Once initialized, you can get data for each `Ticker` object:

```py title="Get Information Example"
tickers.tickers['MSFT'].info

{
 'quoteType': 'EQUITY',
 'quoteSourceName': 'Nasdaq Real Time Price',
 'currency': 'USD',
 'shortName': 'Microsoft Corporation',
 'exchangeTimezoneName': 'America/New_York',
  ...
 'symbol': 'MSFT'
}

tickers.tickers['AAPL'].history(period="1mo")

                                 Open        High         Low       Close    Volume  Dividends  Stock Splits
Date                                                                                                        
2023-10-09 00:00:00-04:00  176.809998  179.050003  175.800003  178.990005  42390800        0.0           0.0
2023-10-10 00:00:00-04:00  178.100006  179.720001  177.949997  178.389999  43698000        0.0           0.0
2023-10-11 00:00:00-04:00  178.199997  179.850006  177.600006  179.800003  47551100        0.0           0.0
2023-10-12 00:00:00-04:00  180.070007  182.339996  179.039993  180.710007  56743100        0.0           0.0
...
2023-11-02 00:00:00-04:00  175.520004  177.779999  175.460007  177.570007  77334800        0.0           0.0
2023-11-03 00:00:00-04:00  174.240005  176.820007  173.350006  176.649994  79763700        0.0           0.0
2023-11-06 00:00:00-05:00  176.380005  179.429993  176.210007  179.229996  63803700        0.0           0.0
2023-11-07 00:00:00-05:00  179.179993  181.639999  178.979996  181.324997  25948355        0.0           0.0

tickers.tickers['GOOG'].actions

                           Dividends  Stock Splits
Date                                              
2014-03-27 00:00:00-04:00        0.0      2.002000
2015-04-27 00:00:00-04:00        0.0      1.002746
2022-07-18 00:00:00-04:00        0.0     20.000000
```

!!! bug
    Sometimes Yahoo! API experiences 404 Client Error when trying to request data using `info`

!!! info "Managing Multi-Level Columns"
    - The following answer on Stack Overflow is for [How to deal with multi-level column names downloaded with yfinance](https://stackoverflow.com/questions/63107801)
      - `yfinance` returns a `pandas.DataFrame` with multi-level column names, with a level for the ticker and a level for the stock price data
      - The answer discusses:
        - How to correctly read the the multi-level columns after saving the dataframe to a csv with `pandas.DataFrame.to_csv`
        - How to download single or multiple tickers into a single dataframe with single level column names and a ticker column