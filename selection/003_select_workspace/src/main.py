import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, SelectWorkspace

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

team_id = sly.env.team_id()
workspace_id = sly.env.workspace_id()

# initialize widgets we will use in UI
select_workspace = SelectWorkspace(
    default_id=workspace_id,
    team_id=team_id,
)
card = Card(
    title="Select Workspace",
    content=Container(widgets=[select_workspace]),
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
