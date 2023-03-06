import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, SelectItem

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

dataset_id = sly.env.dataset_id()

# initialize widgets we will use in UI
select_item = SelectItem(dataset_id=dataset_id, compact=False)
card = Card(
    title="Select Item",
    content=Container(widgets=[select_item]),
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
