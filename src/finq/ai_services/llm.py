from __future__ import annotations

"""LLM chat completion service adapter."""

import os
from typing import Any, Dict, Optional

from .base import BaseService


class LLMChatService(BaseService):
    """Adapter for OpenAI-style chat completion models."""

    def __init__(self, model: str = "gpt-3.5-turbo", client: Optional[Any] = None) -> None:
        self.model = model
        self.client = client
        self.api_key: Optional[str] = None

    def authenticate(self, api_key: Optional[str] = None) -> None:
        """Authenticate using an API key or environment variable."""
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if self.client is None:
            try:
                import openai  # type: ignore
            except Exception as exc:  # pragma: no cover - dependency optional
                raise RuntimeError("openai package is required for LLMChatService") from exc
            openai.api_key = self.api_key
            self.client = openai

    def execute(self, prompt: str, **kwargs) -> Dict[str, Any]:
        """Send the prompt to the chat completion API."""
        if self.client is None:
            self.authenticate()
        response = self.client.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            **kwargs,
        )
        return response  # type: ignore[no-any-return]

    def format_output(self, response: Dict[str, Any]) -> str:
        """Return the assistant's message content."""
        try:
            return response["choices"][0]["message"]["content"].strip()
        except Exception as exc:  # pragma: no cover - defensive
            raise ValueError("Unexpected response format") from exc
