"""Configuration for the server."""

import os

# API configuration
AWS_API_BASE_URL = "https://aws.amazon.com/api"
API_TIMEOUT = float(os.getenv("API_TIMEOUT", "30.0"))

# Logging configuration
SERVER_LOG_LEVEL = os.getenv("SERVER_LOG_LEVEL", "INFO")
LOG_ROTATION = os.getenv("LOG_ROTATION", "10 MB")
LOG_RETENTION = os.getenv("LOG_RETENTION", "7 days")
