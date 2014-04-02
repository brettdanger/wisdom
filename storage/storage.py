from abc import ABCMeta, abstractmethod
import yaml


class StorageBase(object):
    __metaclass__ = ABCMeta

    @classmethod
    def get_config(cls, engine_name):
        config = yaml.load(open('config.yaml'))
        return config['storage_configs'].get(engine_name, None)

    @abstractmethod
    def store_courses(self):
        #abstract implemented in each provider
        pass

