import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Text, TimePicker

load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api: sly.Api = sly.Api.from_env()

text = Text()
time_picker = TimePicker()

card = Card(
    "Time Picker",
    content=Container([time_picker, text]),
)

layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@time_picker.value_changed
def show_time(res):
    info = f"Selected time: {res}"
    text.set(text=info, status="info")
