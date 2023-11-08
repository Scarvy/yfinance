# Single Ticker

The `Ticker` module, which allows you to access ticker data in a more Pythonic way:

```py title="Ticker Example"
import yfinance as yf

msft = yf.Ticker("MSFT")

yfinance.Ticker object <MSFT>
```

## Stock Information

```py title="Stock info Example"
msft.info

{
 'quoteType': 'EQUITY',
 'quoteSourceName': 'Nasdaq Real Time Price',
 'currency': 'USD',
 'shortName': 'Microsoft Corporation',
 'exchangeTimezoneName': 'America/New_York',
  ...
 'symbol': 'MSFT'
}
```

## Historical Data

Get historical market data for different periods.

**Periods:**

- 1, 5 Day
- 1, 3, 6 Month
- 1, 2, 5, 10 Year
- Year-to-Date
- Max

```py title="Historical Market Data Example"
hist = msft.history(period="max")

                                 Open        High         Low       Close      Volume  Dividends  Stock Splits
Date                                                                                                          
1986-03-13 00:00:00-05:00    0.055004    0.063093    0.055004    0.060396  1031788800        0.0           0.0
1986-03-14 00:00:00-05:00    0.060396    0.063632    0.060396    0.062553   308160000        0.0           0.0
1986-03-17 00:00:00-05:00    0.062553    0.064172    0.062553    0.063632   133171200        0.0           0.0
1986-03-18 00:00:00-05:00    0.063632    0.064172    0.061475    0.062014    67766400        0.0           0.0
1986-03-19 00:00:00-05:00    0.062014    0.062553    0.060396    0.060936    47894400        0.0           0.0
...                               ...         ...         ...         ...         ...        ...           ...
2023-10-31 00:00:00-04:00  338.850006  339.000000  334.690002  338.109985    20265300        0.0           0.0
2023-11-01 00:00:00-04:00  339.790009  347.420013  339.649994  346.070007    28158800        0.0           0.0
2023-11-02 00:00:00-04:00  347.239990  348.829987  344.769989  348.320007    24348100        0.0           0.0
2023-11-03 00:00:00-04:00  349.630005  354.390015  347.329987  352.799988    23624000        0.0           0.0
2023-11-06 00:00:00-05:00  353.450012  357.540009  353.350006  356.529999    23811600        0.0           0.0

[9490 rows x 7 columns]
```

```py title="Interval Example"
msft.history(period="1y", interval="1wk")

                                 Open        High         Low       Close     Volume  Dividends  Stock Splits
Date                                                                                                         
2022-11-07 00:00:00-05:00  219.865922  245.617144  219.162709  244.745560  170431600       0.00           0.0
2022-11-14 00:00:00-05:00  239.674563  244.636620  235.356280  238.911926  137343700       0.68           0.0
2022-11-21 00:00:00-05:00  239.793771  247.014505  239.078664  245.812714   74769700       0.00           0.0
2022-11-28 00:00:00-05:00  244.412273  254.384223  236.595614  253.291687  137898700       0.00           0.0
2022-12-05 00:00:00-05:00  250.302079  252.099825  240.568508  243.756744  109602000       0.00           0.0
...
2023-10-16 00:00:00-04:00  331.049988  336.880005  325.450012  326.670013  113714800       0.00           0.0
2023-10-23 00:00:00-04:00  325.470001  346.200012  324.390015  329.809998  178267100       0.00           0.0
2023-10-30 00:00:00-04:00  333.410004  354.390015  331.829987  352.799988  119224300       0.00           0.0
2023-11-06 00:00:00-05:00  353.450012  362.079987  353.350006  361.477509   31892344       0.00           0.0
```

Show history meta data, use

```py title="History Metadata Example"
msft.history_metadata

{
    'currency': 'USD',
    'symbol': 'MSFT',
    'exchangeName': 'NMS',
    'instrumentType': 'EQUITY',
    'firstTradeDate': 511108200,
    'regularMarketTime': 1699368185,
    'gmtoffset': -18000,
    'timezone': 'EST',
    'exchangeTimezoneName': 'America/New_York',
    'regularMarketPrice': 358.905,
    'chartPreviousClose': 0.097,
    'priceHint': 2,
    'currentTradingPeriod': {
        'pre': {'timezone': 'EST', 'start': 1699347600, 'end': 1699367400, 'gmtoffset': -18000},
        'regular': {'timezone': 'EST', 'start': 1699367400, 'end': 1699390800, 'gmtoffset': -18000},
        'post': {'timezone': 'EST', 'start': 1699390800, 'end': 1699405200, 'gmtoffset': -18000}
    },
    'dataGranularity': '1d',
    'range': '',
    'validRanges': ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
}
```

!!! note Note
    To show meta information about the history requires history() to be called first.

---

Available paramaters for the `history()` method are:

- **period:** data period to download (Either Use period parameter or use start and end) Valid periods are: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
- **interval:** data interval (intraday data cannot extend last 60 days) Valid intervals are: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
- **start:** If not using period - Download start date string (YYYY-MM-DD) or datetime.
- **end:** If not using period - Download end date string (YYYY-MM-DD) or datetime.
- **prepost:** Include Pre and Post market data in results? (Default is False)
- **auto_adjust:** Adjust all OHLC automatically? (Default is True)
- **actions:** Download stock dividends and stock splits events? (Default is True)

## Stock-Level Information

Show a variety of relevant stock-level information including:

**Examples:**

- Actions
- Dividends
- Stock Splits
- Capital Gains
- Share Count

```py title="Show Information Example"
msft.actions

                           Dividends  Stock Splits
Date                                              
1987-09-21 00:00:00-04:00       0.00           2.0
1990-04-16 00:00:00-04:00       0.00           2.0
1991-06-27 00:00:00-04:00       0.00           1.5
1992-06-15 00:00:00-04:00       0.00           1.5
1994-05-23 00:00:00-04:00       0.00           2.0
...                              ...           ...
2022-08-17 00:00:00-04:00       0.62           0.0
2022-11-16 00:00:00-05:00       0.68           0.0
2023-02-15 00:00:00-05:00       0.68           0.0
2023-05-17 00:00:00-04:00       0.68           0.0
2023-08-16 00:00:00-04:00       0.68           0.0

[88 rows x 2 columns]

msft.dividends

Date
2003-02-19 00:00:00-05:00    0.08
2003-10-15 00:00:00-04:00    0.16
2004-08-23 00:00:00-04:00    0.08
2004-11-15 00:00:00-05:00    3.08
2005-02-15 00:00:00-05:00    0.08
                             ... 
2022-08-17 00:00:00-04:00    0.62
2022-11-16 00:00:00-05:00    0.68
2023-02-15 00:00:00-05:00    0.68
2023-05-17 00:00:00-04:00    0.68
2023-08-16 00:00:00-04:00    0.68
Name: Dividends, Length: 79, dtype: float64

msft.splits

Date
1987-09-21 00:00:00-04:00    2.0
1990-04-16 00:00:00-04:00    2.0
1991-06-27 00:00:00-04:00    1.5
1992-06-15 00:00:00-04:00    1.5
1994-05-23 00:00:00-04:00    2.0
1996-12-09 00:00:00-05:00    2.0
1998-02-23 00:00:00-05:00    2.0
1999-03-29 00:00:00-05:00    2.0
2003-02-18 00:00:00-05:00    2.0
Name: Stock Splits, dtype: float64

msft.capital_gains  # only for mutual funds & etfs
Series([], Name: Capital Gains, dtype: float64)
```

```py title="Share Count Example"

msft.get_shares_full(start="2022-01-01", end=None)

2022-01-27 00:00:00-05:00    7496869888
2022-02-04 00:00:00-05:00    7800719872
2022-02-05 00:00:00-05:00    7496869888
2022-02-11 00:00:00-05:00    7496869888
2022-03-04 00:00:00-05:00    7605040128
                                ...    
2023-10-24 00:00:00-04:00    7429029888
2023-10-26 00:00:00-04:00    7432260096
2023-10-28 00:00:00-04:00    7432260096
2023-11-01 00:00:00-04:00    7432260096
2023-11-03 00:00:00-04:00    7432260096
Length: 84, dtype: int64
```

## Financials

In the `Ticker` module, you can access financials and other relevant information about a stock like news.

**Example:**

- Income Statement
- Balance Sheet
- Cash Flow Statement
- Holders
- News

### Income Statement

```py title="Income Statement Example"
msft.income_stmt

                                                        2023-06-30      2022-06-30      2021-06-30      2020-06-30
Tax Effect Of Unusual Items                                    0.0             0.0             0.0             0.0
Tax Rate For Calcs                                        0.189786        0.131134        0.138266            0.16
Normalized EBITDA                                   102384000000.0   97843000000.0   81602000000.0   65755000000.0
Total Unusual Items                                    -15000000.0     334000000.0    1303000000.0      28000000.0
Total Unusual Items Excluding Goodwill                 -15000000.0     334000000.0    1303000000.0      28000000.0
Net Income From Continuing Operation Net Minori...   72361000000.0   72738000000.0   61271000000.0   44281000000.0
Reconciled Depreciation                              13861000000.0   14460000000.0   11686000000.0   12796000000.0
Reconciled Cost Of Revenue                           65863000000.0   62650000000.0   52232000000.0   46078000000.0
EBITDA                                              102384000000.0   97843000000.0   81602000000.0   65755000000.0
EBIT                                                 88523000000.0   83383000000.0   69916000000.0   52959000000.0
Net Interest Income                                   1026000000.0      31000000.0    -215000000.0      89000000.0
Interest Expense                                      1968000000.0    2063000000.0    2346000000.0    2591000000.0
Interest Income                                       2994000000.0    2094000000.0    2131000000.0    2680000000.0
Normalized Income                                    72361000000.0   72738000000.0   61271000000.0   44281000000.0
Net Income From Continuing And Discontinued Ope...   72361000000.0   72738000000.0   61271000000.0   44281000000.0
Total Expenses                                      123392000000.0  114887000000.0   98172000000.0   90056000000.0
Total Operating Income As Reported                   88523000000.0   83383000000.0   69916000000.0   52959000000.0
Diluted Average Shares                                7472000000.0    7540000000.0    7608000000.0    7683000000.0
Basic Average Shares                                  7446000000.0    7496000000.0    7547000000.0    7610000000.0
Diluted EPS                                                   9.68            9.65            8.05            5.76
Basic EPS                                                     9.72             9.7            8.12            5.82
Diluted NI Availto Com Stockholders                  72361000000.0   72738000000.0   61271000000.0   44281000000.0
Net Income Common Stockholders                       72361000000.0   72738000000.0   61271000000.0   44281000000.0
Net Income                                           72361000000.0   72738000000.0   61271000000.0   44281000000.0
Net Income Including Noncontrolling Interests        72361000000.0   72738000000.0   61271000000.0   44281000000.0
Net Income Continuous Operations                     72361000000.0   72738000000.0   61271000000.0   44281000000.0
Tax Provision                                        16950000000.0   10978000000.0    9831000000.0    8755000000.0
Pretax Income                                        89311000000.0   83716000000.0   71102000000.0   53036000000.0
Other Income Expense                                   788000000.0     333000000.0    1186000000.0      77000000.0
Other Non Operating Income Expenses                    788000000.0     333000000.0    1186000000.0      77000000.0
Special Income Charges                                 -30000000.0    -101000000.0             NaN             NaN
Write Off                                               30000000.0     101000000.0             NaN             NaN
Gain On Sale Of Security                                15000000.0     435000000.0    1303000000.0      28000000.0
Net Non Operating Interest Income Expense             1026000000.0      31000000.0    -215000000.0      89000000.0
Interest Expense Non Operating                        1968000000.0    2063000000.0    2346000000.0    2591000000.0
Interest Income Non Operating                         2994000000.0    2094000000.0    2131000000.0    2680000000.0
Operating Income                                     88523000000.0   83383000000.0   69916000000.0   52959000000.0
Operating Expense                                    57529000000.0   52237000000.0   45940000000.0   43978000000.0
Research And Development                             27195000000.0   24512000000.0   20716000000.0   19269000000.0
Selling General And Administration                   30334000000.0   27725000000.0   25224000000.0   24709000000.0
Selling And Marketing Expense                        22759000000.0   21825000000.0   20117000000.0   19598000000.0
General And Administrative Expense                    7575000000.0    5900000000.0    5107000000.0    5111000000.0
Other Gand A                                          7575000000.0    5900000000.0    5107000000.0    5111000000.0
Gross Profit                                        146052000000.0  135620000000.0  115856000000.0   96937000000.0
Cost Of Revenue                                      65863000000.0   62650000000.0   52232000000.0   46078000000.0
Total Revenue                                       211915000000.0  198270000000.0  168088000000.0  143015000000.0
Operating Revenue                                   211915000000.0  198270000000.0  168088000000.0  143015000000.0
```

```py title="Quarterly Income Statement Example"
msft.quarterly_income_stmt

                                                            2023-09-30     2023-06-30     2023-03-31     2022-12-31     2022-09-30
Tax Effect Of Unusual Items                           -21045118.017886            0.0            0.0            0.0    -10640000.0
Tax Rate For Calcs                                            0.183001           0.19       0.192917       0.192438           0.19
Normalized EBITDA                                        31845000000.0  28128000000.0  25901000000.0  24047000000.0  24918000000.0
Total Unusual Items                                       -115000000.0    111000000.0    162000000.0   -232000000.0    -56000000.0
Total Unusual Items Excluding Goodwill                    -115000000.0    111000000.0    162000000.0   -232000000.0    -56000000.0
Net Income From Continuing Operation Net Minori...       22291000000.0  20081000000.0  18299000000.0  16425000000.0  17556000000.0
Reconciled Depreciation                                   3921000000.0   3874000000.0   3549000000.0   3648000000.0   2790000000.0
Reconciled Cost Of Revenue                               16302000000.0  16795000000.0  16128000000.0  17488000000.0  15452000000.0
EBITDA                                                   31730000000.0  28128000000.0  25901000000.0  24047000000.0  24862000000.0
EBIT                                                     27809000000.0  24254000000.0  22352000000.0  20399000000.0  22072000000.0
Net Interest Income                                        641000000.0    423000000.0    252000000.0    210000000.0    141000000.0
Interest Expense                                           525000000.0    482000000.0    496000000.0    490000000.0    500000000.0
Interest Income                                           1166000000.0    905000000.0    748000000.0    700000000.0    641000000.0
Normalized Income                                   22384954881.982113  20081000000.0  18299000000.0  16425000000.0  17601360000.0
Net Income From Continuing And Discontinued Ope...       22291000000.0  20081000000.0  18299000000.0  16425000000.0  17556000000.0
Total Expenses                                           29622000000.0  31935000000.0  30505000000.0  32348000000.0  28604000000.0
Total Operating Income As Reported                       26895000000.0  24254000000.0  22352000000.0  20399000000.0  21518000000.0
Diluted Average Shares                                    7462000000.0   7467000000.0   7464000000.0   7473000000.0   7485000000.0
Basic Average Shares                                      7429000000.0   7434000000.0   7441000000.0   7451000000.0   7457000000.0
Diluted EPS                                                       2.99           2.69           2.45            2.2           2.35
Basic EPS                                                          3.0            2.7           2.46            2.2           2.35
Diluted NI Availto Com Stockholders                      22291000000.0  20081000000.0  18299000000.0  16425000000.0  17556000000.0
Net Income Common Stockholders                           22291000000.0  20081000000.0  18299000000.0  16425000000.0  17556000000.0
Net Income                                               22291000000.0  20081000000.0  18299000000.0  16425000000.0  17556000000.0
Net Income Including Noncontrolling Interests            22291000000.0  20081000000.0  18299000000.0  16425000000.0  17556000000.0
Net Income Continuous Operations                         22291000000.0  20081000000.0  18299000000.0  16425000000.0  17556000000.0
Tax Provision                                             4993000000.0   4646000000.0   4374000000.0   3914000000.0   4016000000.0
Pretax Income                                            27284000000.0  24727000000.0  22673000000.0  20339000000.0  21572000000.0
Other Income Expense                                      -252000000.0    473000000.0    321000000.0    -60000000.0    -87000000.0
Other Non Operating Income Expenses                       -137000000.0    473000000.0    321000000.0    -60000000.0    -31000000.0
Gain On Sale Of Security                                  -115000000.0    141000000.0    162000000.0   -232000000.0    -56000000.0
Net Non Operating Interest Income Expense                  641000000.0    423000000.0    252000000.0    210000000.0    141000000.0
Interest Expense Non Operating                             525000000.0    482000000.0    496000000.0    490000000.0    500000000.0
Interest Income Non Operating                             1166000000.0    905000000.0    748000000.0    700000000.0    641000000.0
Operating Income                                         26895000000.0  24254000000.0  22352000000.0  20399000000.0  21518000000.0
Operating Expense                                        13320000000.0  15140000000.0  14377000000.0  14860000000.0  13152000000.0
Research And Development                                  6659000000.0   6739000000.0   6984000000.0   6844000000.0   6628000000.0
Selling General And Administration                        6661000000.0   8401000000.0   7393000000.0   8016000000.0   6524000000.0
Selling And Marketing Expense                             5187000000.0   6204000000.0   5750000000.0   5679000000.0   5126000000.0
General And Administrative Expense                        1474000000.0   2197000000.0   1643000000.0   2337000000.0   1398000000.0
Other Gand A                                              1474000000.0   2197000000.0   1643000000.0   2337000000.0   1398000000.0
Gross Profit                                             40215000000.0  39394000000.0  36729000000.0  35259000000.0  34670000000.0
Cost Of Revenue                                          16302000000.0  16795000000.0  16128000000.0  17488000000.0  15452000000.0
Total Revenue                                            56517000000.0  56189000000.0  52857000000.0  52747000000.0  50122000000.0
Operating Revenue                                        56517000000.0  56189000000.0  52857000000.0  52747000000.0  50122000000.0
```

### Balance Sheet

```py title="Balance Sheet Example"
msft.balance_sheet

                                                      2023-06-30      2022-06-30      2021-06-30      2020-06-30
Ordinary Shares Number                              7432000000.0    7464000000.0    7519000000.0    7571000000.0
Share Issued                                        7432000000.0    7464000000.0    7519000000.0    7571000000.0
Net Debt                                           12533000000.0   35850000000.0   43922000000.0   49751000000.0
Total Debt                                         59965000000.0   61270000000.0   67775000000.0   70998000000.0
Tangible Book Value                               128971000000.0   87720000000.0   84477000000.0   67915000000.0
...                                                          ...             ...             ...             ...
Cash Cash Equivalents And Short Term Investments  111262000000.0  104757000000.0  130334000000.0  136527000000.0
Other Short Term Investments                       76558000000.0   90826000000.0  116110000000.0  122951000000.0
Cash And Cash Equivalents                          34704000000.0   13931000000.0   14224000000.0   13576000000.0
Cash Equivalents                                   26226000000.0    5673000000.0    6952000000.0             NaN
Cash Financial                                      8478000000.0    8258000000.0    7272000000.0             NaN

[73 rows x 4 columns]
```

```py title="Quarterly Balance Sheet Example"
msft.quarterly_balance_sheet

                                                      2023-09-30      2023-06-30      2023-03-31      2022-12-31      2022-09-30
Ordinary Shares Number                              7431000000.0    7432000000.0    7437000000.0    7447000000.0    7457000000.0
Share Issued                                        7431000000.0    7432000000.0    7437000000.0    7447000000.0    7457000000.0
Net Debt                                                     NaN   12533000000.0   21648000000.0   32470000000.0   25738000000.0
Total Debt                                         84989000000.0   59965000000.0   60522000000.0   60114000000.0   60282000000.0
Tangible Book Value                               144029000000.0  128971000000.0  116864000000.0  104877000000.0   95299000000.0
...                                                          ...             ...             ...             ...             ...
Cash Cash Equivalents And Short Term Investments  143945000000.0  111262000000.0  104427000000.0   99508000000.0  107244000000.0
Other Short Term Investments                       63493000000.0   76558000000.0   77865000000.0   83862000000.0   84360000000.0
Cash And Cash Equivalents                          80452000000.0   34704000000.0   26562000000.0   15646000000.0   22884000000.0
Cash Equivalents                                   73074000000.0   26226000000.0   18053000000.0    8342000000.0   15647000000.0
Cash Financial                                      7378000000.0    8478000000.0    8509000000.0    7304000000.0    7237000000.0

[73 rows x 5 columns]
```

### Cash Flow

```py title="Cash Flow Statement Example"
msft.cashflow

                                                   2023-06-30     2022-06-30     2021-06-30     2020-06-30
Free Cash Flow                                  59475000000.0  65149000000.0  56118000000.0  45234000000.0
Repurchase Of Capital Stock                    -22245000000.0 -32696000000.0 -27385000000.0 -22968000000.0
Repayment Of Debt                               -2750000000.0  -9023000000.0  -3750000000.0  -5518000000.0
Issuance Of Debt                                          NaN            NaN            NaN            0.0
Issuance Of Capital Stock                        1866000000.0   1841000000.0   1693000000.0   1343000000.0
Capital Expenditure                            -28107000000.0 -23886000000.0 -20622000000.0 -15441000000.0
End Cash Position                               34704000000.0  13931000000.0  14224000000.0  13576000000.0
Beginning Cash Position                         13931000000.0  14224000000.0  13576000000.0  11356000000.0
Effect Of Exchange Rate Changes                  -194000000.0   -141000000.0    -29000000.0   -201000000.0
Changes In Cash                                 20967000000.0   -152000000.0    677000000.0   2421000000.0
Financing Cash Flow                            -43935000000.0 -58876000000.0 -48486000000.0 -46031000000.0
Cash Flow From Continuing Financing Activities -43935000000.0 -58876000000.0 -48486000000.0 -46031000000.0
Net Other Financing Charges                     -1006000000.0   -863000000.0  -2523000000.0  -3751000000.0
Cash Dividends Paid                            -19800000000.0 -18135000000.0 -16521000000.0 -15137000000.0
Common Stock Dividend Paid                     -19800000000.0 -18135000000.0 -16521000000.0 -15137000000.0
Net Common Stock Issuance                      -20379000000.0 -30855000000.0 -25692000000.0 -21625000000.0
Common Stock Payments                          -22245000000.0 -32696000000.0 -27385000000.0 -22968000000.0
Common Stock Issuance                            1866000000.0   1841000000.0   1693000000.0   1343000000.0
Net Issuance Payments Of Debt                   -2750000000.0  -9023000000.0  -3750000000.0  -5518000000.0
Net Short Term Debt Issuance                              NaN            NaN            NaN            0.0
Net Long Term Debt Issuance                     -2750000000.0  -9023000000.0  -3750000000.0  -5518000000.0
Long Term Debt Payments                         -2750000000.0  -9023000000.0  -3750000000.0  -5518000000.0
Long Term Debt Issuance                                   NaN            NaN            NaN            0.0
Investing Cash Flow                            -22680000000.0 -30311000000.0 -27577000000.0 -12223000000.0
Cash Flow From Continuing Investing Activities -22680000000.0 -30311000000.0 -27577000000.0 -12223000000.0
Net Other Investing Changes                     -3116000000.0  -2825000000.0   -922000000.0  -1241000000.0
Net Investment Purchase And Sale                10213000000.0  18438000000.0   2876000000.0   6980000000.0
Sale Of Investment                              47864000000.0  44894000000.0  65800000000.0  84170000000.0
Purchase Of Investment                         -37651000000.0 -26456000000.0 -62924000000.0 -77190000000.0
Net Business Purchase And Sale                  -1670000000.0 -22038000000.0  -8909000000.0  -2521000000.0
Purchase Of Business                            -1670000000.0 -22038000000.0  -8909000000.0  -2521000000.0
Net PPE Purchase And Sale                      -28107000000.0 -23886000000.0 -20622000000.0 -15441000000.0
Purchase Of PPE                                -28107000000.0 -23886000000.0 -20622000000.0 -15441000000.0
Operating Cash Flow                             87582000000.0  89035000000.0  76740000000.0  60675000000.0
Cash Flow From Continuing Operating Activities  87582000000.0  89035000000.0  76740000000.0  60675000000.0
Change In Working Capital                       -2388000000.0    446000000.0   -936000000.0   2148000000.0
Change In Other Working Capital                  5177000000.0   5805000000.0   2324000000.0   2212000000.0
Change In Other Current Liabilities              2825000000.0   3169000000.0   5551000000.0   2694000000.0
Change In Other Current Assets                  -4824000000.0  -3514000000.0  -4391000000.0  -3367000000.0
Change In Payables And Accrued Expense          -2721000000.0   2943000000.0   2798000000.0   3018000000.0
Change In Payable                               -2721000000.0   2943000000.0   2798000000.0   3018000000.0
Change In Account Payable                       -2721000000.0   2943000000.0   2798000000.0   3018000000.0
Change In Inventory                              1242000000.0  -1123000000.0   -737000000.0    168000000.0
Change In Receivables                           -4087000000.0  -6834000000.0  -6481000000.0  -2577000000.0
Changes In Account Receivables                  -4087000000.0  -6834000000.0  -6481000000.0  -2577000000.0
Stock Based Compensation                         9611000000.0   7502000000.0   6118000000.0   5289000000.0
Deferred Tax                                    -6059000000.0  -5702000000.0   -150000000.0  -3620000000.0
Deferred Income Tax                             -6059000000.0  -5702000000.0   -150000000.0  -3620000000.0
Depreciation Amortization Depletion             13861000000.0  14460000000.0  11686000000.0  12796000000.0
Depreciation And Amortization                   13861000000.0  14460000000.0  11686000000.0  12796000000.0
Depreciation                                    13861000000.0  14460000000.0  11686000000.0  12796000000.0
Operating Gains Losses                            196000000.0   -409000000.0  -1249000000.0   -219000000.0
Gain Loss On Investment Securities                        NaN            NaN            NaN   -219000000.0
Net Income From Continuing Operations           72361000000.0  72738000000.0  61271000000.0  44281000000.0
```

```py title="Quarterly Cash Flow Example"
msft.quarterly_cashflow

                                                   2023-09-30     2023-06-30     2023-03-31     2022-12-31     2022-09-30
Free Cash Flow                                  20666000000.0  19827000000.0  17834000000.0   4899000000.0  16915000000.0
Repurchase Of Capital Stock                     -4831000000.0  -5704000000.0  -5509000000.0  -5459000000.0  -5573000000.0
Repayment Of Debt                               -1500000000.0  -1000000000.0            0.0   -750000000.0  -1000000000.0
Issuance Of Debt                                25765000000.0            NaN            NaN            NaN            NaN
Issuance Of Capital Stock                         685000000.0    512000000.0    536000000.0    243000000.0    575000000.0
Capital Expenditure                             -9917000000.0  -8943000000.0  -6607000000.0  -6274000000.0  -6283000000.0
End Cash Position                               80452000000.0  34704000000.0  26562000000.0  15646000000.0  22884000000.0
Beginning Cash Position                         34704000000.0  26562000000.0  15646000000.0  22884000000.0  13931000000.0
Effect Of Exchange Rate Changes                   -99000000.0    -81000000.0     29000000.0     88000000.0   -230000000.0
Changes In Cash                                 45847000000.0   8223000000.0  10887000000.0  -7326000000.0   9183000000.0
Financing Cash Flow                             14761000000.0 -11413000000.0 -10290000000.0 -11349000000.0 -10883000000.0
Cash Flow From Continuing Financing Activities  14761000000.0 -11413000000.0 -10290000000.0 -11349000000.0 -10883000000.0
Net Other Financing Charges                      -307000000.0   -167000000.0   -258000000.0   -317000000.0   -264000000.0
Cash Dividends Paid                             -5051000000.0  -5054000000.0  -5059000000.0  -5066000000.0  -4621000000.0
Common Stock Dividend Paid                      -5051000000.0  -5054000000.0  -5059000000.0  -5066000000.0  -4621000000.0
Net Common Stock Issuance                       -4146000000.0  -5192000000.0  -4973000000.0  -5216000000.0  -4998000000.0
Common Stock Payments                           -4831000000.0  -5704000000.0  -5509000000.0  -5459000000.0  -5573000000.0
Common Stock Issuance                             685000000.0    512000000.0    536000000.0    243000000.0    575000000.0
Net Issuance Payments Of Debt                   24265000000.0  -1000000000.0            0.0   -750000000.0  -1000000000.0
Net Short Term Debt Issuance                    18692000000.0            NaN            NaN            NaN            NaN
Short Term Debt Issuance                        18692000000.0            NaN            NaN            NaN            NaN
Net Long Term Debt Issuance                      5573000000.0  -1000000000.0            0.0   -750000000.0  -1000000000.0
Long Term Debt Payments                         -1500000000.0  -1000000000.0            0.0   -750000000.0  -1000000000.0
Long Term Debt Issuance                          7073000000.0            NaN            NaN            NaN            NaN
Investing Cash Flow                               503000000.0  -9134000000.0  -3264000000.0  -7150000000.0  -3132000000.0
Cash Flow From Continuing Investing Activities    503000000.0  -9134000000.0  -3264000000.0  -7150000000.0  -3132000000.0
Net Other Investing Changes                      -982000000.0   -269000000.0  -1686000000.0   -301000000.0   -860000000.0
Net Investment Purchase And Sale                12588000000.0    419000000.0   5330000000.0    104000000.0   4360000000.0
Sale Of Investment                              21048000000.0  12395000000.0  14393000000.0  11703000000.0   9373000000.0
Purchase Of Investment                          -8460000000.0 -11976000000.0  -9063000000.0 -11599000000.0  -5013000000.0
Net Business Purchase And Sale                  -1186000000.0   -341000000.0   -301000000.0   -679000000.0   -349000000.0
Purchase Of Business                            -1186000000.0   -341000000.0   -301000000.0   -679000000.0   -349000000.0
Net PPE Purchase And Sale                       -9917000000.0  -8943000000.0  -6607000000.0  -6274000000.0  -6283000000.0
Purchase Of PPE                                 -9917000000.0  -8943000000.0  -6607000000.0  -6274000000.0  -6283000000.0
Operating Cash Flow                             30583000000.0  28770000000.0  24441000000.0  11173000000.0  23198000000.0
Cash Flow From Continuing Operating Activities  30583000000.0  28770000000.0  24441000000.0  11173000000.0  23198000000.0
Change In Working Capital                        2418000000.0   4243000000.0   1843000000.0 -10347000000.0   1873000000.0
Change In Other Working Capital                 -2701000000.0  14905000000.0   1233000000.0  -8049000000.0  -2912000000.0
Change In Other Current Liabilities             -3815000000.0   2864000000.0   1721000000.0   2076000000.0  -3836000000.0
Change In Other Current Assets                  -2809000000.0  -3967000000.0    598000000.0   -457000000.0   -998000000.0
Change In Payables And Accrued Expense           1214000000.0   1311000000.0   -407000000.0  -2058000000.0  -1567000000.0
Change In Payable                                1214000000.0   1311000000.0   -407000000.0  -2058000000.0  -1567000000.0
Change In Account Payable                        1214000000.0   1311000000.0   -407000000.0  -2058000000.0  -1567000000.0
Change In Inventory                              -505000000.0    374000000.0    106000000.0   1305000000.0   -543000000.0
Change In Receivables                           11034000000.0 -11244000000.0  -1408000000.0  -3164000000.0  11729000000.0
Changes In Account Receivables                  11034000000.0 -11244000000.0  -1408000000.0  -3164000000.0  11729000000.0
Stock Based Compensation                         2507000000.0   2416000000.0   2465000000.0   2538000000.0   2192000000.0
Deferred Tax                                     -568000000.0  -1888000000.0  -1675000000.0  -1305000000.0  -1191000000.0
Deferred Income Tax                              -568000000.0  -1888000000.0  -1675000000.0  -1305000000.0  -1191000000.0
Depreciation Amortization Depletion              3921000000.0   3874000000.0   3549000000.0   3648000000.0   2790000000.0
Depreciation And Amortization                    3921000000.0   3874000000.0   3549000000.0   3648000000.0   2790000000.0
Depreciation                                              NaN   3874000000.0   3549000000.0   3648000000.0   2790000000.0
Operating Gains Losses                             14000000.0     44000000.0    -40000000.0    214000000.0    -22000000.0
Net Income From Continuing Operations           22291000000.0  20081000000.0  18299000000.0  16425000000.0  17556000000.0
```

!!! note Note
    see `Ticker.get_income_stmt()` for more options

### Holders

```py title="Holders Example"

msft.major_holders

        0                                      1
0   0.05%        % of Shares Held by All Insider
1  73.21%       % of Shares Held by Institutions
2  73.25%        % of Float Held by Institutions
3    6255  Number of Institutions Holding Shares


msft.institutional_holders

                              Holder     Shares Date Reported   % Out         Value
0                 Vanguard Group Inc  653247546    2023-06-29  0.0879  234600794384
1                     Blackrock Inc.  536245027    2023-06-29  0.0722  192581679164
2           State Street Corporation  293614078    2023-06-29  0.0395  105445625265
3                           FMR, LLC  210111250    2023-06-29  0.0283   75457254238
4      Price (T.Rowe) Associates Inc  159904219    2023-06-29  0.0215   57426402950
5      Geode Capital Management, LLC  148129470    2023-06-29  0.0199   53197737284
6                     Morgan Stanley  123498322    2023-06-29  0.0166   44351952982
7          JP Morgan Chase & Company  113024837    2023-06-29  0.0152   40590610263
8  Norges Bank Investment Management   86316926    2022-12-30  0.0116   30998998055
9            Capital World Investors   85507261    2023-06-29  0.0115   30708223060

msft.mutualfund_holders

                                              Holder     Shares Date Reported   % Out        Value
0             Vanguard Total Stock Market Index Fund  231883087    2023-06-29  0.0312  83276174166
1                            Vanguard 500 Index Fund  177034936    2023-06-29  0.0238  63578557430
2                            Fidelity 500 Index Fund   85181943    2023-08-30  0.0115  30591391605
3                             SPDR S&P 500 ETF Trust   83514381    2023-09-29  0.0112  29992520056
4                           iShares Core S&P 500 ETF   70264910    2023-09-29  0.0095  25234237471
5                         Vanguard Growth Index Fund   63262454    2023-06-29  0.0085  22719445413
6        Invesco ETF Tr-Invesco QQQ Tr, Series 1 ETF   58757680    2023-08-30  0.0079  21101645905
7  Vanguard Institutional Index Fund-Institutiona...   50756950    2023-06-29  0.0068  18228343701
8                         Growth Fund Of America Inc   39310503    2023-09-29  0.0053  14117581134
9         Vanguard Information Technology Index Fund   39119308    2023-08-30  0.0053  14048917273
```

### Earnings

Show future and historic earnings dates, returns at most next 4 quarters and last 8 quarters by default.

```py title="Earnings Example"
msft.earnings_dates

                           EPS Estimate  Reported EPS  Surprise(%)
Earnings Date                                                     
2024-10-22 06:00:00-04:00           NaN           NaN          NaN
2024-07-23 06:00:00-04:00           NaN           NaN          NaN
2024-04-23 06:00:00-04:00           NaN           NaN          NaN
2024-01-22 16:00:00-05:00          2.78           NaN          NaN
2024-01-22 05:00:00-05:00          2.78           NaN          NaN
2023-10-24 12:00:00-04:00          2.65          2.99       0.1270
2023-07-25 12:00:00-04:00          2.55          2.69       0.0549
2023-04-25 12:00:00-04:00          2.23          2.45       0.0981
2023-01-24 11:00:00-05:00          2.29          2.32       0.0109
2022-10-25 12:00:00-04:00          2.30          2.35       0.0205
2022-07-26 12:00:00-04:00          2.29          2.23      -0.0274
2022-04-26 12:00:00-04:00          2.19          2.22       0.0160
```

> Note: If more are needed use msft.get_earnings_dates(limit=XX) with increased limit argument.

### News

```py title="News Example"
msft.news

[
    {
        'uuid': '7edcd98a-2762-3687-88ea-40f207a3bff8',
        'title': 'Dow Jones Falls Ahead Of Fed Speakers; Uber Stock Rallies On Earnings',
        'publisher': "Investor's Business Daily",
        'link': 'https://finance.yahoo.com/m/7edcd98a-2762-3687-88ea-40f207a3bff8/dow-jones-falls-ahead-of-fed.html',
        'providerPublishTime': 1699368891,
        'type': 'STORY',
        'thumbnail': {
            'resolutions': [
                {
                    'url': 'https://s.yimg.com/uu/api/res/1.2/HDjemjYlp7Z5vRwiz3dW9Q--~B/aD01NjM7dz0xMDAwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/ibd.com/8e3f0f90c622d76c522be98b9f3975ee',
                    'width': 1000,
                    'height': 563,
                    'tag': 'original'
                },
                {
                    'url': 'https://s.yimg.com/uu/api/res/1.2/udkt6p.2GFTMNRqe6zXG_A--~B/Zmk9ZmlsbDtoPTE0MDtweW9mZj0wO3c9MTQwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/ibd.com/8e3f0f90c622d76c522be98b9f3975ee',
                    'width': 140,
                    'height': 140,
                    'tag': '140x140'
                }
            ]
        },
        'relatedTickers': ['UBER', '^DJI', 'INTC', 'DKNG', 'UNH', 'NVDA', 'MELI', 'AMZN', 'COMP', 'MSFT']
    },
    ...
    {
        'uuid': '42bfa43d-8885-37f5-a402-d9a7d46ac168',
        'title': 'Should You Buy Microsoft Stock After Its Latest Earnings?',
        'publisher': 'Motley Fool',
        'link': 'https://finance.yahoo.com/m/42bfa43d-8885-37f5-a402-d9a7d46ac168/should-you-buy-microsoft.html',
        'providerPublishTime': 1699368780,
        'type': 'STORY',
        'thumbnail': {
            'resolutions': [
                {
                    'url': 'https://s.yimg.com/uu/api/res/1.2/3v_zdhwmq58vDJUbOcOe7A--~B/aD0yODgwO3c9NTEyMDthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/motleyfool.com/55357ed2e882a9e4b4e48a913fe86d6f',
                    'width': 5120,
                    'height': 2880,
                    'tag': 'original'
                },
                {
                    'url': 'https://s.yimg.com/uu/api/res/1.2/0nyv5bSXjY7WpJvSIsD8og--~B/Zmk9ZmlsbDtoPTE0MDtweW9mZj0wO3c9MTQwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/motleyfool.com/55357ed2e882a9e4b4e48a913fe86d6f',
                    'width': 140,
                    'height': 140,
                    'tag': '140x140'
                }
            ]
        },
        'relatedTickers': ['MSFT', 'AMZN', 'AAPL', 'GOOG']
    },
]
```

### Options

With the `options` method you can get option expirations and options chain for a specific expiration.



```py title="Options Expirations Example"
msft.options

(
    '2023-11-10',
    '2023-11-17',
    '2023-11-24',
    '2023-12-01',
    '2023-12-08',
    '2023-12-15',
    '2023-12-22',
    '2024-01-19',
    '2024-02-16',
    '2024-03-15',
    '2024-04-19',
    '2024-05-17',
    '2024-06-21',
    '2024-09-20',
    '2024-12-20',
    '2025-01-17',
    '2025-06-20',
    '2025-12-19',
    '2026-01-16'
)
```

Once choosing an expiration date, you can get options data using `opt.calls`, `opt.puts`, and `opt underlying`.

```py title="Option Chain For Specific Date Example"
opt = msft.option_chain('2023-11-10')


opt.calls

         contractSymbol             lastTradeDate  strike  lastPrice     bid     ask     change  percentChange  volume  openInterest  impliedVolatility  inTheMoney contractSize currency
0   MSFT231110C00170000 2023-11-07 15:01:37+00:00   170.0     189.60  189.55  189.80   2.500000       1.336184     1.0             9           2.976565        True      REGULAR      USD
1   MSFT231110C00180000 2023-11-06 18:15:35+00:00   180.0     174.90  179.50  179.70   0.000000       0.000000    15.0            17           2.621097        True      REGULAR      USD
2   MSFT231110C00190000 2023-11-07 14:42:39+00:00   190.0     168.70  169.50  169.65   2.649994       1.595901     1.0             3           2.375004        True      REGULAR      USD
3   MSFT231110C00200000 2023-10-25 13:53:57+00:00   200.0     143.05  159.35  160.20   0.000000       0.000000    11.0            12           2.501957        True      REGULAR      USD
4   MSFT231110C00220000 2023-11-07 14:36:52+00:00   220.0     138.60  138.55  141.15  14.000008      11.235961     3.0             1           2.199223        True      REGULAR      USD
..                  ...                       ...     ...        ...     ...     ...        ...            ...     ...           ...                ...         ...          ...      ...
63  MSFT231110C00425000 2023-11-02 13:36:49+00:00   425.0       0.01    0.00    0.01   0.000000       0.000000     5.0             7           0.515630       False      REGULAR      USD
64  MSFT231110C00430000 2023-10-23 17:08:13+00:00   430.0       0.01    0.00    0.01   0.000000       0.000000     NaN             1           0.546880       False      REGULAR      USD
65  MSFT231110C00435000 2023-11-03 13:30:09+00:00   435.0       0.01    0.00    0.01   0.000000       0.000000     1.0             2           0.578129       False      REGULAR      USD
66  MSFT231110C00465000 2023-10-17 17:09:47+00:00   465.0       0.01    0.00    0.01   0.000000       0.000000     NaN             1           0.750003       False      REGULAR      USD
67  MSFT231110C00490000 2023-10-24 18:51:19+00:00   490.0       0.01    0.00    0.01   0.000000       0.000000     NaN             1           0.906251       False      REGULAR      USD

[68 rows x 14 columns]


opt.puts

Options(
    puts=         contractSymbol             lastTradeDate  strike  lastPrice     bid     ask  change  percentChange  volume  openInterest  impliedVolatility  inTheMoney contractSize currency
0   MSFT231110P00180000 2023-10-20 14:52:56+00:00   180.0       0.01    0.00    0.01     0.0            0.0     1.0             1           1.937500       False      REGULAR      USD
1   MSFT231110P00190000 2023-10-03 17:08:44+00:00   190.0       0.04    0.00    0.31     0.0            0.0     NaN             5           2.480473       False      REGULAR      USD
2   MSFT231110P00200000 2023-10-30 15:26:45+00:00   200.0       0.01    0.00    0.01     0.0            0.0   117.0           131           1.687502       False      REGULAR      USD
3   MSFT231110P00205000 2023-10-30 18:18:50+00:00   205.0       0.01    0.00    0.01     0.0            0.0     NaN           200           1.625002       False      REGULAR      USD
4   MSFT231110P00210000 2023-11-03 17:53:54+00:00   210.0       0.01    0.00    0.01     0.0            0.0     1.0           513           1.531252       False      REGULAR      USD
..                  ...                       ...     ...        ...     ...     ...     ...            ...     ...           ...                ...         ...          ...      ...
62  MSFT231110P00445000 2023-10-25 13:42:06+00:00   445.0     101.05   84.75   86.40     0.0            0.0     1.0             0           0.781252        True      REGULAR      USD
63  MSFT231110P00450000 2023-10-25 13:42:06+00:00   450.0     106.05   89.70   91.90     0.0            0.0     NaN             0           1.017583        True      REGULAR      USD
64  MSFT231110P00455000 2023-10-04 16:25:33+00:00   455.0     137.15  100.95  102.60     0.0            0.0     NaN             0           2.081304        True      REGULAR      USD
65  MSFT231110P00460000 2023-10-19 14:20:40+00:00   460.0     125.78   99.90  101.80     0.0            0.0     2.0             0           1.127934        True      REGULAR      USD
66  MSFT231110P00470000 2023-10-25 13:39:07+00:00   470.0     125.35  109.50  112.05     0.0            0.0     NaN             0           1.165043        True      REGULAR      USD

[67 rows x 14 columns],

opt.underlying

underlying={
    'language': 'en-US',
    'region': 'US',
    'quoteType': 'EQUITY',
    'typeDisp': 'Equity',
    'quoteSourceName': 'Nasdaq Real Time Price',
    'triggerable': True,
    'customPriceAlertConfidence': 'HIGH',
    'currency': 'USD',
    'marketState': 'REGULAR',
    'regularMarketChangePercent': 0.8246157,
    'regularMarketPrice': 359.47,
    'exchange': 'NMS',
    'shortName': 'Microsoft Corporation',
    'longName': 'Microsoft Corporation',
    'messageBoardId': 'finmb_21835',
    'exchangeTimezoneName': 'America/New_York',
    'exchangeTimezoneShortName': 'EST',
    'gmtOffSetMilliseconds': -18000000,
    'market': 'us_market',
    'esgPopulated': False,
    'firstTradeDateMilliseconds': 511108200000,
    'priceHint': 2,
    'regularMarketChange': 2.9400024,
    'regularMarketTime': 1699370532,
    'regularMarketDayHigh': 359.94,
    'regularMarketDayRange': '357.63 - 359.94',
    'regularMarketDayLow': 357.63,
    'regularMarketVolume': 5037078,
    'regularMarketPreviousClose': 356.53,
    'bid': 359.37,
    'ask': 359.36,
    'bidSize': 11,
    'askSize': 22,
    'fullExchangeName': 'NasdaqGS',
    'financialCurrency': 'USD',
    'regularMarketOpen': 359.4,
    'averageDailyVolume3Month': 22362356,
    'averageDailyVolume10Day': 29692830,
    'fiftyTwoWeekLowChange': 140.12,
    'fiftyTwoWeekLowChangePercent': 0.6387964,
    'fiftyTwoWeekRange': '219.35 - 366.78',
    'fiftyTwoWeekHighChange': -7.3099976,
    'fiftyTwoWeekHighChangePercent': -0.019930197,
    'fiftyTwoWeekLow': 219.35,
    'fiftyTwoWeekHigh': 366.78,
    'fiftyTwoWeekChangePercent': 55.778385,
    'dividendDate': 1702512000,
    'earningsTimestamp': 1698183000,
    'earningsTimestampStart': 1705921140,
    'earningsTimestampEnd': 1706270400,
    'trailingAnnualDividendRate': 2.79,
    'trailingPE': 34.899998,
    'dividendRate': 3.0,
    'trailingAnnualDividendYield': 0.007825429,
    'dividendYield': 0.84,
    'epsTrailingTwelveMonths': 10.3,
    'epsForward': 11.92,
    'epsCurrentYear': 10.35,
    'priceEpsCurrentYear': 34.7314,
    'sharesOutstanding': 7432260096,
    'bookValue': 29.702,
    'fiftyDayAverage': 329.399,
    'fiftyDayAverageChange': 30.071014,
    'marketCap': 2671674654720,
    'fiftyDayAverageChangePercent': 0.09129055,
    'twoHundredDayAverage': 308.35446,
    'twoHundredDayAverageChange': 51.11554,
    'twoHundredDayAverageChangePercent': 0.16576877,
    'forwardPE': 30.15688,
    'priceToBook': 12.102552,
    'sourceInterval': 15,
    'exchangeDataDelayedBy': 0,
    'averageAnalystRating': '1.7 - Buy',
    'tradeable': False,
    'cryptoTradeable': False,
    'displayName': 'Microsoft',
    'symbol': 'MSFT'
}
```

### Identifiers

Supported identifiers are:

- **ISIN = International Securities Identification Number**

!!! danger "show ISIN code"
    The `isin` property is *experimental*. May not work all the time.

```py title="ISIN Example"
msft.isin

# TODO add output
```

### `Ticker` properties

!!! warning Warning
    Some properties have not been fully implemented which will raise a `YNotImplementedError`.
    Below is a list properties that will raise this error.

- `analyst_price_target`
- `calendar`
- `earnings`
- `quarterly_earnings`
- `recommendations`
- `recommendations_summary`
- `revenue_forecasts`
- `shares`
- `analyst_trend_details`

!!! info Info
    Updated as of 2023-11-07.
