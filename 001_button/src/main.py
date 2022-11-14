import os
from time import sleep

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, Text

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# initialize widgets we will use in UI
button_add = Button(text="Add", icon="zmdi zmdi-plus-1")
button_subtract = Button(text="Subtract", icon="zmdi zmdi-neg-1")
text_num = Text(text="0", status="text")

card = Card(
    "Button",
    description="👉 Click on the button to add or subtract 1",
    content=Container([button_add, button_subtract, text_num]),
)
layout = Container(widgets=[card], direction="vertical")
app = sly.Application(layout=layout)


@button_add.click
def add():
    text_num.text = str(int(text_num.text) + 1)


@button_subtract.click
def subtract():
    text_num.text = str(int(text_num.text) - 1)
