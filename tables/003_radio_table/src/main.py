import os
import time

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, DoneLabel, Progress, RadioTable


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# initialize widgets we will use in UI
radio_table = RadioTable(
    columns=["Format", "Total Images", "Number of Classes", "Number of Objects"],
    rows=[
        ["Supervisely", "245", "15", "5468"],
        ["PascalVOC", "76", "20", "387"],
        ["COCO", "128", "80", "786"],
        ["Cityscapes", "45", "35", "1334"],
    ],
)

button = Button("Button")
progress = Progress(message="processing images", show_percents=True)
progress.hide()

done_label = DoneLabel()
done_label.hide()

radio_table_card = Card(
    title="Radio Table",
    content=Container([radio_table, button]),
)

progress_card = Card(
    title="Progress",
    content=Container([progress, done_label]),
)

layout = Container(
    widgets=[radio_table_card, progress_card],
    direction="horizontal",
    fractions=[1, 1],
)
app = sly.Application(layout=layout)


@button.click
def show_progress():
    progress.show()
    selected_row = radio_table.get_selected_row()
    images_count = int(selected_row[1])

    with progress(message="Processing images...", total=images_count) as pbar:
        for _ in range(images_count):
            time.sleep(0.01)
            pbar.update(1)
    done_label.text = f"{images_count} images processed from {selected_row[0]} format data."
    done_label.show()
