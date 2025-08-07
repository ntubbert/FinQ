from __future__ import annotations

"""Registry for dynamically loading FinQ services."""

from importlib import import_module
from typing import Any, Dict, Type

from .ai_services.base import BaseService

# Mapping of service names to their import paths
_SERVICE_PATHS: Dict[str, str] = {
    "llm_chat": "finq.ai_services.llm:LLMChatService",
    "ocr_summarizer": "finq.ai_services.ocr:OCRSummarizerService",
    "forecasting": "finq.ai_services.forecasting:ForecastingService",
}


def get_service(name: str, **kwargs) -> BaseService:
    """Instantiate a service by name.

    Parameters
    ----------
    name:
        Registered service name.
    kwargs:
        Keyword arguments passed to the service constructor.
    """
    path = _SERVICE_PATHS.get(name)
    if path is None:
        raise KeyError(f"Service '{name}' is not registered")

    module_name, class_name = path.split(":")
    module = import_module(module_name)
    cls: Type[BaseService] = getattr(module, class_name)
    return cls(**kwargs)
