import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Checkbox


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# initialize widgets we will use in UI
checkbox = Checkbox(
    content="Enable",
    checked=False,
)

card = Card(
    title="Checkbox",
    content=checkbox,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
