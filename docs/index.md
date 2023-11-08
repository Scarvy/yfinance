# Welcome to yfinance

[![Python version](https://img.shields.io/badge/python-2.7,%203.6+-blue.svg?style=flat)](https://pypi.python.org/pypi/yfinance)
[![PyPi version](https://img.shields.io/pypi/v/yfinance.svg?maxAge=60%)](https://pypi.python.org/pypi/yfinance)
[![PyPi status](https://img.shields.io/pypi/status/yfinance.svg?maxAge=60)](https://pypi.python.org/pypi/yfinance)
[![PyPi downloads](https://img.shields.io/pypi/dm/yfinance.svg?maxAge=2592000&label=installs&color=%2327B1FF)](https://pypi.python.org/pypi/yfinance)
[![Travis-CI build status](https://img.shields.io/travis/ranaroussi/yfinance/main.svg?maxAge=1)](https://travis-ci.com/github/ranaroussi/yfinance)
[![CodeFactor](https://www.codefactor.io/repository/github/ranaroussi/yfinance/badge)](https://www.codefactor.io/repository/github/ranaroussi/yfinance)
[![Star this repo](https://img.shields.io/github/stars/ranaroussi/yfinance.svg?style=social&label=Star&maxAge=60)](https://github.com/ranaroussi/yfinance)
[![Follow me on twitter](https://img.shields.io/twitter/follow/aroussi.svg?style=social&label=Follow&maxAge=60)](https://twitter.com/aroussi)

**yfinance** is a threaded and Pythonic way to download market data from [Yahoo!Ⓡ finance](https://finance.yahoo.com).

!!! warning WARNING
     **yfinance** is not affiliated, endorsed, or vetted by Yahoo, Inc. It's an open-source tool that uses Yahoo's publicly available APIs, and is intended for research and educational purposes. You should refer to Yahoo!'s terms of use (here, here, and here) for detailes on your rights to use the actual data downloaded.

---

Access ticker data in a more Pythonic way:

```py title="Single Ticker Example"
import yfinance as yf

msft = yf.Ticker("MSFT")

# get all stock info
msft.info

# get historical market data
hist = msft.history(period="1mo")

                                 Open        High         Low       Close    Volume  Dividends  Stock Splits
Date                                                                                                        
2023-10-09 00:00:00-04:00  324.750000  330.299988  323.179993  329.820007  19891200        0.0           0.0
2023-10-10 00:00:00-04:00  330.959991  331.100006  327.670013  328.390015  20557100        0.0           0.0
2023-10-11 00:00:00-04:00  331.209991  332.820007  329.140015  332.420013  20063200        0.0           0.0
```

Access multiple tickers, use

```py title="Multiple Tickers Example"
import yfinance as yf

tickers = yf.Tickers('msft aapl goog')

# access each ticker using (example)
tickers.tickers['MSFT'].info
tickers.tickers['AAPL'].history(period="1mo")
tickers.tickers['GOOG'].actions

                           Dividends  Stock Splits
Date                                              
1987-05-11 00:00:00-04:00   0.000536           0.0
1987-06-16 00:00:00-04:00   0.000000           2.0
1987-08-10 00:00:00-04:00   0.000536           0.0
1987-11-17 00:00:00-05:00   0.000714           0.0
1988-02-12 00:00:00-05:00   0.000714           0.0
...                              ...           ...
2022-08-05 00:00:00-04:00   0.230000           0.0
2022-11-04 00:00:00-04:00   0.230000           0.0
2023-02-10 00:00:00-05:00   0.230000           0.0
2023-05-12 00:00:00-04:00   0.240000           0.0
2023-08-11 00:00:00-04:00   0.240000           0.0
```

Download price history into a `pandas` DataFrame:

```py title="Download History Example"
import yfinance as yf
data = yf.download("SPY AAPL", period="1mo")

[*********************100%%**********************]  2 of 2 completed

             Adj Close                   Close                    High                     Low                    Open                Volume           
                  AAPL         SPY        AAPL         SPY        AAPL         SPY        AAPL         SPY        AAPL         SPY      AAPL        SPY
Date                                                                                                                                                   
2023-10-09  178.990005  432.290009  178.990005  432.290009  179.050003  432.880005  175.800003  427.010010  176.809998  427.579987  42390800   80374400
2023-10-10  178.389999  434.540009  178.389999  434.540009  179.720001  437.220001  177.949997  432.529999  178.100006  432.940002  43698000   78607300
2023-10-11  179.800003  436.320007  179.800003  436.320007  179.850006  436.579987  177.600006  433.179993  178.199997  435.640015  47551100   62451700
2023-10-12  180.710007  433.660004  180.710007  433.660004  182.339996  437.339996  179.039993  431.230011  180.070007  436.950012  56743100   81154200
2023-10-13  178.850006  431.500000  178.850006  431.500000  181.929993  436.450012  178.139999  429.880005  181.419998  435.209991  51427100   95143100
2023-10-16  178.720001  436.040009  178.720001  436.040009  179.080002  437.140015  176.509995  433.570007  176.750000  433.820007  52517000   75433200
2023-10-17  177.149994  436.019989  177.149994  436.019989  178.419998  438.140015  174.800003  432.450012  176.649994  432.809998  57549400   75324700
2023-10-18  175.839996  430.209991  175.839996  430.209991  177.580002  435.179993  175.110001  429.089996  175.580002  434.190002  54764400   93559800
2023-10-19  175.460007  426.429993  175.460007  426.429993  177.839996  432.820007  175.190002  425.730011  176.039993  430.950012  59302900  121323000
2023-10-20  172.880005  421.190002  172.880005  421.190002  175.419998  426.540009  172.639999  421.079987  175.309998  425.980011  64189300  123845800
2023-10-23  173.000000  420.459991  173.000000  420.459991  174.009995  424.450012  169.929993  417.799988  170.910004  419.609985  55980100   92035100
2023-10-24  173.440002  423.630005  173.440002  423.630005  173.669998  424.820007  171.449997  420.739990  173.050003  422.649994  43816600   78564200
2023-10-25  171.100006  417.549988  171.100006  417.549988  173.059998  421.920013  170.649994  417.019989  171.880005  421.890015  57157000   94223200
2023-10-26  166.889999  412.549988  166.889999  412.549988  171.380005  417.329987  165.669998  411.600006  170.369995  416.450012  70625300  115156800
2023-10-27  168.220001  410.679993  168.220001  410.679993  168.960007  414.600006  166.830002  409.209991  166.910004  414.190002  58499100  107367700
2023-10-30  170.289993  415.589996  170.289993  415.589996  171.169998  416.679993  168.869995  412.220001  169.020004  413.559998  51131000   86562700
2023-10-31  170.770004  418.200012  170.770004  418.200012  170.899994  418.529999  167.899994  414.209991  169.350006  416.179993  44846000   79665200
2023-11-01  173.970001  422.660004  173.970001  422.660004  174.229996  423.500000  170.119995  418.649994  171.000000  419.200012  56934900   98068100
2023-11-02  177.570007  430.760010  177.570007  430.760010  177.779999  430.920013  175.460007  426.559998  175.520004  426.579987  77334800   94938900
2023-11-03  176.649994  434.690002  176.649994  434.690002  176.820007  436.290009  173.350006  433.010010  174.240005  433.140015  79763700  100110800
2023-11-06  179.229996  435.690002  179.229996  435.690002  179.429993  436.149811  176.210007  433.679993  176.380005  435.470001  58830087   67646162
```

---

## More Examples

→ Check out this [Blog post](https://aroussi.com/#post/python-yahoo-finance) for a detailed tutorial with code examples.

[Changelog »](changelog.md)
