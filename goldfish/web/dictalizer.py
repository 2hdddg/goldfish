from __future__ import absolute_import


def _dict_containing_namedtuples_to_dict(d):
    for k, v in d.iteritems():
        if isinstance(v, tuple):
            if hasattr(v, '_asdict'):
                d[k] = namedtuple_to_dict(v)
            else:
                d[k] = _list_containing_named_tuples_to_list(v)
        elif isinstance(v, dict):
            d[k] = _dict_containing_namedtuples_to_dict(v)
        elif isinstance(v, list):
            d[k] = _list_containing_named_tuples_to_list(v)
    return d


def _list_containing_named_tuples_to_list(l):
    converted = []
    for x in l:
        if isinstance(x, tuple):
            if hasattr(x, '_asdict'):
                converted.append(namedtuple_to_dict(x))
        elif isinstance(x, dict):
            converted.append(_dict_containing_namedtuples_to_dict(x))
        elif isinstance(x, list):
            converted.append(_list_containing_named_tuples_to_list(x))
    return converted


def namedtuple_to_dict(nt):
    d = nt._asdict()
    return _dict_containing_namedtuples_to_dict(d)
