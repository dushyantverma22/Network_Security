import os
import sys
import json
import pymongo

from dotenv import load_dotenv
load_dotenv()

from pymongo.mongo_client import MongoClient
from urllib.parse import quote_plus

MANGO_DB_PASSWORD = os.getenv("MONGODBPASSWORD")
password = quote_plus("Admin@12")
username = quote_plus("dushyantdchss")
# Replace in the URI with encoded values
uri = f"mongodb+srv://dushyantdchss:{password}@cluster0.9ktju.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

import certifi  ## certifi is used to check authensity
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo
from network_security.logging import logger
from network_security.exception.exception import NetworkSecurityException

class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_convert(self, file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            #records=json.loads(data.T.to_json().values())
            records = data.to_dict(orient="records")  # Convert DataFrame to list of dicts
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_mangodb(self,records,database,collection):
        try:
            self.database = database  # Remove comma here
            self.collection = collection  # Remove comma here
            self.mongo_client = pymongo.MongoClient(uri, tlsCAFile=ca)
            db = self.mongo_client[self.database]
            coll = db[self.collection]
            coll.insert_many(records)
            return len(records)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__=='__main__':
    FILE_PATH="Network_data\\phisingData.csv"
    DataBase="dushyant"
    Collection="Networkdata"
    networkobj=NetworkDataExtract()
    record=networkobj.csv_to_json_convert(file_path=FILE_PATH)
    print(record)
    no_of_records=networkobj.insert_data_mangodb(records=record, database=DataBase,collection=Collection)
    print(no_of_records)

        

