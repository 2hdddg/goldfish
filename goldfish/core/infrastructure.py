from __future__ import absolute_import


from . import db


class WorkUnit(object):
    def __init__(self):
        self._state = 'initial'
        self.db = db

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, type, value, traceback):
        if value:
            self.cancel()
            return False

        self.end()
        return True

    def start(self):
        if self._state == 'initial':
            self._state = 'started'
        else:
            raise "can not start from state:" + self._state

    def start_if_not_started(self):
        if self._state == 'started':
            return

        self.start()

    def end(self):
        if self._state == 'started':
            self._state = 'ended'
        else:
            raise "can not end from state:" + self._state

    def cancel(self):
        if self._state == 'started':
            self._state = 'cancelled'
        else:
            raise "can not cancel from state:" + self._state
