import os
from time import sleep

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# initialize widgets we will use in UI
progress_bar = sly.app.widgets.Progress()
start_btn = sly.app.widgets.Button(text="Start", icon="zmdi zmdi-play")
finish_msg = sly.app.widgets.Text(status="success")

card = Card(
    title="Progress Bar",
    description="👉 Click on the button to start",
    content=Container([progress_bar, start_btn, finish_msg]),
)
layout = Container(widgets=[card], direction="vertical")
app = sly.Application(layout=layout)


@start_btn.click
def start_progress():
    with progress_bar(message=f"Processing items...", total=10) as pbar:
        for _ in range(10):
            sleep(0.5)
            pbar.update(1)

    finish_msg.text = "Finished"
