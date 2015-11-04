from __future__ import absolute_import
import unittest

from ..testsetup import create_real_workunit, create_dummy_user


class UserCommandsIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.workunit = create_real_workunit()

    def test_creation_of_valid_user(self):
        created = self.workunit.command.user.create(
            first_name="Me", last_name="Too", email="me@too.com", password="xyz")

        retrieved = self.workunit.lookup.user(created.id)
        self.assertGreater(created.id, 0)
        self.assertEqual(retrieved.id, created.id)

    def test_creation_of_valid_calendar(self):
        owner = create_dummy_user(self.workunit)
        created = self.workunit.command.calendar.create(
            owner=owner.id)

        retrieved = self.workunit.lookup.calendar(created.id)
        self.assertGreater(created.id, 0)
        self.assertEqual(retrieved.id, created.id)
