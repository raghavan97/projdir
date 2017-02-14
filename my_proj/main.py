import logging
from colorlog import ColoredFormatter
from my_proj.m1.m1_src import m1f


def setup_root_logger():
    formatter = ColoredFormatter(
        '%(log_color)s%(asctime)s:%(levelname)s:%(name)s:%(lineno)s'
        ':%(reset)s%(message)s'
    )

    logger = logging.getLogger('my_proj')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)


def main():
    setup_root_logger()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    logger.critical("Appearing coz log level >= ERROR")
    logger.error("Appearing coz log level for >= ERROR")
    logger.warning("Not appearing coz log level >= ERROR")
    logger.info("Not appearing coz log level >= ERROR")
    logger.debug("Not appearing coz log level >= ERROR")
    m1f()
