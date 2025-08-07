"""Stock price adapter."""

from typing import Dict

PRICES: Dict[str, float] = {
    "AAPL": 150.0,
    "MSFT": 250.0,
}


def get_stock_price(symbol: str) -> float:
    """Return the stock price for the given symbol.

    Parameters
    ----------
    symbol: str
        Stock ticker symbol.

    Returns
    -------
    float
        Price in USD. Returns 0.0 if the symbol is unknown.
    """
    return PRICES.get(symbol.upper(), 0.0)
