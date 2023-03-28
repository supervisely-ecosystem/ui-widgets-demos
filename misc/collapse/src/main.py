import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Collapse, Table


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
    accordion=True,
)

card = Card(title="Collapse", content=Container([collapse]))
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
