import unittest

import testsetup

from goldfish.core.entity import User
from goldfish.web.context import Context
import goldfish.web.buildresource as buildresource


class FakeWorkUnit(object):
    pass


def _user():
    return User(666, "Joey", "Ramone", "joey@blitzkrieg.com", "hash")


class FakeCurrent(object):
    ref = ''
    data = ''


class TestApplicationResource(unittest.TestCase):
    def test_should_have_logout_action_when_authorized(self):
        context = Context(FakeWorkUnit(), user=_user())

        resource = buildresource.application(context)

        self.assertIn('logout', resource.actions)

    def test_should_have_login_action_when_NOT_authorized(self):
        context = Context(FakeWorkUnit())

        resource = buildresource.application(context)

        self.assertIn('login', resource.actions)

    def test_when_a_current_page_is_set_it_should_be_linked_and_embedded(self):
        context = Context(FakeWorkUnit())
        current = FakeCurrent()
        current.ref = 'the link'
        current.data = 'just to know'

        resource = buildresource.application(context, current)

        current_link = resource.links['current']
        self.assertEqual(current_link, 'the link')
        self.assertEqual(resource.embedded[current_link].data, 'just to know')