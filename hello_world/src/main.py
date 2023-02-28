import os

import names  # requires
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, Text

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))
api = sly.Api()

# initialize widgets that we will use in UI
hello_msg = Text(text="Hello, World!", status="text")
start_btn = Button(text="Generate Name", icon="zmdi zmdi-play")

# create layout using Card widget
layout = Card(title="Hello, World!", content=Container([hello_msg, start_btn]))

# create an app object with layout
app = sly.Application(layout=layout)

# add action to button
@start_btn.click
def generate_name():
    hello_msg.text = f"Hello, {names.get_first_name()}!"
