import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def m2f():
    logger.critical("Appearing since log level >= INFO")
    logger.error("Appearing since log level >= INFO")
    logger.warning("Appearing since log level >= INFO")
    logger.info("Appearing since log level >= INFO")
    logger.debug("Not Appearing since log level >= INFO")
