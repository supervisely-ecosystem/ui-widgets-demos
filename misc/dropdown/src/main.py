import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Dropdown, Text

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api: sly.Api = sly.Api.from_env()


items = [
    Dropdown.Item(text="1", command="A"),
    Dropdown.Item(text="2", divided=True, command="B"),
    Dropdown.Item(text="3", disabled=True, command="C"),
    Dropdown.Item(text="4", command="D"),
    Dropdown.Item(text="5", divided=True, command="E"),
    Dropdown.Item(text="6", command="F"),
]

dropdown = Dropdown(items=items, header="Example dropdown")

text = Text()

card = Card(
    "Dropdown",
    content=Container([dropdown, text]),
)


layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@dropdown.value_changed
def show_item(res):
    info = f"Command {res} will be executed"
    text.set(text=info, status="info")
