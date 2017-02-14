import logging
from my_proj.m2.m2_src import m2f

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def m1f():
    logger.critical("Appearing coz log level >= DEBUG")
    logger.error("Appearing coz log level  >= DEBUG")
    logger.warning("Appearing coz log level >= DEBUG")
    logger.info("Appearing coz log level >= DEBUG")
    logger.debug("Appearing coz log level >= DEBUG")
    m2f()
