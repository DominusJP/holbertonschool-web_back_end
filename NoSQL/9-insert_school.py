#!/usr/bin/env python3
"""Insert a document in Python"""


def insert_school(mongo_collection, **kwargs):
    """Insert a document in Python"""
    document_id = mongo_collection.insert(kwargs)
    return document_id