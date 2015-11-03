import string
import random

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


def random_string(num):
    options = string.ascii_lowercase
    choosen = [random.choice(options) for _ in range(num)]

    return ''.join(choosen)


def create_real_workunit():
    return WorkUnit()


def create_dummy_user(workunit):
    return workunit.command.user.create(
        first_name=random_string(20),
        last_name=random_string(20),
        email=random_string(10) + "@" + random_string(15) + ".com",
        password=random_string(20))


def create_dummy_calendar(workunit, owner=None):
    owner = create_dummy_user(workunit) if not owner else owner

    return workunit.command.calendar.create(
        owner=owner)
