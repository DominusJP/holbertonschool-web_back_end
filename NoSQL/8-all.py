#!/usr/bin/env python3
"""escersise 8: Py function that lists all documents in collection"""


def list_all(mongo_collection):
    """function that lists all documents in collection"""
    if not mongo_collection:
        return []
    return mongo_collection.find()
