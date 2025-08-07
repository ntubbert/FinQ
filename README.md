# FinQ

[![CI](https://github.com/OWNER/FinQ/actions/workflows/ci.yml/badge.svg)](https://github.com/OWNER/FinQ/actions/workflows/ci.yml)
[![Coverage Status](https://img.shields.io/codecov/c/github/OWNER/FinQ.svg)](https://codecov.io/gh/OWNER/FinQ)

FinQ is an early-stage project for building a financial question answering service powered by FastAPI, SQLAlchemy, and LangChain.

## Goals
- Provide a simple API for querying financial data using natural language.
- Leverage large language models through LangChain.
- Persist and manage data with SQLAlchemy.

## Usage
1. Copy `.env.example` to `.env` and populate the required keys.
2. Install dependencies with `pip install -e .`.
3. Start the development server using `uvicorn finq.main:app --reload`.

This repository currently contains scaffolding for further development.
