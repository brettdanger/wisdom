from providers import *
import importlib
import yaml


#get the configuration
config = yaml.load(open('config.yaml'))

provider_list = config["providers"]
storage_list = config["storage_engines"]

for provider in provider_list:
    print "Collecting Courses for provider: {}".format(provider)
    mod = importlib.import_module("providers." + provider.lower())
    func = getattr(mod, provider)()
    data = getattr(func, "get_courses")()

    #loop through Storage Lists
    for store in storage_list:
        print "Saving Courses into Engine: {}".format(store)
        mod = importlib.import_module("storage." + store.lower())
        func = getattr(mod, store)()
        data = getattr(func, "store_courses")(data)
