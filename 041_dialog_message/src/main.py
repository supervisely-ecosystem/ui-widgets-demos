import os
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Button, Flexbox

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# initialize widgets we will use in UI

info_btn = Button("Show info")
warning_btn = Button("Show warning")
error_btn = Button("Show error")


card = Card(
    title="Dialog message demo",
    description="click button to show dialog window",
    content=Flexbox([info_btn, warning_btn, error_btn]),
)

app = sly.Application(layout=card)

# @TODO: umar change info icon on error
@info_btn.click
def add():
    raise sly.app.DialogWindowError(title="My info", description="Info description")


@warning_btn.click
def add():
    raise sly.app.DialogWindowError(title="My warning", description="Warning description")


@error_btn.click
def add():
    raise sly.app.DialogWindowError(title="My error", description="Error description")
