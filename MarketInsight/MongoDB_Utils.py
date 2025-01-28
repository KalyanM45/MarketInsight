import pymongo
import pandas as pd

# Initialize the MongoDB client and database
client = pymongo.MongoClient()
db = client["MarketInsight"]

def Push_Records(records, collection_name):
    """
    Pushes records to the specified collection in the MongoDB database
    """
    collection = db[collection_name]
    if isinstance(records, list):  # If records is a list, insert as multiple
        collection.insert_many(records)
    elif isinstance(records, dict):  # If records is a single dictionary, insert as one
        collection.insert_one(records)
    else:
        raise ValueError("Records should be a dictionary or a list of dictionaries")
    print(f"{len(records)} Records Inserted into Collection: {collection_name} in DB: MarketInsight")


def Get_Records(collection_name):
    """
    Retrieves records from the specified collection in the MongoDB database
    """
    collection = db[collection_name]
    records = collection.find()
    records = pd.DataFrame(records)
    return records

def Delete_Records(collection_name):
    """
    Deletes all records from the specified collection in the MongoDB database
    """
    collection = db[collection_name]
    result = collection.delete_many({})
    print(f"{result.deleted_count} Records Deleted from Collection: {collection_name} in DB: MarketInsight")
