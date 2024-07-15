#!/usr/bin/env python3
""" 8 """


def list_all(mongo_collection):
    """ list_all """
    documents = mongo_collection.find()

    if documents.count() == 0:
        return []

    return documents
