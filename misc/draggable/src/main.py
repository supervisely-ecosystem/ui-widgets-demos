import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Draggable, Text

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

text = Text("Drag me!", status="text", font_size=32)
draggable = Draggable(content=text)

card = Card(title="Draggable", content=None)
app = sly.Application(layout=card)
