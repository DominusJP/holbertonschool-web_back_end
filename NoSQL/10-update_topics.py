#!/usr/bin/env python3
"""Change school topics"""


def update_topics(mongo_collection, name, topics):
    """changes all school topics"""
    result = mongo_collection.update_many({'name': name},
                                          {'$set': {'topics': topics}})
    return result.modified_count