from __future__ import absolute_import

from collections import namedtuple

User = namedtuple(
    'User', ['id', 'first_name', 'last_name', 'email', 'hashedpassword'])

Calendar = namedtuple(
    'Calendar', ['id', 'owner', 'name'])

Happening = namedtuple(
    'Happening', ['id', 'calendar', 'tags', 'date', 'time'])

Rule = namedtuple(
    'Rule', ['id', 'calendar', 'user'])

Action = namedtuple(
    'Action', ['id', 'rule'])
