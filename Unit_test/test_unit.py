from django.test import TestCase

from mock_site.models import Session


class BasicTest(TestCase):

    def setUp(self):
        self.session = Session()
        self.session.title = "mock interview website"
        self.session.start_time = "8:00 pm"
        self.session.end_time = "9:00 pm"
        self.session.note = "Start a interview session"
        self.session.save()

    def test_fields(self):
        session = Session()
        session.title = "mock interview website"
        session.start_time = "8:00 pm"
        session.end_time = "9:00 pm"
        session.save()

        record = Session.Object.get(pk=1)
        self.assertEqual(record, session)

    def test_note(self):
        self.assertEqual(self.session.note, "Start-a-interview-session")

    def test_start_time(self):
        self.assertEqual(self.session.start_time, "8:00-pm")

    def test_end_time(self):
        self.assertEqual(self.session.end_time, "9:00-pm")

    def test_completed(self):
        self.assertEqual(self.session.completed, False)
        self.session.completed()
        self.assertEqual(self.session.completed, True)
