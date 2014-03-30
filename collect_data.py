import json
from providers import *

import importlib

# provider_list = []
# coursera = coursera.Coursera()
# provider_list.append(coursera)

# for provider in provider_list:
#     print provider.get_courses()

provider_list = ["Coursera"]

for provider in provider_list:
    print "Collecting Courses for provider: {}".format(provider)
    mod = importlib.import_module("providers." + provider.lower())
    func = getattr(mod, provider)()
    data = getattr(func, "get_courses")()

    print len(data)
