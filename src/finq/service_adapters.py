"""Service adapters providing financial data access."""
from __future__ import annotations

from typing import Dict


class QuoteService:
    """Adapter to retrieve stock quote data.

    For demonstration, this returns static data.
    In a real implementation, this would call an external API.
    """

    def get_quote(self, ticker: str) -> Dict[str, float]:
        """Return a static quote for the given ticker symbol."""
        return {"ticker": ticker.upper(), "price": 100.0}
