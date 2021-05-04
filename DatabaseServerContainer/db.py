from flask_pymongo import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://<ID>:<password>@cluster0.zodbm.mongodb.net/<Collection>?retryWrites=true&w=majority")
db = client.get_database('<Collection>')
NBA = pymongo.collection.Collection(db, 'NBA')
Schedule = pymongo.collection.Collection(db, 'Schedule')
ELO = pymongo.collection.Collection(db, 'ELO')
Results = pymongo.collection.Collection(db, 'Results')
