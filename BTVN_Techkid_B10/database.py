from pymongo import MongoClient
from bson.objectid import ObjectId

mongo_uri = "mongodb+srv://admin:admin@cluster0-bg51p.mongodb.net/test?retryWrites=true"
client = MongoClient(mongo_uri)

# 2. Get / Create database
biker = client.biker_database

# 3. Get / Create collection
biker_collection = biker["biker_collection"]