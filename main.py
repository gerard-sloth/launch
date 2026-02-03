from pymongo import MongoClient
from config import settings

client = MongoClient(settings.mongo_uri)

if __name__ == "__main__":
    databases = client.list_database_names()
    print("Databases:", databases)
    
    for db_name in databases:
        db = client[db_name]
        collections = db.list_collection_names()
        print(f"Database '{db_name}': {len(collections)} collections - {collections}")
        
        # Optional: Show sample documents from first collection
        if collections:
            collection = db[collections[0]]
            sample_docs = list(collection.find().limit(3))
            print(f"  Sample from '{collections[0]}': {len(sample_docs)} docs")
            for doc in sample_docs:
                print(f"    {doc}")
        print()