import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Container, Text

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

layout = Container(widgets=[Text(text="Text in the container")])
app = sly.Application(layout=layout)
