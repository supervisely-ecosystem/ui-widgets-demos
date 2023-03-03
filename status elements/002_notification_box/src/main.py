import os
from time import sleep

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, Flexbox, NotificationBox

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

workspace_id = sly.env.workspace_id()

# create Notification Box with "info" box type
note_box_info = NotificationBox()
note_box_info.hide()

step_1_btn = Button(text="INFO", button_type="info")

step_1_container = Container(widgets=[step_1_btn, note_box_info])


# create progress bar for the demo
progress_bar = sly.app.widgets.Progress()

# create Notification Box with "success" box type
note_box_success = NotificationBox(title="Finished.", box_type="success")
note_box_success.hide()
step_2_btn = Button(text="SUCCESS", button_type="success")
step_2 = Container(widgets=[note_box_success, step_2_btn])


# create Notification Box with "error" and "warning" box types
note_box_error = NotificationBox(title="Error.", box_type="error")
note_box_error.hide()
step_3_btn = Button(text="ERROR", button_type="danger")
step_3 = Container(widgets=[note_box_error, step_3_btn])


note_box_warning = NotificationBox(title="Warning.", box_type="warning")
note_box_warning.hide()
step_4_btn = Button(text="WARNING", button_type="warning")
step_4 = Container(widgets=[note_box_warning, step_4_btn])


notes_container = Flexbox(widgets=[note_box_success, note_box_error, note_box_warning])
btns_container = Container(
    widgets=[step_2_btn, step_3_btn, step_4_btn],
    direction="horizontal",
)

progress_container = Container(widgets=[btns_container, progress_bar, notes_container])

container = Container(
    widgets=[step_1_container, progress_container],
    direction="horizontal",
)

card = Card(
    title="Notification Box",
    content=container,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@step_1_btn.click
def create_project_and_dataset():
    project = api.project.create(
        workspace_id=workspace_id,
        name="New project",
        type=sly.ProjectType.IMAGES,
        change_name_if_conflict=True,
    )

    if project is not None:
        note_box_info.set(
            title="New project and dataset created.",
            description=f"Project ID: {project.id}).",
        )
        note_box_info.show()


@step_2_btn.click
def start_progress():
    note_box_warning.hide()
    note_box_error.hide()
    with progress_bar(message="Processing items...", total=5) as pbar:
        for _ in range(5):
            sleep(1)
            pbar.update(1)

    note_box_success.show()


@step_3_btn.click
def show_error():
    note_box_success.hide()
    note_box_warning.hide()
    note_box_error.show()


@step_4_btn.click
def show_warning():
    note_box_success.hide()
    note_box_error.hide()
    note_box_warning.show()
