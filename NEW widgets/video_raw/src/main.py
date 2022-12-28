import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, InputNumber, Text, VideoRaw

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

video_id = 17546759

# get video info from server
video_info = api.video.get_info_by_id(video_id)

# initialize widgets we will use in UI
video1 = VideoRaw(video_id=video_id)
video2 = VideoRaw(video_id=video_id)

# create control form
input_timestamp = InputNumber(value=0, min=0, max=video_info.duration)
button_jump = Button(text="Jump")
button_get_time = Button(text="Show timestamp")
info_timestamp = Text(status="info")

# create containers for control form
set_container = Container(widgets=[button_jump, input_timestamp])
get_container = Container(widgets=[button_get_time, info_timestamp])
controls_container = Container(widgets=[set_container, get_container], direction="horizontal")

# create new cards
card1 = Card(
    title="Video",
    content=Container(widgets=[video1, controls_container]),
)
card2 = Card(
    title="Video",
    content=video2,
)

layout = Container(widgets=[card1, card2], direction="horizontal", fractions=[1, 1])
app = sly.Application(layout=layout)


# set current timestamp
@button_jump.click
def set_current_timestamp():
    video1.set_current_timestamp(input_timestamp.get_value())


# get current timestamp
@button_get_time.click
def get_current_timestamp():
    info_timestamp.text = str(video1.get_current_timestamp())
