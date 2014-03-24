from abc import ABCMeta, abstractmethod


class ProviderBase(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_courses(self):
        pass

    @staticmethod
    def get_schema_map():
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

        return course_schema

    @staticmethod
    def get_valid_language(language):
        language_map = {
            "en": "english",
            "english": "english"
        }

        return language_map.get(language, None)
