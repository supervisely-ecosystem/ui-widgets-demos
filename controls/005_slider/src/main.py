import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Slider


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

slider = Slider(
    value=[10, 50],
    step=5,
    range=True,
    show_stops=True,
)


card = Card(title="Slider", content=Container([slider]))
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
