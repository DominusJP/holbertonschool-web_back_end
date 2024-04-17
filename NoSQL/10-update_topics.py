#!/usr/bin/env python3
"""excersise 10: Py funct that changes all documents based on a name"""


def update_topics(mongo_collection, name, topics):
    """function: update topics"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
