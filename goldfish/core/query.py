
def get_user_by_email(workunit, email):
    for id, user in workunit.db.users.iteritems():
        if user.email == email:
            return user

    return None
