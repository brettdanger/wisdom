import json
from providers import *

import importlib

# provider_list = []
# coursera = coursera.Coursera()
# provider_list.append(coursera)

# for provider in provider_list:
#     print provider.get_courses()

provider_list = [{"module_name": "providers.coursera", "class_name": "Coursera", "display_name": "Coursera"}]

for provider in provider_list:
    mod = importlib.import_module(provider["module_name"])
    func = getattr(mod, provider['class_name'])()
    print getattr(func, "get_courses")()
