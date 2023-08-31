import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, DatePicker, Text

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api: sly.Api = sly.Api.from_env()

daterange_picker = DatePicker(
    editable=False,
    placeholder="Select date range",
    picker_type="daterange",
)
date_picker = DatePicker(
    editable=False,
)
text = Text()
button_clear = Button("Clear")
button_default = Button("Set default")

controls_container = Container([button_clear, button_default], direction="horizontal")
middle_container = Container([controls_container, text])

card = Card(
    "Date Picker",
    content=Container([daterange_picker, middle_container, date_picker], direction="horizontal"),
)


layout = Container(widgets=[card])
app = sly.Application(layout=layout)


def _check_dates(value1, value2):
    from datetime import datetime

    if value1 is None or value2 is None:
        text.set(text="", status="info")
        return

    def _get_datetime(val: str):
        val = val.replace("T", " ").replace("Z", "")
        return datetime.strptime(val, "%Y-%m-%d %H:%M:%S.%f")

    if _get_datetime(value2[0]) <= _get_datetime(value1) <= _get_datetime(value2[1]):
        text.set(text="Date 1 in daterange.", status="success")
        return
    text.set(text="Date 1 not in daterange.", status="error")


@date_picker.value_changed
def check_date(date_value):
    daterange_value = daterange_picker.get_value()
    _check_dates(date_value, daterange_value)


@daterange_picker.value_changed
def check_daterange(daterange_value):
    date_value = date_picker.get_value()
    _check_dates(date_value, daterange_value)


@button_clear.click
def clear_dates():
    date_picker.clear_value()
    daterange_picker.clear_value()


@button_default.click
def set_default():
    from datetime import datetime, timedelta

    now = datetime.now()
    yesterday = now - timedelta(days=1)
    tomorrow = now + timedelta(days=1)

    date_picker.set_value(now)
    daterange_picker.set_range_values([yesterday, tomorrow])
