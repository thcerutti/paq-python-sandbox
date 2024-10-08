import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

mongoDBuser = os.getenv('MONGO_USER')
mongoDBpassword = os.getenv('MONGO_PASSWORD')
mongoDBurl = os.getenv('MONGO_DB_URL')
mongoDBparams = os.getenv('MONGO_PARAMS')
fullUrl = f"mongodb+srv://{mongoDBuser}:{mongoDBpassword}@{mongoDBurl}/?{mongoDBparams}"
print(fullUrl)

# uri = "mongodb+srv://cerutti:iIf3bnKf7G6CA2lD@paq-db.z6n6d.mongodb.net/?retryWrites=true&w=majority&appName=paq-db"

# Create a new client and connect to the server
client = MongoClient(fullUrl, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

    # Connect to the sample_mflix database and retrieve the movies collection
    db = client.sample_mflix
    movies_collection = db.movies

    # Example: Print the first movie document
    first_movie = movies_collection.find_one()
    print(first_movie.get('plot'))
    print(first_movie)
    print('---------------')
    print(movies_collection.estimated_document_count())
except Exception as e:
    print(e)
