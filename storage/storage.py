from abc import ABCMeta, abstractmethod


class StorageBase(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def store_courses(self):
        #abstract implemented in each provider
        pass

