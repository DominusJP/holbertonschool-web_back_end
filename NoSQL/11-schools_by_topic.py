#!/usr/bin/env python3
"""Where can I learn Python?"""


def schools_by_topic(mongo_collection, topic):
    """Find schools that have the specified topic"""
    cursor = mongo_collection.find({'topics': {'$in': [topic]}})
    """Extract school names from the cursor"""
    school_names = [document['name'] for document in cursor]
    return school_names