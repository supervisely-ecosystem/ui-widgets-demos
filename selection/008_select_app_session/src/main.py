import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, SelectAppSession

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

team_id = sly.env.team_id()
# initialize widgets we will use in UI
select_app_session = SelectAppSession(team_id=team_id, tags=["deployed_nn"])

card = Card(
    title="Select App Session",
    content=Container(widgets=[select_app_session]),
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
