import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, RadioTabs, Text, Button


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# initialize widgets we will use in UI
tabs = RadioTabs(
    titles=["Info tab", "Success tab", "Warning tab", "Error tab"],
    contents=[
        Text("Info text", status="info"),
        Text("Success text", status="success"),
        Text("Warning text", status="warning"),
        Text("Error text", status="error"),
    ],
    descriptions=[
        "Tab with info text",
        "Tab with success text",
        "Tab with warning text",
        "Tab with error text",
    ],
)

many_tabs = RadioTabs(
    titles=[f"{i + 1} tab" for i in range(10)],
    contents=[Text(f"{i + 1} text", status="info") for i in range(10)],
    descriptions=[f"Tab with {i + 1} text" for i in range(10)],
)

text = Text("Opened tab: Info tab")

card = Card(
    title="Radio tabs",
    content=Container([tabs, text]),
)
card_many_tabs = Card("Many radio tabs", content=many_tabs)
layout = Container(widgets=[card, card_many_tabs])
app = sly.Application(layout=layout)


@tabs.value_changed
def show_opened_tab(value):
    text.text = f"Opened tab: {value}"
