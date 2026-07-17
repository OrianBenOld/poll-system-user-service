import os

class Config:
    """Database configuration for User Service"""
    DB_HOST = os.getenv("USER_DB_HOST", "localhost")
    DB_PORT = int(os.getenv("USER_DB_PORT", 3307))
    DB_USER = os.getenv("USER_DB_USER", "root")
    DB_PASSWORD = os.getenv("USER_DB_PASSWORD", "root_password")
    DB_NAME = os.getenv("USER_DB_NAME", "user_db")

    # Poll service URL for inter-service communication
    POLL_SERVICE_URL = os.getenv("POLL_SERVICE_URL", "http://localhost:8002")

config = Config()
