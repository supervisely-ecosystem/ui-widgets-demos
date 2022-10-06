import os
import names  # requires
from dotenv import load_dotenv
import supervisely as sly
from supervisely.app.widgets import Card, Container


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# initialize widgets we will use in UI
hello_msg = sly.app.widgets.Text(text="Hello, World!", status="text")
start_btn = sly.app.widgets.Button(text="Generate Name", icon="zmdi zmdi-play")

# create sly-card object
card = Card(title="Hello, World!", content=Container([hello_msg, start_btn]))
layout = Container(widgets=[card], direction="vertical")

app = sly.Application(layout=layout)


@start_btn.click
def generate_name():
    hello_msg.text = f"Hello, {names.get_first_name()}!"
