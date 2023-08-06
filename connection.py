import os

from datetime import datetime
from dotenv import load_dotenv
from pymongo import MongoClient

# Load the MongoDB URI from the .env file and use it to connect to the database
load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

# Connect to the database
client = MongoClient(MONGODB_URI)

# Get reference to 'bank' database
db = client.bank

# Close the connection to the database
client.close()