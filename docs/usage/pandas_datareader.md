# Using `pandas_datareader`

If your legacy code is using `pandas_datareader` and you wand to keep the code changes to minimum, you can simply call the override method and keep your code as it was:

```py title="Pandas DataReader Example" linenums="1" hl_lines="1 4"
from pandas_datareader import data as pdr

import yfinance as yf
yf.pdr_override()

# download dataframe using pandas_datareader
data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30")
```
