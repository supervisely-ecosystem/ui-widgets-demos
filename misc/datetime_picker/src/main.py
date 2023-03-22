import os
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Text, DateTimePicker

load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api: sly.Api = sly.Api.from_env()

text = Text()
datetime_picker = DateTimePicker()

card = Card(
    "Date and Time Picker",
    content=Container([datetime_picker, text]),
)

layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@datetime_picker.value_changed
def show_datetime(res):
    info = f"Selected date and time: {res}"
    text.set(text=info, status="info")
