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


def long_function(steps: int):
    for i in range(steps):
        sleep(1)
        print(f"step {i}")
    # raise ValueError(123)
    return 123


def callback(future):
    if future.exception():
        print(repr(future.exception()))
    else:
        print(future.result())


import asyncio
import concurrent

executor = concurrent.futures.ThreadPoolExecutor()
loop = asyncio.get_event_loop()


@button_add.click
def add():
    my_future = loop.run_in_executor(executor, long_function, 5)
    task = asyncio.ensure_future(my_future, loop=loop)
    task.add_done_callback(callback)
    # res = long_function(5)
    # print(f"!!! res: {res}")
    text_num.text = str(int(text_num.text) + 1)


@button_subtract.click
def subtract():
    text_num.text = str(int(text_num.text) - 1)
