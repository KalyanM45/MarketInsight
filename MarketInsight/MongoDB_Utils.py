import pymongo
import pandas as pd

# Initialize the MongoDB client and database
client = pymongo.MongoClient("mongodb+srv://kalyan:kalyan@cluster0.vnsa8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
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