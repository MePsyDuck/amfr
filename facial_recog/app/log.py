import datetime
import logging
import os

from .config import log_dir


def setup_logger():
    os.mkdir(log_dir)
    logging.basicConfig(
        filename=os.path.join(log_dir, str(datetime.datetime.now().strftime('%Y%m%d_%H%M%S.log'))),
        filemode='w',
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
