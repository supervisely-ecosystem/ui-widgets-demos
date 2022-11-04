import os
from re import T

import supervisely as sly
from dotenv import load_dotenv

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
app = sly.Application(templates_dir=os.path.join(os.getcwd(), "014_tag", "templates"))

default_tag = sly.app.widgets.Tag(text="Default")
gray_tag = sly.app.widgets.Tag(text="Gray", type="gray")
primary_tag = sly.app.widgets.Tag(text="Primary", type="primary")
success_tag = sly.app.widgets.Tag(text="Success", type="success")
warning_tag = sly.app.widgets.Tag(text="Warning", type="warning")
danger_tag = sly.app.widgets.Tag(text="Danger", type="danger")

highlight_border_button = sly.app.widgets.Button(text="Enable border highlighting")


@highlight_border_button.click
def highlight():
    tags = [default_tag, gray_tag, primary_tag, success_tag, warning_tag, danger_tag]
    for tag in tags:
        if tag.is_border_highlighted():
            tag.disable_border_highlighting()
        else:
            tag.enable_border_highlighting()
