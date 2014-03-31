from providers import *
import importlib

provider_list = ["Coursera"]
storage_list = ["MongoDB"]

for provider in provider_list:
    print "Collecting Courses for provider: {}".format(provider)
    mod = importlib.import_module("providers." + provider.lower())
    func = getattr(mod, provider)()
    data = getattr(func, "get_courses")()

    print len(data)

    #loop through Storage Lists
    for store in storage_list:
        print "Saving Courses into Engine: {}".format(store)
    mod = importlib.import_module("storage." + store.lower())
    func = getattr(mod, store)()
    data = getattr(func, "store_courses")(data)
