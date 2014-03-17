from abc import ABCMeta, abstractmethod


class ProviderBase(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_courses(self):
        pass

#    @abstractmethod
#    def __get_schema_map(self):
#        pass
