#!/usr/bin/env python3
"""excersise 9: py function that inserts a new document in kwargs"""


def insert_school(mongo_collection, **kwargs):
    """function: insert school"""
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
