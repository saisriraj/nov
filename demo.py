from fuel_auto.logger import logging
import sys

logging.info("Welcome to r custome logging") 


from fuel_auto.exception import Auto_Exception

try:
    a = 8/0
except Exception as e:
    raise Auto_Exception(e,sys)