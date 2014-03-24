from provider import ProviderBase
import requests
import json


class Coursera(ProviderBase):
    def __init__(self):
        self.course_data = []

    def get_courses(self):
        #coursera_url = "https://www.coursera.org/maestro/api/topic/list?full=1"
        #open cached copy
        #check cached copy age get new copy if it is too old
        with open('_cache/coursera_list.json') as f:
            data = f.read()
            courses = json.loads(data)

        #response = requests.get(coursera_url)
        #for item in response.json():
        #print json.dumps(courses[0], sort_keys=True, indent=4, separators=(',', ': '))
        catalog = []
        for item in courses:
            course = self.get_schema_map()
            print json.dumps(item, sort_keys=True, indent=4, separators=(',', ': '))
            break
            try:
                #get required items
                course['course_name'] = item['name']
                course['providers_id'] = item["short_name"]
                course['provider'] = "coursera"
                course['providers_id'] = item["short_name"]
                course['language'] = self.get_valid_language(item['language'])

                #get the data we need from the full course detail
                more_details = self.__get_course_detail(course["providers_id"])

                course['description'] = more_details.get("about_the_course", "not found")
            except Exception("KeyError"):
                #we don't have all required fields, skip for now
                #log it
                continue

            #get optional field
            course['short_description'] = item.get('short_description', None)
            catalog.append(item['short_name'])

            self.course_data.append(course)
            #quit at one entry
            break
            
        return self.course_data

    def __get_course_detail(self, id):
        response = requests.get("https://www.coursera.org/maestro/api/topic/information?topic-id=" + id)
        #print json.dumps(response.json(), sort_keys=True, indent=4, separators=(',', ': '))
        return response.json()

'''
    def __get_session_detail(self, id):
        response = requests.get("https://www.coursera.org/maestro/api/course/information?course_id=" + id)


course_schema = {
            "course_name": None,
            "provider": None,
            "language": None,
            "instructor": None,
            "providers_id": None,
            "media": {
                "photo_url": None,
                "icon_url": None,
                "video_url": None,
                "video_type": None,
                "video_id": None
            },
            "prerequisites": [],
            "short_description": None,
            "full_description": None,
            "suggested_reading": [],
            "course_url": None,
            "institution": {
                "name": None,
                "description": None,
                "id": None,
                "website": None,
                "logo_url": None,
                "city": None,
                "state": None,
                "country": None
            },
            "sessions": [],
            "workload": None,
            "categories": [],
            "tags": []
        }
'''
