from abc import ABCMeta, abstractmethod
from hashlib import md5


class ProviderBase(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_courses(self):
        #abstract implemented in each provider
        pass

    @classmethod
    def get_schema_map(cls):
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
            "short_description": None,
            "full_description": None,
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

        return course_schema

    @classmethod
    def get_valid_language(cls, language):
        language_map = {
            "en": "english",
            "english": "english",
            "ja": "japanese"
        }

        return language_map.get(language, None)

    @classmethod
    def create_id(cls, id_string):
        return md5(id_string.encode('utf-8')).hexdigest()
