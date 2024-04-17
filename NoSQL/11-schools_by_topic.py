#!/usr/bin/env python3
"""excersise 11: Pyfunc that returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """specific topic return"""
    return mongo_collection.find({"topics": topic})
