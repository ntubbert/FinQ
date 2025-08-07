"""Authentication middleware for the FinQ API."""
from __future__ import annotations

import os

from fastapi import HTTPException, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware


class APIKeyMiddleware(BaseHTTPMiddleware):
    """Simple API key authentication middleware."""

    def __init__(self, app, api_key: str | None = None) -> None:
        super().__init__(app)
        self.api_key = api_key or os.getenv("FINQ_API_KEY", "secret")

    async def dispatch(
        self, request: Request, call_next
    ) -> Response:  # type: ignore[override]
        key = request.headers.get("X-API-Key")
        if key != self.api_key:
            raise HTTPException(
                status_code=401, detail="Invalid or missing API key"
            )
        return await call_next(request)
