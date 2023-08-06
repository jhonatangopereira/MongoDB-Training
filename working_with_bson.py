from bson.objectid import ObjectId

# Create a new ObjectId
bson_example = {
    "_id": ObjectId("6173c8d9e4b0a9a9e4b0a9a9"),
    "name": "John",
    "age": 37,
    "address": {
        "street": "Main",
        "city": "New York",
        "state": "NY"
    }
}