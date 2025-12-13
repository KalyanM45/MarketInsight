import logging
import os
from datetime import datetime
from pathlib import Path


def get_logger(name: str = __name__) -> logging.Logger:
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Avoid adding handlers multiple times
    if logger.handlers:
        return logger
    
    # Create log directory structure
    current_date = datetime.now().strftime("%Y-%m-%d")
    current_timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    
    log_dir = Path("logs") / current_date
    log_dir.mkdir(parents=True, exist_ok=True)
    
    log_file = log_dir / f"{current_timestamp}.log"
    
    # Create formatters with your custom format
    # [YYYY-MM-DD HH:MM:SS]: app_name: TYPE: line_no: message
    file_formatter = logging.Formatter(
        '[%(asctime)s]: %(name)s: %(levelname)s: %(lineno)d: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_formatter = logging.Formatter(
        '[%(asctime)s]: %(name)s: %(levelname)s: %(lineno)d: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # File handler - logs everything
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(file_formatter)
    
    # Console handler - logs only WARNING and ERROR
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(console_formatter)
    
    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger