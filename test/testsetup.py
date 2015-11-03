
from goldfish.core.workunit import WorkUnit
from goldfish.core.lookup import Lookup
from goldfish.core.query import Query, UserQuery


class LookupFake(Lookup):
    user_mock = None

    def __init__(self):
        pass

    def user(self, id):
        if hasattr(self.user_mock, '__call__'):
            return self.user_mock(id)
        return self.user_mock


class UserQueryFake(UserQuery):
    by_email_mock = None

    def __init__(self):
        pass

    def by_email(self, email):
        return self.by_email_mock


class QueryFake(Query):
    user_mock = None

    def __init__(self):
        self._user = UserQueryFake()

    @property
    def user(self):
        return self._user


class WorkUnitFake(WorkUnit):
    def __init__(self, fake_query=True, fake_lookup=True):
        db = {}
        self.db = db
        self._query = QueryFake() if fake_query else Query(db)
        self._lookup = LookupFake() if fake_lookup else Lookup(db)

    @property
    def query(self):
        return self._query

    @property
    def lookup(self):
        return self._lookup
