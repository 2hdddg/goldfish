import goldfish.core.lookup as lookup


class Context(object):
    def __init__(self, workunit, user=None, userid=None):
        self.workunit = workunit
        if user:
            self.is_authorized = True
            self._user = user
        elif userid:
            self.is_authorized = True
            self._userid = userid
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
