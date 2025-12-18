# logger.py
import logging
from datetime import datetime
from pathlib import Path

# Create log file ONCE
_current_date = datetime.now().strftime("%Y-%m-%d")
_current_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

LOG_DIR = Path("logs") / _current_date
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / f"{_current_timestamp}.log"

_LOGGING_CONFIGURED = False


def get_logger(name: str = __name__) -> logging.Logger:
    global _LOGGING_CONFIGURED

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not _LOGGING_CONFIGURED:
        formatter = logging.Formatter(
            "[%(asctime)s]: %(name)s: %(levelname)s: %(lineno)d: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.WARNING)
        console_handler.setFormatter(formatter)

        root_logger = logging.getLogger()
        root_logger.setLevel(logging.DEBUG)
        root_logger.addHandler(file_handler)
        root_logger.addHandler(console_handler)

        _LOGGING_CONFIGURED = True

    return logger