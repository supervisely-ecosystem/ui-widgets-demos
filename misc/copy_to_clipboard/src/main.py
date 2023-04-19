import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, CopyToClipboard, Button, Editor


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

editor = Editor('{ "value": 10 }')

# copytoclipboard = CopyToClipboard(content=editor)
copytoclipboard = CopyToClipboard(content='{ "value": 10 }')

card = Card(content=Container([copytoclipboard]))

layout = Container(widgets=[card], direction="vertical")
app = sly.Application(layout=layout)
