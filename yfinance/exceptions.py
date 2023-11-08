"""Exceptions for `yfinance` library."""


class YFinanceException(Exception):
    """
    Base exception class for `yfinance` errors.

    This exception is the base class for all other exceptions raised by the `yfinance` library.
    It acts as a catch-all for any `yfinance`-specific issues that do not fall under more specific exception categories.
    """


class YFinanceDataException(YFinanceException):
    """
    Exception raised for errors in retrieving data from `yfinance`.

    This exception indicates that an error occurred while attempting to fetch financial data.
    It could be due to issues like network problems, data unavailability, or unexpected changes in the data source's API.
    """


class YFNotImplementedError(NotImplementedError):
    """
    Exception raised for unimplemented features in `yfinance`.

    Attributes:
        method_name (str): The name of the method that has not been implemented yet.

    Args:
        method_name (str): The name of the method that triggered the exception.

    This exception is raised when trying to use a feature or method that is acknowledged but not yet supported
    by the `yfinance` library, indicating future or potential implementation.
    """

    def __init__(self, method_name):
        super().__init__(
            f"Have not implemented fetching '{method_name}' from Yahoo API"
        )
