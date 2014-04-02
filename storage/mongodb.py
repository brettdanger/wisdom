from storage import StorageBase
import pymongo
from pymongo import ASCENDING


class MongoDB(StorageBase):
    #do not override here, place this in the YAML configuration config.yaml
    config = {
        "server": "localhost",
        "db": "wisdom",
        "collection": "courses"}

    def __init__(self):
        config = self.get_config(self.__class__.__name__)  # call the super init method to get config

        if config is not None:
            for item in config:
                self.config[item] = config[item]

        connection = pymongo.MongoClient(self.config["server"])
        self.db = connection[self.config["db"]]

    def store_courses(self, courses):
        #we can't bulk upsert so lets loop and upsert
        for course in courses:
            self.db[self.collection].update({"id": course["id"]}, course, upsert=True)

        self.__set_indicies()

    #this method is to override the collection for testing
    def set_collection(self, collection):
        self.collection = collection

    #setup any indexes we might want
    def __set_indicies(self):
        self.db[self.collection].ensure_index("id", unique=True)
        self.db[self.collection].ensure_index([("course_name", ASCENDING), ("provider", ASCENDING)], unique=True)
