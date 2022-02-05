from typing import Callable

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
from starlette.types import ASGIApp
from fastapi import Request
from config import BaseConfig


class NormaliseCacheQueryParams(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        if "nocache" in request.query_params:
            request.state.cache = {"nocache": True}
        else:
            request.state.cache = {"nocache": False}

        response = await call_next(request)
        return response


class NormaliseUnitQueryParams(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        units = {
            "speed": BaseConfig.BASE_UNITS.value,
            "temp": BaseConfig.BASE_UNITS.value
        }
        normalised_params = {}

        for param in units:
            if param in request.query_params:
                client_value = request.query_params[param]
                normalised_params[param] = client_value
            else:
                normalised_params[param] = units[param]

        request.state.units = normalised_params
        response = await call_next(request)
        return response
