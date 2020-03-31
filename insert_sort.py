
from list import raw_list_10000
from datetime import datetime
from settings import logger_settings

import logging.config

logger = logging.getLogger(__name__)

logging.config.dictConfig(logger_settings)
from time import sleep

"""

0. Insert_sort(A, n)

1.  for i=2 to n :
2       # Wstaw A[i] w posortowany ciąg A[1 ... i-1]
3.      wstawiany_element = A[i]
4.      j = i - 1
5.      while j>0 and A[j]>wstawiany_element:
6.          A[j + 1] = A[j]
7.          j = j - 1
8.      A[j + 1] = wstawiany_element

"""

t0 = datetime.now()

raw_list = raw_list_10000
t1 = datetime.now()
logger.info(f't1 - t0 = {t1-t0}')
fin_list = [raw_list[0],raw_list[1]]

for k in range(2, len(raw_list)-1):
    # sleep(0.5)
    # print(fin_list)
    for l in range(len(fin_list)):
        if raw_list[k]<fin_list[0]:
            fin_list.insert(0, raw_list[k])
        elif fin_list[l+1]>raw_list[k] and raw_list[k]>fin_list[l]:
            fin_list.insert(l+1, raw_list[k])
        elif raw_list[k] > fin_list[len(fin_list)-1]:
            fin_list.insert(len(fin_list), raw_list[k])

print(fin_list)
t_fin = datetime.now()
logger.info(f't_fin - t1 = {t_fin-t1}')



