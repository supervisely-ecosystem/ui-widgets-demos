import os
from time import sleep
from dotenv import load_dotenv
import supervisely as sly


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
app = sly.Application(
    templates_dir=os.path.join(os.getcwd(), "progress_bar", "templates")
)


# initialize widgets we will use in UI
progress = sly.app.widgets.Progress(hide_on_finish=False)
button = sly.app.widgets.Button(text="Start", icon="zmdi zmdi-play")
finish_msg = sly.app.widgets.Text(status="success")


@button.click
def start_progress():
    with progress(message=f"Processing items...", total=20) as pbar:
        for _ in range(20):
            sleep(1)
            pbar.update(1)

    finish_msg.text = "Finished"
