from pymongo.mongo_client import MongoClient
from urllib.parse import quote_plus

# Encode the username and password to escape special characters
username = quote_plus("dushyantdchss")
password = quote_plus("Admin@23")

# Replace in the URI with encoded values
#uri = f"mongodb+srv://{username}:{password}@cluster0.9ktju.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


#from pymongo.mongo_client import MongoClient

uri = f"mongodb+srv://dushyantdchss:{password}@cluster0.9ktju.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
