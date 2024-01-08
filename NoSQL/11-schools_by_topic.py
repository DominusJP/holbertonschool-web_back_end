#!/usr/bin/env python3
"""Where can I learn Python?"""


def schools_by_topic(mongo_collection, topic):
    """ returns the list of school with spec topics"""
    schools = []
    for school in mongo_collection.find({'topics': topic}):
        schools.append(school)
    return schools