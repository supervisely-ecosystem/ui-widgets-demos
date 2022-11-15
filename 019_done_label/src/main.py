import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, DoneLabel


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# initialize widgets we will use in UI
done_label = DoneLabel(
    text="Task has been successfully finished",
)

card = Card(
    title="Done Label",
    content=done_label,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
