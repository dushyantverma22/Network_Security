from pymongo.mongo_client import MongoClient
from urllib.parse import quote_plus
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Encode the username and password to escape special characters
username = quote_plus("dushyantdchss")
password = quote_plus("admin@1234")  # Uncomment this line if using password from code

# Alternatively, you can load password from environment variables as well
# password = quote_plus(os.getenv("MONGO_DB_PASSWORD"))

# Retrieve MongoDB URL from environment variable
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

# Construct URI with encoded username and password
uri = f"mongodb+srv://{username}:{password}@cluster0.9ktju.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Print URI to verify (optional)
print("MongoDB URI:", uri)

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Connection failed:", e)
