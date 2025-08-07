from __future__ import annotations

"""Base classes for AI services."""

from abc import ABC, abstractmethod


class BaseService(ABC):
    """Abstract base class for all AI powered services.

    Each service should implement its own authentication logic, main
    execution routine and formatting of the raw output into a consistent
    structure that FinQ consumers can rely on.
    """

    @abstractmethod
    def authenticate(self, *args, **kwargs) -> None:
        """Authenticate with the underlying provider."""

    @abstractmethod
    def execute(self, *args, **kwargs):
        """Run the service's main functionality and return raw output."""

    @abstractmethod
    def format_output(self, *args, **kwargs):
        """Post-process raw output into a structured format."""
