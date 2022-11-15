import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Empty

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# initialize widgets we will use in UI
empty = Empty()

card = Card(
    title="Empty",
    content=empty,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
