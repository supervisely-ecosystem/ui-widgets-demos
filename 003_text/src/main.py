import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, Text

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# initialize widgets we will use in UI
button_show_text = Button(
    text="Text",
    button_type="primary",
    button_size="small",
    icon="zmdi zmdi-comment-text",
)
button_show_info = Button(
    text="Info", button_type="info", button_size="small", icon="zmdi zmdi-info-outline"
)
button_show_success = Button(
    text="Success", button_type="success", button_size="small", icon="zmdi zmdi-check"
)
button_show_warning = Button(
    text="Warning",
    button_type="warning",
    button_size="small",
    icon="zmdi zmdi-alert-circle-o",
)
button_show_error = Button(
    text="Error",
    button_type="danger",
    button_size="small",
    icon="zmdi zmdi-minus-circle-outline",
)

buttons_container = Container(
    widgets=[
        button_show_text,
        button_show_info,
        button_show_success,
        button_show_warning,
        button_show_error,
    ],
    direction="horizontal",
)

text = Text(text="Lorem ipsum dolor sit amet... anim id est laborum.", status="text")

card = Card(
    title="Text",
    description="👉 Click on the button to change text highlighting",
    content=Container(widgets=[buttons_container, text]),
)

layout = Container(widgets=[card], direction="vertical")
app = sly.Application(layout=layout)


@button_show_text.click
def show_text():
    text.status = "text"


@button_show_info.click
def show_info():
    text.status = "info"


@button_show_success.click
def show_success():
    text.status = "success"


@button_show_warning.click
def show_warning():
    text.status = "warning"


@button_show_error.click
def show_error():
    text.status = "error"
