import os
from time import sleep

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, Text

from awaits.awaitable import awaitable
import asyncio

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


@awaitable
def long_function(steps: int):
    for i in range(steps):
        sleep(1)
        print(f"step {i}")
    return 123


@button_add.click
def add():
    res = asyncio.run(long_function(5))
    print(f"!!! res: {res}")
    text_num.text = str(int(text_num.text) + 1)


@button_subtract.click
def subtract():
    text_num.text = str(int(text_num.text) - 1)
