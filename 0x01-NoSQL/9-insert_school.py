#!/usr/bin/env python3
""" 9 """


def insert_school(mongo_collection, **kwargs):
    """ insert_school """
    document_id = mongo_collection.insert(kwargs)
    return document_id
