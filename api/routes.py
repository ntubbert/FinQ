"""Simple HTTP API routes using the standard library."""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse

from service.adapters.crypto import get_crypto_price
from service.adapters.stock import get_stock_price


class RequestHandler(BaseHTTPRequestHandler):
    """Handle HTTP requests for stock and crypto prices."""

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path in ("/", "", "/index.html"):
            self._send_homepage()
            return

        parts = parsed.path.strip("/").split("/")
        if len(parts) != 2:
            self.send_error(404, "Not found")
            return
        kind, symbol = parts
        if kind == "stock":
            price = get_stock_price(symbol)
            if price == 0.0:
                self.send_error(404, "Stock not found")
                return
        elif kind == "crypto":
            price = get_crypto_price(symbol)
            if price == 0.0:
                self.send_error(404, "Crypto not found")
                return
        else:
            self.send_error(404, "Not found")
            return
        body = json.dumps({"symbol": symbol.upper(), "price": price}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_homepage(self) -> None:
        """Serve a simple HTML onboarding home screen."""
        body = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset=\"utf-8\">
    <title>FinQ Onboarding</title>
  </head>
  <body>
    <h1>Welcome to FinQ</h1>
    <p>Select an onboarding task to get started:</p>
    <ul>
      <li><a href=\"/onboarding/accounting\">Link to accounting software</a></li>
      <li><a href=\"/onboarding/bank\">Link to bank</a></li>
      <li><a href=\"/onboarding/data\">Link to data sources</a></li>
      <li><a href=\"/onboarding/business\">Describe business</a></li>
      <li><a href=\"/onboarding/goals\">Determine goals</a></li>
    </ul>
  </body>
</html>
""".strip().encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def create_server() -> HTTPServer:
    """Create an HTTP server bound to localhost on a random port."""
    return HTTPServer(("localhost", 0), RequestHandler)
