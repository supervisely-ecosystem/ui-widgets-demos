import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, ClassesTable

load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

project_id = int(os.environ["modal.state.slyProjectId"])

classes_table = ClassesTable(project_id=project_id)


card = Card(
    title="Classes Table",
    content=classes_table,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
