# Smarter scraping

To use a custom `requests` session (for example to cache calls to the
API or customize the `User-agent` header), pass a `session=` argument to
the `Ticker` constructor.

```py title="Cache Example" linenums="1" hl_lines="5-7"
import yfinance as yf

import requests_cache

session = requests_cache.CachedSession('yfinance.cache')
session.headers['User-agent'] = 'my-program/1.0'
ticker = yf.Ticker('msft', session=session)

# The scraped response will be stored in the cache
ticker.actions
```

Combine a `requests_cache` with rate-limiting to avoid triggering Yahoo's rate-limiter/blocker that can corrupt data.

```py title="Cache Session Example" linenums="1" hl_lines="3-15"
import yfinance as yf

from requests import Session
from requests_cache import CacheMixin, SQLiteCache
from requests_ratelimiter import LimiterMixin, MemoryQueueBucket
from pyrate_limiter import Duration, RequestRate, Limiter

class CachedLimiterSession(CacheMixin, LimiterMixin, Session):
    pass

session = CachedLimiterSession(
    limiter=Limiter(RequestRate(2, Duration.SECOND*5)),  # max 2 requests per 5 seconds
    bucket_class=MemoryQueueBucket,
    backend=SQLiteCache("yfinance.cache"),
)

ticker = yf.Ticker('msft', session=session)
```
