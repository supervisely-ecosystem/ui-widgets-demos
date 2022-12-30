import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, Flexbox, InputNumber, Text, VideoPlayer
from supervisely._utils import abs_url

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()


# prepare video and video info
video_url = "https://user-images.githubusercontent.com/79905215/210067166-e5531dae-d090-436e-bb3b-f053e2e831eb.mp4"
video_type = "video/mp4"
video_meta = sly.video.get_info(video_url)

# initialize widgets we will use in UI
video1 = VideoPlayer(url=video_url, mime_type=video_type)
video2 = VideoPlayer()
video2.set_video(url=video_url, mime_type=video_type)

# create play/pause buttons
play_btn = Button(text="Play", button_size="mini", icon="zmdi zmdi-play")
pause_btn = Button(text="Pause", button_size="mini", icon="zmdi zmdi-pause")

# create current time control form
get_time_btn = Button(text="Get timestamp", button_size="mini")
input_time = InputNumber(
    value=0,
    min=0,
    max=round(video_meta["duration"], 1),
    step=0.1,
)
set_time_btn = Button(text="Set timestamp", button_size="mini")

# create containers for control form
controls_container = Flexbox(
    widgets=[play_btn, pause_btn, get_time_btn, input_time, set_time_btn],
    center_content=True,
)

# create new cards
card1 = Card(
    title="Video player",
    content=video1,
)
card2 = Card(
    title="Controls - operations from python code",
    content=Container(widgets=[video2, controls_container]),
)

layout = Container(widgets=[card1, card2], direction="horizontal", fractions=[1, 1])
app = sly.Application(layout=layout)


# start playing video
@play_btn.click
def play():
    video2.play()


# pause video
@pause_btn.click
def pause():
    video2.pause()


# get current timestamp
@get_time_btn.click
def get_current_timestamp():
    input_time.value = video2.get_current_timestamp()


# set current timestamp
@set_time_btn.click
def set_current_timestamp():
    time_to_set = input_time.get_value()
    video2.set_current_timestamp(time_to_set)
