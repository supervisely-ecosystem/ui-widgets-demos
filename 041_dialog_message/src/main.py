import os
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Button, Flexbox
from supervisely.app import DataJson, StateJson

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# initialize widgets we will use in UI

info_btn = Button("Show info")
warning_btn = Button("Show warning")
error_btn = Button("Show error")
success_btn = Button("Show success")

card = Card(
    title="Dialog message demo",
    description="click button to show dialog window",
    content=Flexbox([info_btn, success_btn, warning_btn, error_btn]),
)

app = sly.Application(layout=card)


@info_btn.click
def show_info():
    sly.app.show_dialog(title="Hello", description="some message", status="info")


@success_btn.click
def show_success():
    sly.app.show_dialog(title="My success", description="Success description", status="success")


@warning_btn.click
def show_waring():
    sly.app.show_dialog(title="My warning", description="some warning", status="warning")
    # or
    # raise sly.app.DialogWindowWarning(title="My warning", description="Warning description")


@error_btn.click
def show_error():
    sly.app.show_dialog(title="My error", description="Error description", status="error")
    # or
    # raise sly.app.DialogWindowError(title="My error", description="Error description")
