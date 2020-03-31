from list import raw_list_10000
from datetime import datetime
from settings import logger_settings

import logging.config

logger = logging.getLogger(__name__)

logging.config.dictConfig(logger_settings)


"""
 procedure bubbleSort( A : lista elementów do posortowania )
   n = liczba_elementów(A)
    do
     for (i = 0; i < n-1; i++) do:
       if A[i] > A[i+1] then
         swap(A[i], A[i+1])
       end if
     end for
     n = n-1
   while n > 1
 end procedure

"""


t0 = datetime.now()

raw_list = raw_list_10000
t1 = datetime.now()
logger.info(f't1 - t0 = {t1-t0}')
list_check = 0
while list_check < len(raw_list):
    for i in range(len(raw_list)-1):
        if raw_list[i+1]-raw_list[i]==1:
            list_check +=1
        else:
            list_check = 0
            for k in range(len(raw_list) - 1):
                if raw_list[k] > raw_list[k + 1]:
                    tmp = raw_list[k]
                    raw_list[k] = raw_list[k + 1]
                    raw_list[k + 1] = tmp

t_fin = datetime.now()
logger.info(f't_fin - t1 = {t_fin-t1}')





