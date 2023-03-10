import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, CopyToClipboard, Button


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

copytoclipboard = CopyToClipboard(content="fasdefsdfzasde")

card = Card(content=Container([copytoclipboard]))

layout = Container(widgets=[card], direction="vertical")
app = sly.Application(layout=layout)
