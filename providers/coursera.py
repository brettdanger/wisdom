from provider import ProviderBase
import requests
import json


class Coursera(ProviderBase):
    def __init__(self):
        self.course_data = []

    def get_courses(self):
        #coursera_url = "https://www.coursera.org/maestro/api/topic/list?full=1"
        #open cached copy
        with open('_cache/coursera_list.json') as f:
            data = f.read()
            courses = json.loads(data)

        #response = requests.get(coursera_url)
        #for item in response.json():
        catalog = []
        for item in courses:
            catalog.append(item['short_name'])


        for course in catalog[0:3]:
            response = requests.get("https://www.coursera.org/maestro/api/topic/information?topic-id=" + course)
            self.course_data.append(response.json())
            #print json.dumps(response.json(), sort_keys=True, indent=4, separators=(',', ': '))

        return self.course_data
