import unittest

import testsetup

from goldfish.core.infrastructure import WorkUnit
from goldfish.core.entity import *
import goldfish.core.lookup as lookup
import goldfish.core.command as command


class CreateUserTests(unittest.TestCase):

    def test_creation_of_valid_user(self):
        workunit = WorkUnit()

        created = command.create_user(
            workunit, first_name="Me", last_name="Too", email="me@too.com", password="xyz")

        retrieved = lookup.user(workunit, created.id)
        self.assertGreater(created.id, 0)
        self.assertEqual(retrieved.id, created.id)


class TryLogonTests(unittest.TestCase):

    def test_can_logon_with_correct_credentials(self):
        workunit = WorkUnit()
        user = User(id=666, first_name="X", last_name="Y", email="the_user", hashedpassword="the_password")

        def fake_query(workunit, username):
            return user

        logged_on_user = command.try_logon(
            workunit, "the_user", "the_password", get_user_by_email=fake_query)

        self.assertEqual(logged_on_user.id, user.id)

    def test_can_NOT_logon_with_non_existant_username(self):
        workunit = WorkUnit()

        def fake_query(workunit, username):
            return None

        logged_on_user = command.try_logon(
            workunit, "the_user", "the_password", get_user_by_email=fake_query)

        self.assertEqual(logged_on_user, None)

    def test_can_NOT_logon_with_wrong_password(self):
        workunit = WorkUnit()
        user = User(id=666, first_name="X", last_name="Y", email="the_user", hashedpassword="the_password")

        def fake_query(workunit, username):
            return user

        logged_on_user = command.try_logon(
            workunit, "the_user", "wrong_password", get_user_by_email=fake_query)

        self.assertEqual(logged_on_user, None)
