"""Configuration for the server."""

from fastmcp.server.server import Transport
from pydantic import Field
from pydantic_settings import BaseSettings


class _Env(BaseSettings):
    """Environment variables."""

    # API configuration
    api_timeout: float = Field(default=30.0)

    # Server configuration
    transport: Transport = Field(default="stdio")

    # Logging configuration
    server_log_level: str = Field(default="INFO")
    log_rotation: str = Field(default="10 MB")
    log_retention: str = Field(default="7 days")


env = _Env()
