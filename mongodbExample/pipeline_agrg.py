from pymongo import MongoClient
from bson.son import SON
import pprint

myclient = MongoClient("mongodb://%s:%s@127.0.0.1" % ('admin', 'admin'))

mydatabase = myclient['database']

mycollection = mydatabase['test2']

# sample_data = [
#     {"x": 1, "tags": ["dog", "cat"]},
#     {"x": 2, "tags": ["cat"]},
#     {"x": 2, "tags": ["mouse", "cat", "dog"]},
#     {"x": 3, "tags": []}
# ]
#
# result = mycollection.insert_many(sample_data)
# mycollection.insert_one({"x":4, "tags":["horse", "mouse", "ant"]})
pipeline = [
    {
        "$unwind": "$tags"  # 1 make flat hierarchy
    },
    {
        "$group": {"_id": "$tags", "count": {"$sum": 1}}  # 2 actual aggregation
    },
    {
        "$sort": SON([("count", -1), ("_id", -1)])  # 3 display
    }
]
pprint.pprint((list(mycollection.aggregate(pipeline))))
