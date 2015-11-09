from __future__ import absolute_import

from collections import namedtuple

""" A representation of a resource, the information
    necessary to represent a resource for a user but
    still not the complete resource.
"""
Representation = namedtuple('Representation', [
    'ref',
    'cls',
    'refcls',
    'data'
])

UserReprData = namedtuple('UserReprData', [
    'first_name',
    'last_name'
])

CalendarReprData = namedtuple('CalendarReprData', [
    'name'
])
