from __future__ import absolute_import
import unittest

from ..testsetup import build_authorized_context, build_unauthorized_context, build_dummy_user

from goldfish.core.exceptions import Unauthorized
import goldfish.web.buildactionresponse as build_action_response_for


class LoginLogoutTests(unittest.TestCase):

    def test_logged_in_should_have_a_logged_in_event_affecting_user(self):
        user = build_dummy_user()
        context = build_authorized_context(user=user)

        response = build_action_response_for.logged_in(context)

        events = response.events['logged_in']
        user_repr = filter(lambda x: x.refcls == 'User', events)[0]
        self.assertEqual(user_repr.data.first_name, user.first_name)

    def test_logged_in_should_have_a_logged_in_event_affecting_application(self):
        context = build_authorized_context()

        response = build_action_response_for.logged_in(context)

        events = response.events['logged_in']
        app_repr = filter(lambda x: x.refcls == 'Application', events)[0]

        self.assertTrue(app_repr)

    def test_logged_in_on_unauthorized_context_should_raise_Unauthorized(self):
        context = build_unauthorized_context()

        with self.assertRaises(Unauthorized):
            build_action_response_for.logged_in(context)

    def test_logged_out_should_have_a_logged_out_event_affecting_application(self):
        context = build_unauthorized_context()

        response = build_action_response_for.logged_out(context)

        events = response.events['logged_out']
        app_repr = filter(lambda x: x.refcls == 'Application', events)[0]

        self.assertTrue(app_repr)
