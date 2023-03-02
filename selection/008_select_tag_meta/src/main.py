import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, SelectTagMeta

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

project_id = int(os.environ["modal.state.slyProjectId"])

# initialize widgets we will use in UI
select_tag_meta = SelectTagMeta(default="cat", project_id=project_id)

card = Card(
    title="Select TagMeta",
    content=select_tag_meta,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
