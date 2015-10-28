from __future__ import absolute_import

from collections import namedtuple

Action = namedtuple('Action', [
    'ref',
    'form'
])

FormField = namedtuple('FormField', [
    'name',
    'value',
    'type',
    'required'
])

ActionResponse = namedtuple('ActionResponse', [
    'events',
    'embedded'
])
