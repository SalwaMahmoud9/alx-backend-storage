#!/usr/bin/env python3
""" 11 """


def schools_by_topic(mongo_collection, topic):
    """ schools_by_topic """
    documents = mongo_collection.find({"topics": topic})
    list_docs = [d for d in documents]
    return list_docs
