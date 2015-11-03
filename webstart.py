from __future__ import absolute_import

from goldfish.web.application import application
from goldfish.core.infrastructure import WorkUnit

with WorkUnit() as workunit:
    user = workunit.command.user.create(
        first_name="Peter", last_name="Wilhelmsson", email="x", password="y")
    workunit.command.calendar.create(owner=user)

application.run(debug=True)
