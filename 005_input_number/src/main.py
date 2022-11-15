import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, InputNumber


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
input_number = InputNumber()
card = Card(
    title="Input Number",
    content=Container(widgets=[input_number]),
)

layout = Container(widgets=[card], direction="vertical")
app = sly.Application(layout=layout)
