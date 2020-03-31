
from list import raw_list_10000
from datetime import datetime

from settings import logger_settings

import logging.config

logger = logging.getLogger(__name__)

logging.config.dictConfig(logger_settings)



t0 = datetime.now()

raw_list = raw_list_10000
t1 = datetime.now()
logger.info(f't1 - t0 = {t1-t0}')

raw_list.sort()

t_fin = datetime.now()
logger.info(f't_fin - t1 = {t_fin-t1}')

