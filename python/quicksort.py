from list import raw_list_10000
from datetime import datetime
from settings import logger_settings
from time import sleep

import logging.config

logger = logging.getLogger(__name__)

logging.config.dictConfig(logger_settings)


t0 = datetime.now()

# raw_list = [5, 4, 10, 2, 1]
t1 = datetime.now()
logger.info(f't1 - t0 = {t1-t0}')

def separator(array_to_sort):

    low_list=[]
    high_list=[]

    if len(array_to_sort)>1:
        core_key = array_to_sort[0]
        for k in array_to_sort:
            if k < core_key:
                low_list.append(k)
            elif k > core_key:
                high_list.append(k)

        return separator(low_list) + [core_key] + separator(high_list)
    else:
        return array_to_sort

print(separator(raw_list_10000))
t_fin = datetime.now()
logger.info(f't_fin - t1 = {t_fin-t1}')