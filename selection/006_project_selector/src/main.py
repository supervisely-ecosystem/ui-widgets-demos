import os
import supervisely as sly
from supervisely.app.widgets import Card, Container, ProjectSelector
from dotenv import load_dotenv


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()


team_id = int(os.environ["modal.state.slyTeamId"])
workspace_id = int(os.environ["modal.state.slyWorkspaceId"])
project_id = int(os.environ["modal.state.slyProjectId"])
project_selector = ProjectSelector(
    team_id=team_id, workspace_id=workspace_id, project_id=project_id
)


card = Card(
    title="Project Selector",
    content=project_selector,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
