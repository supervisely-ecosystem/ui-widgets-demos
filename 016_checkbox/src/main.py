import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import (
    Button,
    Card,
    Checkbox,
    Container,
    NotificationBox,
    SelectDataset,
)

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# get variables from environment
project_id = sly.env.project_id()

# create select project widget
select_dataset = SelectDataset(
    project_id=project_id,
    compact=True,
)

# initialize widgets we will use in UI
checkbox = Checkbox(
    content="Choose all datasets",
    checked=False,
    widget_id=None
)

# create button to show images
show_btn = Button(text="Show info")

# create notification box widget
note = NotificationBox()
note.hide()

card = Card(
    title="Checkbox demo",
    content=Container(widgets=[select_dataset, checkbox, show_btn, note]),
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@show_btn.click
def show_info():
    images_count = 0

    # check if checkbox is enabled
    if checkbox.is_checked():
        datasets_list = api.dataset.get_list(project_id=project_id)
        select_dataset.disable()
        for dataset in datasets_list:
            images_count += dataset.images_count if dataset.images_count is not None else 0

    else:
        ds_id = select_dataset.get_selected_id()
        dataset = api.dataset.get_info_by_id(ds_id)
        images_count = dataset.images_count

    note.title = f"Total count of images in selected datasets: {images_count}."
    note.show()


@checkbox.value_changed
def hide_notification(value):
    if value is True:
        select_dataset.disable()
    else:
        select_dataset.enable()

    note.hide()
