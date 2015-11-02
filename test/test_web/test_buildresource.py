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

    def test_should_contain_user_representation_when_authorized(self):
        context = Context(FakeWorkUnit(), user=_user())

        resource = buildresource.application(context)

        self.assertEqual(resource.data.user_repr.data.first_name, "Joey")


class TestUserResource(unittest.TestCase):
    def test_should_set_properties(self):
        context = Context(FakeWorkUnit())
        user = _user()

        resource = buildresource.user(context, user)

        self.assertEqual(resource.data.first_name, user.first_name)
        self.assertEqual(resource.data.last_name, user.last_name)

    def test_should_have_link_to_calendars_when_authorized_and_user_is_self(self):
        user = _user()
        context = Context(FakeWorkUnit(), user=user)

        resource = buildresource.user(context, user)

        self.assertIn('calendars', resource.links)


class TestUserTemplateResource(unittest.TestCase):
    def test_should_have_create_action(self):
        context = Context(FakeWorkUnit())

        resource = buildresource.user_template(context)

        self.assertIn('create', resource.actions)

    def test_create_action_should_have_form(self):
        context = Context(FakeWorkUnit())

        resource = buildresource.user_template(context)

        action = resource.actions['create']
        self.assertGreater(len(action.form), 0)
