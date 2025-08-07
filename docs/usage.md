# FinQ Usage

## API

Start the server using the CLI:

```bash
python -m finq.cli serve
```

Then call the API using an API key:

```bash
export FINQ_API_KEY=secret
curl -H "X-API-Key: secret" http://localhost:8000/quote/AAPL
```

## Command Line

Fetch a quote directly from the command line:

```bash
python -m finq.cli quote AAPL
```
