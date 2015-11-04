from __future__ import absolute_import
import unittest

from ..testsetup import WorkUnitFake, build_unauthorized_context, build_authorized_context, build_dummy_user

from goldfish.core.exceptions import Unauthorized
from goldfish.web.context import Context


class TestContext(unittest.TestCase):

    def test_should_be_unauthorized_when_constructed_without_user(self):
        context = build_unauthorized_context()

        self.assertFalse(context.is_authorized)

    def test_should_be_authorized_when_constructed_with_user(self):
        context = build_authorized_context()

        self.assertTrue(context.is_authorized)

    def test_should_be_authorized_when_constructed_with_userid(self):
        context = build_authorized_context()

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
        inited_user = build_dummy_user()

        def lookup(id):
            if not id == inited_user.id:
                raise "hell"
            return inited_user

        workunit = WorkUnitFake()
        workunit.lookup.user_mock = lookup
        context = Context(workunit, userid=inited_user.id)

        user = context.user

        self.assertEquals(user.first_name, inited_user.first_name)
