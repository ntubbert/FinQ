"""FastAPI routers for FinQ services."""
from __future__ import annotations

from fastapi import APIRouter, Depends

from ..service_adapters import QuoteService

router = APIRouter(prefix="/quote", tags=["quote"])


def get_quote_service() -> QuoteService:
    return QuoteService()


@router.get("/{ticker}")
async def read_quote(
    ticker: str,
    service: QuoteService = Depends(get_quote_service),
):
    """Return quote data for the given ticker."""
    return service.get_quote(ticker)
