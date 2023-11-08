"""Provides code to retrieve data from the Yahoo Finance API."""
from typing import Optional, Dict, Any, Union
from functools import wraps, lru_cache

import requests
from frozendict import frozendict

cache_maxsize = 64


def lru_cache_freezeargs(func):
    """
    Decorator transforms mutable dictionary and list arguments into immutable types
    Needed so lru_cache can cache method calls what has dict or list arguments.
    """

    @wraps(func)
    def wrapped(*args, **kwargs):
        args = tuple(
            [frozendict(arg) if isinstance(arg, dict) else arg for arg in args]
        )
        kwargs = {
            k: frozendict(v) if isinstance(v, dict) else v for k, v in kwargs.items()
        }
        args = tuple([tuple(arg) if isinstance(arg, list) else arg for arg in args])
        kwargs = {k: tuple(v) if isinstance(v, list) else v for k, v in kwargs.items()}
        return func(*args, **kwargs)

    # copy over the lru_cache extra methods to this wrapper to be able to access them
    # after this decorator has been applied
    wrapped.cache_info = func.cache_info
    wrapped.cache_clear = func.cache_clear
    return wrapped


class TickerData:
    """
    A class to centralize the retrieval of data from the Yahoo Finance API.

    This class is designed to facilitate the fetching of financial data by providing
    a single point of access to the Yahoo API. It also aims to improve performance
    by implementing caching mechanisms that can reduce the need for repeated API calls
    and speed up data retrieval processes.

    Attributes:
        user_agent_headers:
            A dictionary containing the default headers to use for HTTP requests,
            simulating a user-agent to avoid being blocked by Yahoo.
        ticker:
            The ticker symbol for the financial instrument of interest.
        _session:
            The HTTP session to use for requests, defaults to `requests` if not provided.
    """

    user_agent_headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
    }

    def __init__(self, ticker: str, session: Optional[requests.Session] = None) -> None:
        """
        Initialize the TickerData object with a ticker symbol and an optional HTTP session.

        Args:
            ticker: The ticker symbol to retrieve data for.
            session: An optional session object to use for making HTTP requests.
                     If not provided, the default `requests` library session is used.
        """
        self.ticker = ticker
        self._session = session or requests

    def get(
        self,
        url: str,
        user_agent_headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        proxy: Optional[Union[str, Dict[str, str]]] = None,
        timeout: float = 30,
    ) -> requests.Response:
        """
        Perform an HTTP GET request.

        Args:
            url: The URL to send the request to.
            user_agent_headers: Custom headers to use for the request.
            params: URL parameters to append to the request.
            proxy: Proxy configuration for the request.
            timeout: How many seconds to wait for the server to send data before giving up.

        Returns:
            Response: The response object resulting from the request.
        """
        proxy = self._get_proxy(proxy)
        response = self._session.get(
            url=url,
            params=params,
            proxies=proxy,
            timeout=timeout,
            headers=user_agent_headers or self.user_agent_headers,
        )
        return response

    @lru_cache_freezeargs
    @lru_cache(maxsize=cache_maxsize)
    def cache_get(
        self,
        url: str,
        user_agent_headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        proxy: Optional[Union[str, Dict[str, str]]] = None,
        timeout: float = 30,
    ) -> requests.Response:
        """
        Cached HTTP GET request to reduce repeated calls for the same request.

        This method uses `functools.lru_cache` to cache the results of HTTP GET requests,
        which can significantly improve performance when the same requests are made multiple times.

        Args:
            url: The URL to send the request to.
            user_agent_headers: Custom headers to use for the request.
            params: URL parameters to append to the request.
            proxy: Proxy configuration for the request.
            timeout: How many seconds to wait for the server to send data
                                              before giving up.

        Returns:
            Response: The response object resulting from the request.
        """
        return self.get(url, user_agent_headers, params, proxy, timeout)

    def _get_proxy(
        self, proxy: Optional[Union[str, Dict[str, str]]]
    ) -> Optional[Dict[str, str]]:
        """
        Set up the proxy configuration in the format expected by requests.

        This is a private method used internally by the `get` and `cache_get` methods.

        Args:
            proxy (str or dict): The proxy settings to be formatted.

        Returns:
            dict: A dictionary with the proxy settings formatted for use with `requests`.
        """
        # setup proxy in requests format
        if proxy is not None:
            if isinstance(proxy, (dict, frozendict)) and "https" in proxy:
                proxy = proxy["https"]
            proxy = {"https": proxy}
        return proxy

    def get_raw_json(
        self,
        url: str,
        user_agent_headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        proxy: Optional[Union[str, Dict[str, str]]] = None,
        timeout: float = 30,
    ) -> Dict[str, Any]:
        """
        Get the JSON content from a URL and return it as a dictionary.

        This method makes an HTTP GET request and parses the JSON content of the response.

        Args:
            url: The URL to retrieve the JSON from.
            user_agent_headers: Custom headers to use for the request.
            params: URL parameters to append to the request.
            proxy: Proxy configuration for the request.
            timeout: How many seconds to wait for the server to send data
                                              before giving up.

        Returns:
            dict: The parsed JSON content from the response.
        """
        response = self.get(
            url,
            user_agent_headers=user_agent_headers,
            params=params,
            proxy=proxy,
            timeout=timeout,
        )
        response.raise_for_status()
        return response.json()
