"""Unit tests for service adapters."""

from service.adapters.crypto import get_crypto_price
from service.adapters.stock import get_stock_price


def test_get_stock_price_known_symbol():
    assert get_stock_price("AAPL") == 150.0


def test_get_stock_price_unknown_symbol():
    assert get_stock_price("UNKNOWN") == 0.0


def test_get_crypto_price_known_symbol():
    assert get_crypto_price("BTC") == 20000.0


def test_get_crypto_price_unknown_symbol():
    assert get_crypto_price("UNKNOWN") == 0.0
