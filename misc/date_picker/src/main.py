import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, DatePicker, Text
from supervisely._utils import get_datetime

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

range_container = Container([daterange_picker, text])
card = Card(
    "Date Picker",
    content=Container([range_container, date_picker], direction="horizontal"),
)


layout = Container(widgets=[card])
app = sly.Application(layout=layout)


def _check_dates(value1, value2):
    if value1 is None or value2 is None:
        text.set(text="", status="info")
        return None
    if get_datetime(value2[0]) <= get_datetime(value1) <= get_datetime(value2[1]):
        text.set(text="Date 1 in daterange.", status="success")
        return
    text.set(text="Date 1 not in daterange.", status="error")


@date_picker.value_changed
def check_date(value):
    value2 = daterange_picker.get_value()
    _check_dates(value, value2)


@daterange_picker.value_changed
def check_daterange(value):
    value1 = date_picker.get_value()
    _check_dates(value1, value)
