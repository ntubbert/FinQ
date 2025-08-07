"""Command line interface for FinQ."""
from __future__ import annotations

import click
import uvicorn

from .service_adapters import QuoteService


@click.group()
def cli() -> None:
    """Entry point for FinQ commands."""


@cli.command()
@click.argument("ticker")
def quote(ticker: str) -> None:
    """Fetch a quote for ``TICKER`` and print the price."""
    service = QuoteService()
    data = service.get_quote(ticker)
    click.echo(f"{data['ticker']}: {data['price']}")


@cli.command()
@click.option("--host", default="127.0.0.1", show_default=True)
@click.option("--port", default=8000, show_default=True, type=int)
def serve(host: str, port: int) -> None:
    """Run the FinQ API server."""
    uvicorn.run("finq.api:app", host=host, port=port)


if __name__ == "__main__":
    cli()
