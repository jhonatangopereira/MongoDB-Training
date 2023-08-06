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

# Get reference to 'accounts' collection
accounts_collection = db.accounts

new_account = {
    "account_holder": "Linus Torvalds",
    "account_id": 123456789,
    "account_type": "checking",
    "balance": 1000000,
    "last_updated": datetime.utcnow()
}

# Insert the new account into the database
result = accounts_collection.insert_one(new_account)

document_id = result.inserted_id
print(f"Inserted new account with ID {document_id}")


# Insert multiple accounts into the database
new_accounts = [
    {
        "account_holder": "Bill Gates",
        "account_id": 987654321,
        "account_type": "savings",
        "balance": 1000000000,
        "last_updated": datetime.utcnow()
    },
    {
        "account_holder": "Ada Lovelace",
        "account_id": 123123123,
        "account_type": "checking",
        "balance": 1000000,
        "last_updated": datetime.utcnow()
    },
    {
        "account_holder": "Alan Turing",
        "account_id": 456456456,
        "account_type": "savings",
        "balance": 1000000,
        "last_updated": datetime.utcnow()
    }
]

# Insert the new accounts into the database
result = accounts_collection.insert_many(new_accounts)

# Print out the IDs of the inserted documents
print(f"Inserted new accounts with IDs {result.inserted_ids}")