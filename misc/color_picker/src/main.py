import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, ColorPicker, Text

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api: sly.Api = sly.Api.from_env()


text = Text()

color_picker = ColorPicker()

card = Card(
    "Color Picker",
    content=Container([color_picker, text]),
)


layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@color_picker.value_changed
def show_color(res):
    color_info = f"Current color: {res}"
    text.set(text=color_info, status="info")
