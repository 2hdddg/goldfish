from __future__ import absolute_import
import unittest

from .. import testsetup

from goldfish.core.workunit import WorkUnit


class UserCommandsIntegrationTests(unittest.TestCase):

    def test_creation_of_valid_user(self):
        workunit = WorkUnit()

        created = workunit.command.user.create(
            first_name="Me", last_name="Too", email="me@too.com", password="xyz")

        retrieved = workunit.lookup.user(created.id)
        self.assertGreater(created.id, 0)
        self.assertEqual(retrieved.id, created.id)
