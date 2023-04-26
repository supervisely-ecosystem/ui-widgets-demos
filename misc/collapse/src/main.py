import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Collapse, Table, Text


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

df = {
    "index": [0, 1, 2],
    "x": [1, 2, 3],
    "-x^2": [-1, -4, -9],
}

tbl = Table(data=df)

collapse = Collapse(
    labels=["Collapse with text", "Collapse with table"],
    contents=["Lorem ipsum dolor sit amet, consectetur adipiscing elit.", tbl],
    accordion=False,
)

collapse.add_items([Collapse.Item("Random added item", title="Added item")])

text = Text("Active item: Collapse with text")

layout = Container(widgets=[Card(title="Collapse", content=Container([text, collapse]))])
app = sly.Application(layout=layout)


@collapse.value_changed
def show_active_item(value):
    if isinstance(value, list):
        act_items = ", ".join(value)
    text.text = f"Active item: {act_items}"


@tbl.click
def handle_table_button(datapoint: sly.app.widgets.Table.ClickedDataPoint):
    if datapoint.button_name is None:
        return
