"""
logger.py

Centralized logging module for the Originating Address Tool.
Logs all events to both terminal and a log file.
"""

import logging
from pathlib import Path

# Ensure logs directory exists
LOG_FILE = Path("logs/activity.log")
LOG_FILE.parent.mkdir(exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


def log_info(message: str):
    """Logs an informational message to terminal and file."""
    print(f"[INFO] {message}")
    logging.info(message)


def log_warning(message: str):
    """Logs a warning message to terminal and file."""
    print(f"[WARN] {message}")
    logging.warning(message)


def log_error(message: str):
    """Logs an error message to terminal and file."""
    print(f"[ERROR] {message}")
    logging.error(message)


def log_success(message: str):
    """Logs a success message to terminal and file."""
    print(f"[SUCCESS] {message}")
    logging.info(message)
