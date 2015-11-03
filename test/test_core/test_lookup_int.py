from __future__ import absolute_import
import unittest

from ..testsetup import create_real_workunit, create_dummy_user, create_dummy_calendar

from goldfish.core.entity import *
from goldfish.core.exceptions import *


class LookupIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.workunit = create_real_workunit()

    def test_user_that_exists_should_return_user(self):
        created = create_dummy_user(self.workunit)

        retrieved = self.workunit.lookup.user(created.id)

        self.assertGreater(created.id, 0)
        self.assertEqual(retrieved.id, created.id)

    def test_user_that_doesnt_exist_should_throw_NotFound(self):
        raised = False
        try:
            self.workunit.lookup.user(-1)
        except NotFound:
            raised = True

        self.assertTrue(raised)

    def test_calendar_that_exists_should_return_calendar(self):
        created = create_dummy_calendar(self.workunit)

        retrieved = self.workunit.lookup.calendar(created.id)

        self.assertGreater(created.id, 0)
        self.assertEqual(retrieved.id, created.id)

    def test_calendar_that_doesnt_exist_should_throw_NotFound(self):
        raised = False
        try:
            self.workunit.lookup.calendar(-1)
        except NotFound:
            raised = True

        self.assertTrue(raised)
