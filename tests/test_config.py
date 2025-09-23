"""Tests for configuration module."""

import pytest

from aws_blackbelt_mcp_server.config import _Env, env


class TestEnvConfig:
    """Test environment variable configuration."""

    def test_default_values(self):
        """Test that default values are set correctly."""
        # Test the actual env instance that's used in the application
        assert env.api_timeout == 30.0
        assert env.transport == "stdio"
        assert env.server_log_level == "INFO"
        assert env.log_rotation == "10 MB"
        assert env.log_retention == "7 days"

    def test_environment_variables_override(self, monkeypatch):
        """Test that environment variables override default values."""
        monkeypatch.setenv("API_TIMEOUT", "60.0")
        monkeypatch.setenv("TRANSPORT", "sse")
        monkeypatch.setenv("SERVER_LOG_LEVEL", "DEBUG")
        monkeypatch.setenv("LOG_ROTATION", "50 MB")
        monkeypatch.setenv("LOG_RETENTION", "30 days")

        # Create a new instance to test environment variable parsing
        env = _Env()

        assert env.api_timeout == 60.0
        assert env.transport == "sse"
        assert env.server_log_level == "DEBUG"
        assert env.log_rotation == "50 MB"
        assert env.log_retention == "30 days"

    def test_invalid_values(self, monkeypatch):
        """Test that invalid values raise validation error."""
        monkeypatch.setenv("TRANSPORT", "invalid")

        with pytest.raises(ValueError):
            _Env()
