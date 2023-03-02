import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, SelectDataset

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

project_id = sly.env.project_id()
dataset_id = sly.env.dataset_id()

# initialize widgets we will use in UI
select_dataset = SelectDataset(
    default_id=dataset_id,
    project_id=project_id,
)
card = Card(
    title="Select Dataset",
    content=Container(widgets=[select_dataset]),
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
