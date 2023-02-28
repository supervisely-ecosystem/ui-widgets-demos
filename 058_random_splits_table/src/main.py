import os
import supervisely as sly
from supervisely.app.widgets import Card, Container, RandomSplitsTable
from dotenv import load_dotenv


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()


# team_id = int(os.environ["modal.state.slyTeamId"])
# workspace_id = int(os.environ["modal.state.slyWorkspaceId"])
# project_id = int(os.environ["modal.state.slyProjectId"])

random_splits_table = RandomSplitsTable(items_count=500, start_train_percent=40)


card = Card(
    title="Random Splits Table",
    content=random_splits_table,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
