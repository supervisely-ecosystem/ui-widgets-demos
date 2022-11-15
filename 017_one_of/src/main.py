import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Select, OneOf


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# initialize widgets we will use in UI
checkbox = OneOf(conditional_widget=Select())

card = Card(
    title="Checkbox",
    content=checkbox,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
