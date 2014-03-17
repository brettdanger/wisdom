import requests
import json

#coursera_url = "https://www.coursera.org/maestro/api/topic/list?full=1"
#open cached copy
with open('_cache/coursera_list.json') as f:
    data = f.read()
    courses = json.loads(data)

print json.dumps(courses[0],sort_keys=True, indent=4, separators=(',', ': '))
#response = requests.get(coursera_url)
#for item in response.json():
catalog = []
for item in courses:
    catalog.append(item['short_name'])

print catalog[125]
print len(catalog)

for course in catalog[0:3]:
    response = requests.get("https://www.coursera.org/maestro/api/topic/information?topic-id=" + course)
    print json.dumps(response.json(), sort_keys=True, indent=4, separators=(',', ': '))
    break
