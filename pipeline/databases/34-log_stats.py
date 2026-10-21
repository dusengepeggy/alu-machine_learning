#!/usr/bin/env python3
"""
Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def log_stats(mongo_collection):
    """Print stats about Nginx request logs"""
    total = mongo_collection.count_documents({})
    print(f"{total} logs")

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status = mongo_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{status} status check")


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    log_stats(client.logs.nginx)
