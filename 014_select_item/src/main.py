import os
from supervisely.app.widgets import Card, Container, SelectItem

import supervisely as sly
from dotenv import load_dotenv

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

dataset_id = int(os.environ["modal.state.slyDatasetId"])

# initialize widgets we will use in UI
select_item = SelectItem(
    dataset_id=dataset_id,
)
card = Card(
    title="Select Item",
    content=Container(widgets=[select_item]),
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
