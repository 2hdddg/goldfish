import unittest

import testsetup

from goldfish.core.infrastructure import WorkUnit
from goldfish.core.lookups import Lookups
import goldfish.core.command as command


class CreateUserTests(unittest.TestCase):

    def test_creation_of_valid_user(self):
        workunit = WorkUnit()
        lookups = Lookups(workunit)

        created = command.create_user(
            workunit, first_name="Me", last_name="Too", email="me@too.com", password="xyz")

        retrieved = lookups.get_user(created.id)
        self.assertGreater(created.id, 0)
        self.assertEqual(retrieved.id, created.id)
