import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, ColorPicker

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api: sly.Api = sly.Api.from_env()

color_picker = ColorPicker(show_alpha=False)

card = Card(
    "Destination Project",
    content=Container([color_picker]),
)


layout = Container(widgets=[card])
app = sly.Application(layout=layout)
