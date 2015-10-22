import unittest

import testsetup

import goldfish.core.command as command
import goldfish.core.lookup as lookup
from goldfish.core.infrastructure import WorkUnit
from goldfish.core.entity import *
from goldfish.core.exceptions import *


class TestLookup(unittest.TestCase):

    def test_user_that_exists_should_return_user(self):
        workunit = WorkUnit()
        created = command.create_user(
            workunit, first_name="Me", last_name="Too", email="me@too.com", password="xyz")

        retrieved = lookup.user(workunit, created.id)
        self.assertGreater(created.id, 0)
        self.assertEqual(retrieved.id, created.id)

    def test_user_that_doesnt_exist_should_throw_NotFound(self):
        workunit = WorkUnit()
        raised = False
        try:
            lookup.user(workunit, -1)
        except NotFound:
            raised = True

        self.assertTrue(raised)
