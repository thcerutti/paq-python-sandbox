import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create a new client and connect to the server
def get_client():
  mongoDBuser = os.getenv('MONGO_USER')
  mongoDBpassword = os.getenv('MONGO_PASSWORD')
  mongoDBurl = os.getenv('MONGO_DB_URL')
  mongoDBparams = os.getenv('MONGO_PARAMS')
  fullUrl = f"mongodb+srv://{mongoDBuser}:{mongoDBpassword}@{mongoDBurl}/?{mongoDBparams}"
  return MongoClient(fullUrl, server_api=ServerApi('1'))

def ping_db(client):
  try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    return True
  except Exception as e:
    print(e)
    return False

def get_collection(client, db_name, collection_name):
  db = client[db_name]
  return db[collection_name]
