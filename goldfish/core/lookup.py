
def user(workunit, id):
    return workunit.db.users[id]


def calendar(workunit, id):
    return workunit.db.calendars[id]
