import os
from dotenv import load_dotenv
import supervisely as sly


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
app = sly.Application(templates_dir=os.path.join(os.getcwd(), "003_text", "templates"))


# initialize widgets we will use in UI
button_show_text = sly.app.widgets.Button(
    text="Text",
    button_type="primary",
    button_size="small",
    icon="zmdi zmdi-comment-text",
)
button_show_info = sly.app.widgets.Button(
    text="Info", button_type="info", button_size="small", icon="zmdi zmdi-info-outline"
)
button_show_success = sly.app.widgets.Button(
    text="Success", button_type="success", button_size="small", icon="zmdi zmdi-check"
)
button_show_warning = sly.app.widgets.Button(
    text="Warning",
    button_type="warning",
    button_size="small",
    icon="zmdi zmdi-alert-circle-o",
)
button_show_error = sly.app.widgets.Button(
    text="Error",
    button_type="danger",
    button_size="small",
    icon="zmdi zmdi-minus-circle-outline",
)

text = sly.app.widgets.Text(
    text="Lorem ipsum dolor sit amet... anim id est laborum.", status="text"
)


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

