import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, SelectProject

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

workspace_id = int(os.environ["modal.state.slyWorkspaceId"])
project_id = int(os.environ["modal.state.slyProjectId"])

# initialize widgets we will use in UI
select_project = SelectProject(
    default_id=project_id,
    workspace_id=workspace_id,
)
card = Card(
    title="Select Project",
    content=Container(widgets=[select_project]),
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
