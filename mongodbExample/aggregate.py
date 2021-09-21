from pymongo import MongoClient

myclient = MongoClient("mongodb://%s:%s@127.0.0.1" % ('admin', 'admin'))

mydatabase = myclient['database']

mycollection = mydatabase['lang']

# profiles = [
#     {"user":"ram", "title":"Python"},
#     {"user":"ram", "title":"C++"},
#     {"user":"raj", "title":"Javascript"},
#     {"user":"john", "title":"MongoDB"},
#     {"user":"rohan", "title":"Perl"}
# ]
#
# mycollection.insert_many(profiles)

# cursor = mycollection.find()
# for r in cursor:
#     print(r)

agg_result = mycollection.aggregate(
    [
        {
            "$group":
                {
                    "_id": "$title",
                    "no_of_times": {"$sum": 1}
                }
        }
    ]
)
print("result:")
for i in agg_result:
    print(i)
