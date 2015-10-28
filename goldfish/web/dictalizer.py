from __future__ import absolute_import


def _dict_containing_namedtuples_to_dict(d):
    for k, v in d.iteritems():
        if isinstance(v, tuple):
            d[k] = namedtuple_to_dict(v)
        elif isinstance(v, dict):
            d[k] = _dict_containing_namedtuples_to_dict(v)
        elif isinstance(v, list):
            d[k] = _list_containing_named_tuples_to_list(v)
    return d


def _list_containing_named_tuples_to_list(l):
    for i, x in enumerate(l):
        if isinstance(x, tuple):
            l[i] = namedtuple_to_dict(x)
        elif isinstance(x, dict):
            l[i] = _dict_containing_namedtuples_to_dict(x)
        elif isinstance(x, list):
            l[i] = _list_containing_named_tuples_to_list(x)
    return l


def namedtuple_to_dict(nt):
    d = nt._asdict()
    return _dict_containing_namedtuples_to_dict(d)
