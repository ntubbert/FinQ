"""FinQ API package exposing the FastAPI application."""
from __future__ import annotations

from fastapi import FastAPI

from .auth import APIKeyMiddleware
from .routes import router


app = FastAPI(title="FinQ API")
app.add_middleware(APIKeyMiddleware)
app.include_router(router)

__all__ = ["app"]
