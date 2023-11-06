import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Timeline, Text, InputNumber, Flexbox, Field

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

timeline = Timeline(
    frames_count=31,
    intervals=[[0, 6], [6, 11], [12, 15], [16, 17], [18, 19], [20, 31]],
    colors=["#DB7093", "#93db70", "#7093db", "#70dbb8", "#db8370", "#db70c9"],
    height="30px",
)

timeline_select_frame = InputNumber(value=1, min=0, max=31, step=1)

timeline_value = Text("Frames:", "text")
timeline_container = Container(
    widgets=[
        timeline,
        Text("<span>Frame:</span>"),
        timeline_select_frame,
    ],
    direction="horizontal",
    fractions=[1, 0, 0],
    style="place-items: center;",
)

card = Card(title="Timeline", content=timeline_container)
app = sly.Application(layout=card)


@timeline.click
def show_current_value(pointer):
    timeline_select_frame.value = pointer


@timeline_select_frame.value_changed
def set_timeline_pointer(frame):
    timeline.set_pointer(frame)
