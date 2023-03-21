import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Text, Tree

load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api: sly.Api = sly.Api.from_env()


data = [
    {
        "id": 1,
        "label": "Level one 1",
        "children": [
            {
                "id": 4,
                "label": "Level two 1-1",
                "children": [
                    {"id": 9, "label": "Level three 1-1-1"},
                    {"id": 10, "label": "Level three 1-1-2"},
                ],
            }
        ],
    },
    {
        "id": 2,
        "label": "Level one 2",
        "children": [{"id": 5, "label": "Level two 2-1"}, {"id": 6, "label": "Level two 2-2"}],
    },
    {
        "id": 3,
        "label": "Level one 3",
        "children": [{"id": 7, "label": "Level two 3-1"}, {"id": 8, "label": "Level two 3-2"}],
    },
]

tree = Tree(data=data, show_checkbox=True)

text = Text()


card = Card(
    "Tree",
    content=Container([tree, text]),
)


layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@tree.node_click
def show_time(res):
    info = f"Current node id={res['id']}, label text: {res['label']}"
    text.set(text=info, status="info")


@tree.check_change
def show_time(res):
    info = f"Current checkbox id={res['id']}"
    text.set(text=info, status="info")
