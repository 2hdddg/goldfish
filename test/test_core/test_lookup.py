from __future__ import absolute_import
import unittest

from .. import testsetup

from goldfish.core.workunit import WorkUnit
from goldfish.core.entity import *
from goldfish.core.exceptions import *


class LookupIntegrationTests(unittest.TestCase):

    def test_user_that_exists_should_return_user(self):
        workunit = WorkUnit()
        created = workunit.command.user.create(
            first_name="Me", last_name="Too", email="me@too.com", password="xyz")

        retrieved = workunit.lookup.user(created.id)

        self.assertGreater(created.id, 0)
        self.assertEqual(retrieved.id, created.id)

    def test_user_that_doesnt_exist_should_throw_NotFound(self):
        workunit = WorkUnit()
        raised = False
        try:
            workunit.lookup.user(-1)
        except NotFound:
            raised = True

        self.assertTrue(raised)
