from pymongo import MongoClient

# from pymongo.errors import ConnectionFailure

myclient = MongoClient("mongodb://%s:%s@127.0.0.1" % ('admin', 'admin'))
print("connection successful", myclient)

# list down the databases
list_of_db = myclient.list_database_names()
print("databases available in mongodb", list_of_db)

# create new database in mongodb
mydb = myclient['test']
# print("Database created...", mydb)
collection = mydb['student']
# cursor = collection.find({"marks": {"$gt": 45}})
# print("The records greater than 45")
# # for record in cursor:
# #   print("records:%s" % record)
#
# cursor = collection.find({"marks": {"$lt": 45}})
# print("The records less than 45")
# for record in cursor:
#    print("records:%s" % record)

# search or display records in between

# ob = collection.find({"$and":[{"marks":{"$gt":40}}, {"marks":{"$lt":50}}]})
# print("And conditions records")
# for record in ob:
#    print("records", record)

# ob = collection.find({"$or":[{"marks":{"$gt":40}}, {"marks":{"$lt":50}}]})
# print("And conditions records")
# for record in ob:
#    print("records", record)

# sorting
mydoc = collection.find().sort("name")
# for x in mydoc:
#    print("sorting..", x)
# mydoc = collection.find().sort("name", -1)
# for x in mydoc:
#     print("sorting..", x)

# 1. connectivity to mongodb
# 2. create database in mongodb
# 3. create collections in mongodb
# 4. insert - insert_one, insert_many
# 5. find - find_one, find
# 6. find- display particular attributes records
# 7. find -- conditional formatting using and or gt, lt
# home work explore operator in pymongo
# 8. Sorting how to sort on fields of the documents

# update
# filter = {'roll_number': 104}
# newvalues = {"$set": {"marks": 35}}
# collection.update_one(filter, newvalues)
# all_documents = collection.find()
# print("updating records")
# for e_record in all_documents:
#     print("doc", e_record)

# upset
# collection.update_many(
#     {
#         "marks":{
#             "$gt":40
#         }
#     },
#     {
#         "$set":{
#             "passed":"True"
#         }
#     }
# )
# print("upset records.....")
# cursor = collection.find()
# for record in cursor:
#     print(record)

# collection.delete_one({'roll_number': 103})

# collection.delete_many({"roll_number": 103})

# print("after delete record:")
cursor = collection.find()
for record in cursor:
    print(record)
