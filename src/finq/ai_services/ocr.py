from __future__ import annotations

"""OCR and summarization service."""

from typing import Any, Dict, Optional

from .base import BaseService
from .llm import LLMChatService


class OCRSummarizerService(BaseService):
    """Perform OCR on an image and optionally summarize the text."""

    def __init__(self, llm_service: Optional[LLMChatService] = None) -> None:
        self.llm_service = llm_service or LLMChatService()

    def authenticate(self, **kwargs) -> None:
        """Proxy authentication to the LLM service if needed."""
        if self.llm_service:
            self.llm_service.authenticate(**kwargs)

    def execute(self, image_path: str, **kwargs) -> Dict[str, Any]:
        """Extract text from an image and optionally summarize it."""
        try:
            import pytesseract
            from PIL import Image
        except Exception as exc:  # pragma: no cover
            raise RuntimeError(
                "pytesseract and pillow packages are required for OCRSummarizerService"
            ) from exc

        text = pytesseract.image_to_string(Image.open(image_path))
        summary: Optional[str] = None
        if self.llm_service:
            prompt = f"Summarize the following text:\n\n{text}"
            response = self.llm_service.execute(prompt, **kwargs)
            summary = self.llm_service.format_output(response)
        return {"text": text, "summary": summary}

    def format_output(self, output: Dict[str, Any]) -> Dict[str, Any]:
        """Return OCR text and summary unchanged."""
        return output
