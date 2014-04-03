import unittest
from storage.mongodb import MongoDB
import pymongo
import json
import yaml


class MongoTest(unittest.TestCase):
    def setUp(self):
        self.config = {
            "unit_test_collection": "testing"
        }
        #get the configuration
        configs = yaml.load(open('config.yaml'))['storage_configs']["MongoDB"]
        for item in configs:
            self.config[item] = configs[item]

        with open('test/stubs/collected_courses.json') as f:
            data = f.read()
            self.courses = json.loads(data)

        mongodb = pymongo.MongoClient()
        self.mongo = mongodb[self.config['db']]

        #drop the unit_test collection
        self.mongo[self.config['unit_test_collection']].drop()

    def test_input(self):
        mDB = MongoDB()
        #overide to testing collection
        mDB.set_collection(self.config["unit_test_collection"])
        mDB.store_courses(self.courses)

        #now check the results
        count = self.mongo[self.config["unit_test_collection"]].count()

        self.assertEquals(count, 10)

    #reinsert and make sure it still equals 10
    def test_updates(self):
        self.test_input()

    #make a change to a few records and make sure the data is changed
    def test_changes(self):
        self.courses[1]["short_description"] = "A new short description"
        self.courses[0]["providers_id"] = "unittests"

        #reenter the data
        self.test_input()

        #check for test_updates
        course = self.mongo[self.config["unit_test_collection"]].find({"id": "daf1d740782b94d750502fcb18a284fa"})
        self.assertEquals(course[0]["short_description"], "A new short description")

        #check for test_updates
        course = self.mongo[self.config["unit_test_collection"]].find({"id": "d114184968727a76272e32f6e4417e78"})
        self.assertEquals(course[0]["providers_id"], "unittests")

        #make sure we still have 10 records
        self.assertEquals(self.mongo[self.config["unit_test_collection"]].count(), 10)
