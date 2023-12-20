import os
from time import sleep
import supervisely as sly
from supervisely.app.widgets import Card, CircleProgress, Container, Button, Progress
from dotenv import load_dotenv


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

progress = Progress()
circle_progress = CircleProgress(progress=progress)
button = Button("Start", button_size="mini")
container = Container([circle_progress, button])

card = Card(
    title="Circle Progress",
    content=container,
)
layout = card
app = sly.Application(layout=layout)


@button.click
def start_progress():
    circle_progress.set_status("none")
    with progress(message="Processing items ...", total=100) as pbar:
        for _ in range(10):
            sleep(0.5)
            pbar.update(10)
        circle_progress.set_status("success")
