import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, Input

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

button = Button("Button")

input_1 = Input()
input_2 = Input()
input_3 = Input()

inputs_container = Container(
    widgets=[input_1, input_2, input_3],
    direction="horizontal",
    fractions=[3, 2, 5],
    gap=20,
)
container = Container(widgets=[inputs_container, button])
layout = Card(title="Container card", content=container)
app = sly.Application(layout=layout)
