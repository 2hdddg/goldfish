from __future__ import absolute_import
import unittest

from ..testsetup import WorkUnitFake, build_unauthorized_context

from goldfish.core.exceptions import Unauthorized
from goldfish.core.entity import User
from goldfish.web.context import Context


def _user():
    return User(666, "Joey", "Ramone", "joey@blitzkrieg.com", "hash")


class TestContext(unittest.TestCase):

    def test_should_be_unauthorized_when_constructed_without_user(self):
        context = build_unauthorized_context()

        self.assertFalse(context.is_authorized)

    def test_should_be_authorized_when_constructed_with_user(self):
        context = Context(WorkUnitFake(), user=_user())

        self.assertTrue(context.is_authorized)

    def test_should_be_authorized_when_constructed_with_userid(self):
        context = Context(WorkUnitFake(), userid=666)

        self.assertTrue(context.is_authorized)

    def test_should_raise_when_accessing_user_on_unauthorized_context(self):
        context = build_unauthorized_context()

        with self.assertRaises(Unauthorized):
            context.user

    def test_should_raise_when_accessing_userid_on_unauthorized_context(self):
        context = build_unauthorized_context()

        with self.assertRaises(Unauthorized):
            context.userid

    def test_can_get_user_when_initialized_with_userid(self):
        def lookup(id):
            if not id == 666:
                raise "hell"
            return _user()

        workunit = WorkUnitFake()
        workunit.lookup.user_mock = lookup
        context = Context(workunit, userid=666)

        user = context.user

        self.assertTrue(user)
