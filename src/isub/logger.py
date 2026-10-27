"""Rotating logger for Isub."""

import logging
from logging.handlers import RotatingFileHandler


def setup_logger(log_path: str = "isub.log") -> logging.Logger:
    logger = logging.getLogger("Isub")
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    handler = RotatingFileHandler(
        log_path, maxBytes=5 * 1024 * 1024, backupCount=3, encoding="utf-8"
    )
    handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    )
    logger.addHandler(handler)
    return logger
