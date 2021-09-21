from pymongo import MongoClient

myclient = MongoClient("mongodb://%s:%s@127.0.0.1" % ('admin', 'admin'))
mydb = myclient['test']
# print("open database", mydb)

mycollection = mydb['employee']


# print("create collection", mycollection)

# record = {
#     "_id": 2,
#     "emp_name": "james",
#     "sal": 43500,
#     "dept": "arts",
#     "phn_no": 367894
# }
#
# val = mycollection.insert_one(record)
# print("record",val )

# print("list of collections in test db", mydb.list_collection_names())


def insert_records():
    id_no = int(input("enter id:"))
    name = input("enter name:")
    salary = int(input("enter sal:"))
    depart = input("enter dept:")
    ph_no = int(input("enter phn_no:"))

    record = {
        "_id": id_no,
        "emp_name": name,
        "sal": salary,
        "dept": depart,
        "phn_no": ph_no
    }

    mycollection.insert_one(record)


def update_records():
    pass


def show_records():
    records = mycollection.find()
    print("records in employee are")
    for doc in records:
        print("doc", doc)


def find_records():
    print("enter which field to be displayed in records")
    entered = int(input('1.id\n'
                        '2.emp_name\n'
                        '3.sal\n'
                        '4.dept\n'
                        '5.phn_no\n'))
    if entered == 1:
        for x in mycollection.find({}, {"_id": 1, "emp_name": 1}):
            print("Only fields with 1", x)


def ask_choice():
    while True:
        print("enter your choice")
        picked = int(input('1.create records(insert)\n'
                           '2.find record by using specific field\n'
                           '3.display all records\n'
                           '4.update records\n'
                           '5.exit\n'
                           ))
        if picked == 1:
            insert_records()
        elif picked == 2:
            find_records()
        elif picked == 3:
            show_records()
        elif picked == 4:
            update_records()
        elif picked == 5:
            return


ask_choice()
