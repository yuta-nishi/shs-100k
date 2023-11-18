import logging

# ANSI escape codes for colored logging
# class _CustomFormatter(logging.Formatter):
#     grey = "\x1b[38;21m"
#     green = "\x1b[32;21m"
#     yellow = "\x1b[33;21m"
#     red = "\x1b[31;21m"
#     bold_red = "\x1b[31;1m"
#     reset = "\x1b[0m"
#     log_format = "%(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)d)"

#     FORMATS = {
#         logging.DEBUG: grey + log_format + reset,
#         logging.INFO: green + log_format + reset,
#         logging.WARNING: yellow + log_format + reset,
#         logging.ERROR: red + log_format + reset,
#         logging.CRITICAL: bold_red + log_format + reset,
#     }

#     def format(self, record: logging.LogRecord) -> str:
#         log_format = self.FORMATS.get(record.levelno)
#         formatter = logging.Formatter(log_format)

#         return formatter.format(record)


def setup_logging() -> logging.Logger:
    LOG_PATH = "/Users/yutanishi/shs-100k/src/log/youtube_downloader.log"

    # Set up logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Set up file handler
    file_handler = logging.FileHandler(LOG_PATH)
    file_handler.setLevel(logging.INFO)

    # Set up console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
