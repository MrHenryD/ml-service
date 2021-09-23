import os
import logging


LOGGING__LOG_LEVEL = os.environ.get("LOGGING__LOG_LEVEL", logging.DEBUG)

SERVICE__HOST = os.environ.get("SERVICE__HOST", "0.0.0.0")
SERVICE__PORT = int(os.environ.get("SERVICE__PORT", 8080))
SERVICE__DEBUG = os.environ.get("SERVICE__DEBUG", True)