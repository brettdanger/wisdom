from storage import StorageBase
import pymongo


class MongoDB(StorageBase):
    def __init__(self):
        self.db = pymongo.MongoClient().wisdom

    def store_courses(self, courses):

        self.db.courses.insert(courses)
