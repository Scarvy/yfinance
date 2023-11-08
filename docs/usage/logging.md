# Logging

`yfinance` uses the `logging` module to handle messages, default behaviour is only print errors.

If debugging, use `yf.enable_debug_mode()` to switch logging to debug with custom formatting.

```py title="Enable Logging Example" linenums="1" hl_lines="2"
import yfinance as yf
yf.enable_debug_mode()
```

Once enabled, you should see logs like this below:

```bash title="Logging Output Example"
yf.download("SPY AAPL", period="1mo")

DEBUG    Entering download()
DEBUG     Disabling multithreading because DEBUG logging enabled
DEBUG     Entering history()
DEBUG      AAPL: Yahoo GET parameters: {'range': '1mo', 'interval': '1d', 'includePrePost': False, 'events': 'div,splits,capitalGains'}
DEBUG      AAPL: yfinance received OHLC data: 2023-10-09 13:30:00 -> 2023-11-07 17:59:50
DEBUG      AAPL: OHLC after cleaning: 2023-10-09 09:30:00-04:00 -> 2023-11-07 12:59:50-05:00
DEBUG      AAPL: OHLC after combining events: 2023-10-09 00:00:00-04:00 -> 2023-11-07 00:00:00-05:00
DEBUG      AAPL: yfinance returning OHLC: 2023-10-09 00:00:00-04:00 -> 2023-11-07 00:00:00-05:00
DEBUG     Exiting history()
DEBUG     Entering history()
DEBUG      SPY: Yahoo GET parameters: {'range': '1mo', 'interval': '1d', 'includePrePost': False, 'events': 'div,splits,capitalGains'}
DEBUG      SPY: yfinance received OHLC data: 2023-10-09 13:30:00 -> 2023-11-07 17:59:51
DEBUG      SPY: OHLC after cleaning: 2023-10-09 09:30:00-04:00 -> 2023-11-07 12:59:51-05:00
DEBUG      SPY: OHLC after combining events: 2023-10-09 00:00:00-04:00 -> 2023-11-07 00:00:00-05:00
DEBUG      SPY: yfinance returning OHLC: 2023-10-09 00:00:00-04:00 -> 2023-11-07 00:00:00-05:00
DEBUG     Exiting history()
DEBUG    Exiting download()
```
