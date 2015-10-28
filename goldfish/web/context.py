from __future__ import absolute_import

from ..core import lookup as lookup


class Context(object):
    def __init__(self, workunit, user=None, userid=None):
        self.workunit = workunit
        if user:
            self.is_authorized = True
            self._user = user
            self._userid = user.id
        elif userid:
            self.is_authorized = True
            self._userid = userid
            self._user = None
        else:
            self.is_authorized = False

    @property
    def user(self):
        if not self.is_authorized:
            raise "Unauthorized!"

        if not self._user:
            workunit = self.workunit
            self._user = lookup.user(
                workunit, self._userid)

        return self._user

    @property
    def userid(self):
        if not self.is_authorized:
            raise "Unauthorized!"

        return self._userid
