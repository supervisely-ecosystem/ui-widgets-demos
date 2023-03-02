import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Empty, Field

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

field = Field(content=Empty(), title="Field", description="Field description")
card = Card(title="Card", description="Card Description", content=field)
app = sly.Application(layout=card)
