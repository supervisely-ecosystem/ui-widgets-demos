import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, DestinationProject, Text, TimePicker

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api: sly.Api = sly.Api.from_env()


time_picker = TimePicker()

card = Card(
    "Time Picker",
    content=Container([time_picker]),
)

layout = Container(widgets=[card])
app = sly.Application(layout=layout)
