import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, Dropdown, Text

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api: sly.Api = sly.Api.from_env()


items = [
    Dropdown.Item(text="1", command="a"),
    Dropdown.Item(text="2", divided=True, command="b"),
    Dropdown.Item(text="3", disabled=True, command="c"),
]

dropdown = Dropdown(items=items)

text = Text()

card = Card(
    "Dropdown",
    content=Container([dropdown]),
)


layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@dropdown.value_changed
def show_item(res):
    text.set(text=res, status="info")
