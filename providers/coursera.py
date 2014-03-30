from provider import ProviderBase
import requests
import json
from datetime import date


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
            try:
                #get required items
                course['course_name'] = item['name']
                course['providers_id'] = item["short_name"]
                course['provider'] = "coursera"
                course['providers_id'] = item["short_name"]
                course['language'] = self.get_valid_language(item['language'])
                course['instructor'] = item['instructor']

                #get the data we need from the full course detail
                more_details = self.__get_course_detail(course["providers_id"])

                course['full_description'] = more_details.get("about_the_course", "not found")
            except Exception("KeyError"):
                #we don't have all required fields, skip for now
                #log it
                continue

            #get optional fields
            course['short_description'] = item.get('short_description', None)
            course['categories'] = item.get('categories', [])
            catalog.append(item['short_name'])

            #get the session data
            for c in item.get('courses'):
                session = {}
                session['duration'] = c.get('duration_string', None)
                session['provider_session_id'] = c.get('id', None)
                #get Start Date
                if all(name in c for name in ['start_year', 'start_month', 'start_day']):
                    session['start_date'] = date(c['start_year'], c['start_month'], c['start_day']).strftime('%Y%m%d')
                else:
                    continue
                course['sessions'].append(session)
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
