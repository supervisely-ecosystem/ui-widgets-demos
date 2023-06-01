import os
from datetime import datetime, timezone
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
def set_only_date_from_today(datetime_value):
    if datetime_value is not None:
        format_string = "%Y-%m-%dT%H:%M:%S.%fZ"
        selected = datetime.strptime(datetime_value, format_string).replace(tzinfo=timezone.utc)
        current_day = datetime.combine(datetime.now().date(), datetime.min.time()).replace(
            tzinfo=timezone.utc
        )
        if selected < current_day:
            new_value = datetime.utcnow().replace(tzinfo=timezone.utc)
            iso_value = new_value.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
            datetime_picker.set_value(iso_value)

    info = f"Selected date and time: {datetime_value}"
    text.set(text=info, status="info")
