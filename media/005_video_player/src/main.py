import os
from pathlib import Path

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, Checkbox
from supervisely.app.widgets import Flexbox, InputNumber, VideoPlayer
from supervisely._utils import abs_url

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()


# get video ID from environment variables
video_id = int(os.environ["modal.state.slyVideoId"])

# get VideoInfo from server
video_info = api.video.get_info_by_id(id=video_id)

# prepare url and mime type for video from server
video_url = abs_url(video_info.path_original)
video_mime_type = video_info.file_meta["mime"]

# prepare url and mime type for video from local directory
local_video_url = "/static/video-cam2.mp4"
local_video_type = "video/mp4"


# initialize widgets we will use in UI
video1 = VideoPlayer(url=local_video_url, mime_type=local_video_type)
video2 = VideoPlayer()
video2.set_video(url=video_url, mime_type=video_mime_type)


# create play/pause buttons
play_btn = Button(text="Play", button_size="mini", icon="zmdi zmdi-play")
pause_btn = Button(text="Pause", button_size="mini", icon="zmdi zmdi-pause")

# create current time control form
get_time_btn = Button(text="Get timestamp", button_size="mini")
input_time = InputNumber(
    value=0,
    min=0,
    max=round(video_info.file_meta["duration"], 1),
    step=0.1,
)
set_time_btn = Button(text="Set timestamp", button_size="mini")


input_sec = InputNumber(min=0.1, max=1000, step=0.1, size="small", controls=True)
forward_btn = Button(text="", button_size="mini", icon="zmdi zmdi-fast-forward", icon_gap=0)
rewind_btn = Button(text="", button_size="mini", icon="zmdi zmdi-fast-rewind", icon_gap=0)


# create containers for control form
controls_container = Flexbox(widgets=[play_btn, pause_btn])
change_timestamp_container = Flexbox(
    widgets=[rewind_btn, input_sec, forward_btn, get_time_btn, input_time, set_time_btn]
)

# prepare mask drawing controls and mask url
draw_mask_checkbox = Checkbox("draw mask on video")
mask_url = "https://user-images.githubusercontent.com/79905215/221801327-7be20a37-d4c0-4f7d-aa35-a072c4839985.png"

# create new cards
card1 = Card(
    title="Video player",
    description="This widget uses video from a local directory",
    content=video1,
)
card2 = Card(
    title="Controls - operations from python code",
    description="This widget uses video from the server",
    content=Container(
        widgets=[video2, draw_mask_checkbox, controls_container, change_timestamp_container]
    ),
)

layout = Container(widgets=[card1, card2], direction="horizontal", fractions=[1, 1])

# declare static files directory path to use videos from local directory
static_dir = Path("media/005_video_player/videos")


app = sly.Application(layout=layout, static_dir=static_dir)


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


# draw mask on video
@draw_mask_checkbox.value_changed
def draw_mask(value):
    global g
    if value is False:
        video2.hide_mask()
        return
    video2.draw_mask(mask_url)


@forward_btn.click
def fast_forward_video():
    step = input_sec.get_value()
    if video2.url is None:
        return
    currrent_time = video2.get_current_timestamp()
    video2.set_current_timestamp(currrent_time + step)


@rewind_btn.click
def fast_rewind_video():
    step = input_sec.get_value()
    if video2.url is None:
        return
    currrent_time = video2.get_current_timestamp()
    video2.set_current_timestamp(currrent_time - step)
