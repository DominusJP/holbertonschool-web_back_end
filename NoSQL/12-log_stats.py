#!/usr/bin/env python3
"""excersise 12: Py script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.logs
collection = db.nginx

# Count total number of logs
total_logs = collection.count_documents({})

print(f"{total_logs} logs where {total_logs} is the number of documents in this collection")

# Count methods
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents({"method": method}) for method in methods}

print("Methods:")
for method, count in method_counts.items():
    print(f"\t{count} logs with method {method}")

# Count logs with method=GET and path=/status
status_logs = collection.count_documents({"method": "GET", "path": "/status"})
print(f"{status_logs} logs with method=GET and path=/status")
