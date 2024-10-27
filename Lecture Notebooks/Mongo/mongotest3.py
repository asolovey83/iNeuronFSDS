import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://soloveyandriy:tAAHDE5wfixW07ew@cluster0.qee4t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.server_info

print(db)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

data = [
    {
        "item": "canvas",
        "qty": 100,
        "size": {"h": 28, "w": 35.5, "uom": "cm"},
        "status": "A"
    },
    {
        "item": "journal",
        "qty": 25,
        "size": {"h": 14, "w": 21, "uom": "cm"},
        "status": "B"
    },
    {
        "item": "sketchpad",
        "qty": 50,
        "size": {"h": 20, "w": 25, "uom": "cm"},
        "status": "A"
    },
    {
        "item": "watercolor set",
        "qty": 15,
        "size": {"h": 5, "w": 30, "uom": "cm"},
        "status": "C"
    },
    {
        "item": "easel",
        "qty": 10,
        "size": {"h": 150, "w": 60, "uom": "cm"},
        "status": "B"
    },
    {
        "item": "paintbrush",
        "qty": 200,
        "size": {"h": 1, "w": 20, "uom": "cm"},
        "status": "A"
    },
    {
        "item": "acrylic paint",
        "qty": 30,
        "size": {"h": 10, "w": 10, "uom": "cm"},
        "status": "C"
    },
    {
        "item": "charcoal sticks",
        "qty": 40,
        "size": {"h": 2, "w": 15, "uom": "cm"},
        "status": "B"
    },
    {
        "item": "oil paint",
        "qty": 20,
        "size": {"h": 8, "w": 15, "uom": "cm"},
        "status": "A"
    },
    {
        "item": "portfolio",
        "qty": 35,
        "size": {"h": 40, "w": 30, "uom": "cm"},
        "status": "B"
    }
]

database = client['inventory']
collection = database['table']

#collection.insert_many(data)

#record = collection.find()
#record1 = collection.find({"status":"A"})
#record2 = collection.find({"status":{'$in':['A', 'C']}})
#record3 = collection.find({"status":{'$gt':'A'}})
#record4 = collection.find({"qty":{'$gte':30}})
#record5 = collection.find({"item": "paintbrush", "qty":{'$gte':30}})
#record6 = collection.find({"$or":[{"item": "paintbrush"}, {"qty":{'$gte':30}}]})
#record7 = collection.find({"$or":[{"item": "paintbrush"}, {"qty":{'$gte':30}}]})

'''for i in record7:
    print(i)'''

#collection.update_one({"item": "paintbrush"}, {"$set":{"item": "motorcycle"}})

#data = collection.find()

'''for i in data:
    print(i)'''

#collection.delete_one({"item": "motorcycle"})

data = collection.find_one({"item": "motorcycle"})

print(data)

# 2:00