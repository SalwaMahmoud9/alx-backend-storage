#!/usr/bin/env python3
""" 101 """


def top_students(mongo_collection):
    """ top_students """

    top_st = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_st
