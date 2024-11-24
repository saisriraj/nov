import sys

from fuel_auto.exception import Auto_Exception
from fuel_auto.logger import logging

import os
from fuel_auto.constants import DATABASE_NAME, MONGODB_URL_KEY
import pymongo
import certifi


from pymongo.mongo_client import MongoClient
import urllib.parse
# Encode the username and password
username = urllib.parse.quote_plus('saisriraj5')
password = urllib.parse.quote_plus('Srir@j1996')



DB_NAME = 'automobile'
COLLECTION_NAME= 'auto_data'
# Construct the encoded URI

url = 'mongodb+srv://saisriraj5:Srir@j1996@cluster0.leajo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'




CONNECTION_URL = f'mongodb+srv://{username}:{password}@cluster0.leajo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'



ca = certifi.where()

class MongoDBClient:
    """
    Class Name :   export_data_into_feature_store
    Description :   This method exports the dataframe from mongodb feature store as dataframe 
    
    Output      :   connection to mongodb database
    On Failure  :   raises an exception
    """
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = CONNECTION_URL
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection succesfull")
        except Exception as e:
            raise Auto_Exception(e,sys)