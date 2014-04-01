import unittest
from mock import Mock, patch
from providers.coursera import Coursera
import json


#setup our mock responses
class ListResponse:
    def json(self):
        with open('test/stubs/coursera_courses.json') as f:
            data = f.read()
            courses = json.loads(data)
        return courses


class CourseResponse:
    def json(self):
        with open('test/stubs/coursera_course.json') as f:
            data = f.read()
            course = json.loads(data)
        return course


class BadCourseResponse:
    def json(self):
        with open('test/stubs/coursera_course2.json') as f:
            data = f.read()
            course = json.loads(data)
        return course


#define urls to response object
def get(*args):
    if args[0] == "https://www.coursera.org/maestro/api/topic/list?full=1":
        return ListResponse()
    elif args[0] == "https://www.coursera.org/maestro/api/topic/information?topic-id=ml":
        return CourseResponse()
    elif args[0] == "https://www.coursera.org/maestro/api/topic/information?topic-id=rt":
        return BadCourseResponse()
    else:
        print "nothing"


#test coursera provider
class CourseraTest(unittest.TestCase):
    def setUp(self):
        pass

    @patch('requests.get')
    def test_input(self, MockClass):
        MockClass.side_effect = get

        coursera = Coursera()
        courses = getattr(coursera, "get_courses")()
        self.assertTrue(MockClass.called)
        self.assertEquals(len(courses), 3)
        self.assertEquals(courses[0].get("course_name"), "Machine Learning")
        self.assertEquals(courses[2].get("language"), "japanese")


