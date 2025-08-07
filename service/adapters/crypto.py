"""Cryptocurrency price adapter."""

from typing import Dict

PRICES: Dict[str, float] = {
    "BTC": 20000.0,
    "ETH": 1500.0,
}


def get_crypto_price(symbol: str) -> float:
    """Return the cryptocurrency price for the given symbol.

    Parameters
    ----------
    symbol: str
        Cryptocurrency ticker symbol.

    Returns
    -------
    float
        Price in USD. Returns 0.0 if the symbol is unknown.
    """
    return PRICES.get(symbol.upper(), 0.0)
