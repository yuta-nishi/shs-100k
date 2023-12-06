import logging


def setup_logging(log_path: str) -> logging.Logger:
    # Set up logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Set up file handler
    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel(logging.INFO)

    # Set up console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
