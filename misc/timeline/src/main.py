import os

from dotenv import load_dotenv
import supervisely as sly
from supervisely.app.widgets import Button, Card, Container, Field, Timeline
from supervisely.app.widgets import FileStorageUpload, Flexbox, Input, Text

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()


timeline = Timeline()

card = Card(
    # title="File Storage Upload",
    content=Container([timeline]),
)

layout = Container(widgets=[card])

app = sly.Application(layout=layout)
