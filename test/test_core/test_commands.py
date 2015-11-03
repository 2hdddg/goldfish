from __future__ import absolute_import
import unittest

from ..testsetup import WorkUnitFake

from goldfish.core.infrastructure import WorkUnit
from goldfish.core.entity import User


class UserCommandsIntegrationTests(unittest.TestCase):

    def test_creation_of_valid_user(self):
        workunit = WorkUnit()

        created = workunit.command.user.create(
            first_name="Me", last_name="Too", email="me@too.com", password="xyz")

        retrieved = workunit.lookup.user(created.id)
        self.assertGreater(created.id, 0)
        self.assertEqual(retrieved.id, created.id)


class UserCommandsTests(unittest.TestCase):
    def setUp(self):
        self.workunit = WorkUnitFake()

    def test_can_logon_with_correct_credentials(self):
        user = User(
            id=666, first_name="X", last_name="Y", email="the_user", hashedpassword="the_password")
        self.workunit.query.user.by_email_mock = user

        logged_on_user = self.workunit.command.user.try_logon("the_user", "the_password")

        self.assertEqual(logged_on_user.id, user.id)

    def test_can_NOT_logon_with_non_existant_username(self):
        self.workunit.query.user.by_email_mock = None

        logged_on_user = self.workunit.command.user.try_logon("the_user", "the_password")

        self.assertEqual(logged_on_user, None)

    def test_can_NOT_logon_with_wrong_password(self):
        user = User(id=666, first_name="X", last_name="Y", email="the_user", hashedpassword="the_password")
        self.workunit.query.user.by_email_mock = user

        logged_on_user = self.workunit.command.user.try_logon(
            "the_user", "wrong_password")

        self.assertEqual(logged_on_user, None)
