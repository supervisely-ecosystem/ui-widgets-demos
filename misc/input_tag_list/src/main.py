import os
import supervisely as sly
from supervisely.app.widgets import Card, Container, ProjectSelector
from dotenv import load_dotenv


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()


team_id = sly.env.team_id()
workspace_id = sly.env.workspace_id()
project_id = sly.env.project_id()

project_selector = ProjectSelector(
    team_id=team_id, workspace_id=workspace_id, project_id=project_id
)


card = Card(
    title="Project Selector",
    content=project_selector,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
