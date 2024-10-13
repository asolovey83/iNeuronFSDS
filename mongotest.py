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

d = {'name': 'sudhanshu', 'emailid': 'sudhanshu@ineuron.ai', 'surname':'kumar'}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

# Figure out how to push/pull from/to GitHub
