from goldfish.web.application import application

import goldfish.core.command as command
from goldfish.core.infrastructure import WorkUnit

workunit = WorkUnit()
workunit.start()
user = command.create_user(workunit, first_name="Peter", last_name="Wilhelmsson", email="x", password="y")
command.create_calendar(workunit, owner=user)

application.run(debug=True)
