import os
import pprint

from dotenv import load_dotenv
from pymongo import MongoClient

from bson.objectid import ObjectId

# Load environment variables
load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')

# Connect to MongoDB
client = MongoClient(MONGO_URI)

# Select database
db = client.bank

# Select collection
accounts_collection = db.accounts

# Update one document
documento_to_update = {"_id": ObjectId("5f1d7a3f9d9b3b3d7c9b9b9b")}

# Update one document
add_to_balance = {"$inc": {"balance": 100}}

# Print original document
pprint.pprint(accounts_collection.find_one(documento_to_update))

# Update one document
result = accounts_collection.update_one(documento_to_update, add_to_balance)
print(f"Documents updated: {str(result.modified_count)}")

# Print updated document
pprint.pprint(accounts_collection.find_one(documento_to_update))


# Update many documents
document_to_update = {"balance": {"$lt": 1000}}

# Update many documents
add_to_balance = {"$inc": {"balance": 100}}

# Print original documents
for account in accounts_collection.find(document_to_update):
    pprint.pprint(account)

# Update many documents
result = accounts_collection.update_many(document_to_update, add_to_balance)

print(f"Documents matches: {str(result.matched_count)}")
print(f"Documents updated: {str(result.modified_count)}")

# Print updated documents
for account in accounts_collection.find(document_to_update):
    pprint.pprint(account)

client.close()
