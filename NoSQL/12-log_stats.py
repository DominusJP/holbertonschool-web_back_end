#!/usr/bin/env python3
"""Log stats"""
import pymongo


def nginx_logs_stats(mongo_uri, database_name='logs', collection_name='nginx'):
    # Connect to MongoDB
    client = pymongo.MongoClient(mongo_uri)
    db = client[database_name]
    collection = db[collection_name]
    # Get the total number of logs
    total_logs = collection.count_documents({})
    # Display total logs
    print(f"{total_logs} logs where {total_logs} is the number of documents in this collection")
    # Display methods stats
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({'method': method})
        print(f"\t{count} logs with method={method}")
    # Display stats for specific method and path
    special_logs_count = collection.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{special_logs_count} logs with method=GET and path=/status")
if __name__ == "__main__":
    # Replace 'your_mongo_uri' with the actual URI for your MongoDB instance
    # Example: "mongodb://username:password@localhost:27017/"
    mongo_uri = 'your_mongo_uri'
    nginx_logs_stats(mongo_uri)