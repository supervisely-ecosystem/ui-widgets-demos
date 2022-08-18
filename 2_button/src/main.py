import os
from time import sleep
from dotenv import load_dotenv
import supervisely as sly


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
app = sly.Application(templates_dir=os.path.join(os.getcwd(), "button", "templates"))


# initialize widgets we will use in UI
button_add = sly.app.widgets.Button(text="Add", icon="zmdi zmdi-plus-1")
button_subtract = sly.app.widgets.Button(text="Subtract", icon="zmdi zmdi-neg-1")
text_num = sly.app.widgets.Text(text="0", status="text")


@button_add.click
def add():
    text_num.text = str(int(text_num.text) + 1)


@button_subtract.click
def subtract():
    text_num.text = str(int(text_num.text) - 1)
