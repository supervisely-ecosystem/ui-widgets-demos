import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, SelectTeam

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

team_id = int(os.environ["modal.state.slyTeamId"])

# initialize widgets we will use in UI
select_team = SelectTeam(
    default_id=team_id,
)
card = Card(
    title="Select Team",
    content=Container(widgets=[select_team]),
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
