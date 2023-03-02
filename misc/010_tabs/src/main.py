import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Tabs, Text, Button


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# initialize widgets we will use in UI
tabs = Tabs(
    labels=["Info", "Success", "Warning", "Error"],
    contents=[
        Text("Info text", status="info"),
        Text("Success text", status="success"),
        Text("Warning text", status="warning"),
        Text("Error text", status="error"),
    ],
    type="card",
)

border_tabs = Tabs(
    labels=["Info", "Success", "Warning", "Error"],
    contents=[
        Text("Info text", status="info"),
        Text("Success text", status="success"),
        Text("Warning text", status="warning"),
        Text("Error text", status="error"),
    ],
    type="border-card",
)


button = Button("Show opened tab")
text = Text("")
text.hide()

card = Card(
    title="Tabs (type 'card')",
    content=Container([tabs, button, text]),
)
border_card = Card(
    title="Tabs (type 'border-card')",
    content=border_tabs,
)
layout = Container(widgets=[card, border_card])
app = sly.Application(layout=layout)


@button.click
def show_opened_tab():
    text.show()
    text.text = f"Opened tab: {tabs.get_active_tab()}"
