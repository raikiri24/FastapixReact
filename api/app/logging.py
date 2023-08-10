import logging
from app.config import settings


logger = logging.getLogger(__name__)


def init_logger():
    if settings.log_level == "DEBUG":
        logger.setLevel(logging.DEBUG)
    elif settings.LOG_LEVEL == 'INFO':
        logger.setLevel(logging.INFO)
    elif settings.LOG_LEVEL == 'WARNING':
        logger.setLevel(logging.WARNING)
    elif settings.LOG_LEVEL == 'ERROR':
        logger.setLevel(logging.ERROR)
    else:
        logger.setLevel(logging.CRITICAL)

    stream_handler = logging.StreamHandler()

    formatter = logging.Formatter(settings.log_format)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
