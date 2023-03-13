import os

from dotenv import load_dotenv
import supervisely as sly
from supervisely.app.widgets import Button, Card, Container
from supervisely.app.widgets import ClassBalance, Input, Text

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

# app requires TASK_ID in local.env

api = sly.Api()

# team_id = sly.env.team_id()


# file_upload = FileStorageUpload(team_id=team_id, path="folder")

# input = Input(placeholder="Please enter path")
# button_change_path = Button("Change path name")
# button_get_paths = Button("Get upoaded paths")

# text = Text()

# btn_container = Container(
#     [button_change_path, button_get_paths],
#     direction="horizontal",
# )
# controls_container = Container([input, btn_container, text])

# card = Card(
#     title="Image Preview",
#     content=Container([file_upload, controls_container]),
# )


max_value = 1000
segments = [
    {"name": "Train", "key": "train", "color": "#1892f8"},
    {"name": "Val", "key": "val", "color": "#25e298"},
    {"name": "Test", "key": "test", "color": "#fcaf33"},
]

rows_data = [
    {
        "nameHtml": "<div>black-pawn</div>",
        "name": "black-pawn",
        "total": 1000,
        "disabled": False,
        "segments": {"train": 600, "val": 350, "test": 50},
    },
    {
        "name": "white-pawn",
        "total": 700,
        "disabled": False,
        "segments": {"train": 400, "val": 250, "test": 50},
    },
    {
        "name": "black-rook",
        "total": 450,
        "disabled": True,
        "segments": {"train": 300, "val": 150, "test": 0},
    },
    {
        "name": "white-rook",
        "total": 250,
        "disabled": False,
        "segments": {"train": 200, "val": 50, "test": 0},
    },
]

slider_data = {
    "black-pawn": [
        {
            "moreExamples": ["https://www.w3schools.com/howto/img_nature.jpg"],
            "preview": "https://www.w3schools.com/howto/img_nature.jpg",
        },
        {
            "moreExamples": ["https://www.quackit.com/pix/samples/18m.jpg"],
            "preview": "https://www.quackit.com/pix/samples/18m.jpg",
        },
    ],
    "white-pawn": [
        {
            "moreExamples": ["https://i.imgur.com/35pUPD2.jpg"],
            "preview": "https://i.imgur.com/35pUPD2.jpg",
        },
        {
            "moreExamples": ["https://i.imgur.com/fB2DBcM.jpeg"],
            "preview": "https://i.imgur.com/fB2DBcM.jpeg",
        },
    ],
    "black-rook": [
        {
            "moreExamples": ["https://i.imgur.com/OpSj3JE.jpg"],
            "preview": "https://i.imgur.com/OpSj3JE.jpg",
        },
        {
            "moreExamples": ["https://www.w3schools.com/howto/img_nature.jpg"],
            "preview": "https://www.w3schools.com/howto/img_nature.jpg",
        },
        {
            "moreExamples": ["https://www.quackit.com/pix/samples/18m.jpg"],
            "preview": "https://www.quackit.com/pix/samples/18m.jpg",
        },
    ],
    "white-rook": [
        {
            "moreExamples": ["https://i.imgur.com/35pUPD2.jpg"],
            "preview": "https://i.imgur.com/35pUPD2.jpg",
        },
        {
            "moreExamples": ["https://i.imgur.com/fB2DBcM.jpeg"],
            "preview": "https://i.imgur.com/fB2DBcM.jpeg",
        },
        {
            "moreExamples": ["https://i.imgur.com/OpSj3JE.jpg"],
            "preview": "https://i.imgur.com/OpSj3JE.jpg",
        },
    ],
}


class_balance = ClassBalance(
    max_value=max_value,
    segments=segments,
    rows_data=rows_data,
    slider_data=slider_data,
    collapsable=True,
    clickable_name=True,
    clickable_segment=True,
)

text = Text()

card = Card(
    content=Container([class_balance, text]),
)

layout = Container(widgets=[card])

app = sly.Application(layout=layout)


@class_balance.click
def show_item(datapoint):
    text.text = datapoint
