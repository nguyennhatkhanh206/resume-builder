import pymongo

# TODO: host and database name must be defined in setting file like db.config 
HOST = "mongodb://localhost:27017/"
DEFAULT_DATABASE_SCHEMA = "model-builder-dev"


class AbstractDbService:
    def __init__(self):
        connect()

def connect():
    mongo_client = pymongo.MongoClient("%s" % HOST)
    mongo_client.get_database(DEFAULT_DATABASE_SCHEMA)
    db_schema = mongo_client[DEFAULT_DATABASE_SCHEMA]
    resume_collection = db_schema[""]

def insert():
    print("insert")

def delete():
    print("delete")

def findOne():
    print("findOne")

def findAll():
    print("find all")
