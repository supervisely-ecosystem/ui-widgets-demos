import os
import random
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Collapse, Table, Text, Button


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

table_data = {
    "index": [0, 1, 2],
    "x": [1, 2, 3],
    "-x^2": [-1, -4, -9],
}

tbl = Table(data=table_data)
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

items = [
    Collapse.Item(name="table", title="Collapse with text", content=text),
    Collapse.Item(name="text", title="Collapse with table", content=tbl),
    Collapse.Item(name="1", title="Random #1", content="Random #1"),
    Collapse.Item(name="2", title="Random #2", content="Random #2"),
]

collapse = Collapse(
    items=items,
    accordion=False,
)

button = Button("Open random collapse")
text = Text("Active item: Collapse with text")

layout = Container(widgets=[Card(title="Collapse", content=Container([text, collapse, button]))])
app = sly.Application(layout=layout)


@collapse.value_changed
def show_active_item(value):
    if isinstance(value, list):
        act_items = ", ".join(value)
    text.text = f"Active item: {act_items}"


@button.click
def open_random_collapse():
    panels = list(collapse.items_names)
    value = panels[random.randint(0, len(panels) - 1)]
    collapse.set_active_panel(value)
    text.text = f"Active item: {value}"


@tbl.click
def handle_table_button(datapoint: sly.app.widgets.Table.ClickedDataPoint):
    if datapoint.button_name is None:
        return
