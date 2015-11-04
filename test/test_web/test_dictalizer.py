from __future__ import absolute_import

from collections import namedtuple
import unittest

from .. import testsetup

from goldfish.web.dictalizer import namedtuple_to_dict


class DictalizerTests(unittest.TestCase):
    def test_can_convert_flat_namedtuple_to_dict(self):
        t = namedtuple('X', ['prop_1', 'prop_2'])(prop_1=1, prop_2=2)

        d = namedtuple_to_dict(t)

        self.assertDictEqual(d, {
                "prop_1": 1,
                "prop_2": 2
            })

    def test_can_convert_namedtuple_containing_namedtuple_to_dict(self):
        n = namedtuple('X', ['prop_1', 'prop_2'])(prop_1=1, prop_2=2)
        t = namedtuple('Y', ['nested'])(nested=n)

        d = namedtuple_to_dict(t)

        self.assertDictEqual(d, {
            "nested": {
                "prop_1": 1,
                "prop_2": 2
            }})

    def test_can_convert_namedtuple_containing_dict_with_namedtuple_to_dict(self):
        n = namedtuple('X', ['prop_1', 'prop_2'])(prop_1=1, prop_2=2)
        d = {"n": n}
        t = namedtuple('Y', ['nested'])(nested=d)

        d = namedtuple_to_dict(t)

        self.assertDictEqual(d, {
            "nested": {
                "n": {
                    "prop_1": 1,
                    "prop_2": 2
                }
            }})

    def test_can_convert_namedtuple_containing_list_with_namedtuple_to_dict(self):
        n = namedtuple('X', ['prop_1', 'prop_2'])(prop_1=1, prop_2=2)
        l = [n]
        t = namedtuple('Y', ['nested'])(nested=l)

        d = namedtuple_to_dict(t)

        self.assertDictEqual(d, {
            "nested": [
                {
                    "prop_1": 1,
                    "prop_2": 2
                }
            ]})

    def test_can_convert_namedtuple_containing_tuple_with_namedtuple_to_dict(self):
        n = namedtuple('X', ['prop_1', 'prop_2'])(prop_1=1, prop_2=2)
        l = (n,)
        t = namedtuple('Y', ['nested'])(nested=l)

        d = namedtuple_to_dict(t)

        self.assertDictEqual(d, {
            "nested": [
                {
                    "prop_1": 1,
                    "prop_2": 2
                }
            ]})
