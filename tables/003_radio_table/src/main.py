import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, RadioTable

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# initialize widgets we will use in UI
radio_table = RadioTable(
    columns=["Format", "Total Images", "Number of Classes", "Number of Objects"],
    rows=[
        ["Supervsiely", "245", "15", "5468"],
        ["PascalVOC", "76", "20", "387"],
        ["COCO", "128", "80", "786"],
        ["Cityscapes", "45", "35", "1334"],
    ],
)

card = Card(
    title="Radio Table",
    content=radio_table,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
