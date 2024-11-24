import os
from datetime import date

DATABASE_NAME = "automobile"

COLLECTION_NAME = "auto_data"

MONGODB_URL_KEY = "MONGODB_URL"

PIPELINE_NAME: str = "fuel_auto"

ARTIFACT_DIR: str = "artifact"


TRAIN_FILE_NAME: str = "train.csv"

TEST_FILE_NAME: str = "test.csv"

FILE_NAME: str = "auto_imports1.csv"

MODEL_FILE_NAME = "model.pkl"


"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "auto_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2



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

MONGODB_URL_KEY = CONNECTION_URL

