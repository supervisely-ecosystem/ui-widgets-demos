import os
from time import sleep

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, DoneLabel

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# initialize widgets we will use in UI
done_label = DoneLabel(
    text="Task has been successfully finished",
)
done_label.hide()

progress = sly.app.widgets.Progress()
start_btn = Button(text="START")

container = Container(widgets=[start_btn, progress, done_label])

card = Card(
    title="Done Label",
    content=container,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@start_btn.click
def start_progress():
    done_label.hide()

    with progress(message="Processing...", total=5) as pbar:
        for _ in range(5):
            sleep(1)
            pbar.update(1)

    done_label.show()
