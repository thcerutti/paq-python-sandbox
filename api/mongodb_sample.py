from Models.db import get_client, ping_db, get_collection

# Send a ping to confirm a successful connection
try:
    # Create a new client and connect to the server
    client = get_client() # MongoClient(fullUrl, server_api=ServerApi('1'))
    ping_db(client)
    mv = get_collection(client, 'sample_mflix', 'movies')
    print(mv.find_one())
except Exception as e:
    print(e)
