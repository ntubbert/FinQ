"""Unit tests for API routes using the built-in HTTP server."""

import json
from http.client import HTTPConnection
from threading import Thread

from api.routes import create_server


def run_server(server):
    server.serve_forever()


def make_request(path):
    server = create_server()
    thread = Thread(target=run_server, args=(server,), daemon=True)
    thread.start()
    host, port = server.server_address
    conn = HTTPConnection(host, port)
    conn.request("GET", path)
    response = conn.getresponse()
    data = response.read()
    server.shutdown()
    thread.join()
    return response.status, data


def test_read_stock_price():
    status, data = make_request("/stock/AAPL")
    assert status == 200
    assert json.loads(data) == {"symbol": "AAPL", "price": 150.0}


def test_read_stock_price_not_found():
    status, _ = make_request("/stock/UNKNOWN")
    assert status == 404


def test_read_crypto_price():
    status, data = make_request("/crypto/BTC")
    assert status == 200
    assert json.loads(data) == {"symbol": "BTC", "price": 20000.0}


def test_read_crypto_price_not_found():
    status, _ = make_request("/crypto/UNKNOWN")
    assert status == 404
