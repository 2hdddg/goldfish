from __future__ import absolute_import
import unittest

from ..testsetup import build_dummy_user, build_authorized_context, build_unauthorized_context

import goldfish.web.buildresource as buildresource


class FakeCurrent(object):
    ref = ''
    data = ''


class TestApplicationResource(unittest.TestCase):
    def test_should_have_logout_action_when_authorized(self):
        context = build_authorized_context()

        resource = buildresource.application(context)

        self.assertIn('logout', resource.actions)

    def test_should_have_login_action_when_NOT_authorized(self):
        context = build_unauthorized_context()

        resource = buildresource.application(context)

        self.assertIn('login', resource.actions)

    def test_when_a_current_page_is_set_it_should_be_linked_and_embedded(self):
        context = build_unauthorized_context()
        current = FakeCurrent()
        current.ref = 'the link'
        current.data = 'just to know'

        resource = buildresource.application(context, current)

        current_link = resource.links['current']
        self.assertEqual(current_link, 'the link')
        self.assertEqual(resource.embedded[current_link].data, 'just to know')

    def test_should_contain_user_representation_when_authorized(self):
        user = build_dummy_user()
        context = build_authorized_context(user=user)

        resource = buildresource.application(context)

        self.assertEqual(resource.data.user_repr.data.first_name, user.first_name)


class TestUserResource(unittest.TestCase):
    def test_should_set_properties(self):
        context = build_unauthorized_context()
        user = build_dummy_user()

        resource = buildresource.user(context, user)

        self.assertEqual(resource.data.first_name, user.first_name)
        self.assertEqual(resource.data.last_name, user.last_name)

    def test_should_have_link_to_calendars_when_authorized_and_user_is_self(self):
        user = build_dummy_user()
        context = build_authorized_context(user=user)

        resource = buildresource.user(context, user)

        self.assertIn('calendars', resource.links)


class TestUserTemplateResource(unittest.TestCase):
    def test_should_have_create_action(self):
        context = build_unauthorized_context()

        resource = buildresource.user_template(context)

        self.assertIn('create', resource.actions)

    def test_create_action_should_have_form(self):
        context = build_unauthorized_context()

        resource = buildresource.user_template(context)

        action = resource.actions['create']
        self.assertGreater(len(action.form), 0)
