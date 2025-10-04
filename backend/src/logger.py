import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path


# Set up a formatter
formatter = logging.Formatter(
    fmt='%(levelname)s\t%(asctime)s\t%(funcName)s:\t%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

# Set up a StreamHandler for console logging
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.INFO)  # Adjust as needed

# Create and configure the root logger
logging.basicConfig(
    level=logging.DEBUG,  # Capture all levels of logs
    handlers=[console_handler],
)

# Example usage
logger = logging.getLogger('keenetic_api')
