import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, ObjectClassesList

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

project_id = int(os.environ["modal.state.slyProjectId"])

# initialize widgets we will use in UI
project_meta = sly.ProjectMeta.from_json(api.project.get_meta(project_id))
obj_classes_list = ObjectClassesList(
    object_classes=project_meta.obj_classes, selectable=True
)
card = Card(
    title="Object Classes List",
    content=Container(widgets=[obj_classes_list]),
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
