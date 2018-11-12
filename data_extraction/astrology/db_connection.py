import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client.list_database_names())


def connect(db, coll, create=False):

    db = client[db]
    collection = db[coll]
    # for x in collection.find():
    #     print(x)
    if create:
        if "horoscope" in db.list_collection_names():
            collection.drop()

    return collection


''' # collection.drop()
    # print(db.list_collection_names())
    #
    # # x = collection.delete_many({})
    # myquery = {"zodiac_sign": "aries"}
    # newvalues = {"$set": {"prediction": "something"}}

    # if not collection.update_one(myquery, newvalues):
    #
    #
    # # print "customers" after the update:
    # for x in collection.find():
    #     print(x)
    # for x in collection.find():
    #     print(x)
    # return collection
    # dict = {"zodiac_sign": "Aries", "prediction": "something" }
    #
    # x = collection.insert_one(dict)


# connect()
'''