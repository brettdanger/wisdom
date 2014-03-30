import unittest
from mock import Mock, patch
import sys
from providers.coursera import Coursera
import json

#setup mock object for requests
sys.modules['requests'] = Mock()


class ListResponse:
    def json(self):
        with open('test/stubs/coursera_list.json') as f:
            data = f.read()
            courses = json.loads(data)
        return courses


class CourseResponse:
    def json(self):
        with open('test/stubs/coursera_course.json') as f:
            data = f.read()
            course = json.loads(data)
        return course


def get(*args):
    if args[0] == "https://www.coursera.org/maestro/api/topic/list?full=1":
        print "running"
        return ListResponse()
    elif args[0] == "https://www.coursera.org/maestro/api/topic/information?topic-id=ml":
        print "running2"
        return CourseResponse()


class CourseraTest(unittest.TestCase):
    def setUp(self):
        pass

    @patch('requests.get')
    def test_input(self, MockClass):
        MockClass.side_effect = get

        coursera = Coursera()
        courses = getattr(coursera, "get_courses")()
        self.assertTrue(MockClass.called)
        self.assertEquals(len(courses), 2)


