from __future__ import annotations

"""Time-series forecasting service using Prophet."""

from typing import Any

from .base import BaseService


class ForecastingService(BaseService):
    """Wraps the Prophet library to provide basic forecasts."""

    def __init__(self) -> None:
        self.model: Any = None

    def authenticate(self, *args, **kwargs) -> None:  # pragma: no cover
        """Prophet does not require authentication."""
        return None

    def execute(self, df, periods: int = 30, freq: str = "D"):
        """Fit a model and return a forecast DataFrame."""
        try:
            from prophet import Prophet
        except Exception as exc:  # pragma: no cover - dependency optional
            raise RuntimeError(
                "prophet package is required for ForecastingService"
            ) from exc

        self.model = Prophet()
        self.model.fit(df)
        future = self.model.make_future_dataframe(periods=periods, freq=freq)
        forecast = self.model.predict(future)
        return forecast

    def format_output(self, forecast):
        """Return commonly used columns from the forecast."""
        return forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]]
