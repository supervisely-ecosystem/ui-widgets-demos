import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, NodesFlow

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

card = Card(title="NodesFlow", content=None)
app = sly.Application(layout=card)
