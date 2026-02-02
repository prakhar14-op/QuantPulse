"""
QuantPulse Backend Configuration

This module contains configuration settings for the FastAPI application.
Environment-specific settings can be loaded from .env files in the future.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Application metadata
APP_NAME = "QuantPulse India Backend"
APP_VERSION = "0.1.0"
APP_DESCRIPTION = "Backend API service for QuantPulse India stock analytics platform"

# API Keys
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

# CORS Configuration
# These origins are allowed to make requests to this API
# Add your frontend URLs here
ALLOWED_ORIGINS = [
    "http://localhost:3000",      # Vite dev server (default)
    "http://localhost:5173",      # Vite dev server (alternative)
    "http://localhost:5174",      # Vite dev server (second instance)
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:5174",
    "http://localhost:8080",      # Alternative dev port
]

# Server Configuration
HOST = "0.0.0.0"
PORT = 8000
