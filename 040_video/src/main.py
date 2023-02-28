import os
from random import randint

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, Video

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# get video ID from environment
video_id = int(os.environ["modal.state.slyVideoId"])

# get VideoInfo from server
video_info = api.video.get_info_by_id(id=video_id)

# initialize widgets we will use in UI
video = Video(video_id=video_id)

# buttons to control widget from python code
button_random_frame = Button(text="Random", icon="zmdi zmdi-tv")
button_loading = Button(text="Loading", icon="zmdi zmdi-refresh")

buttons_container = Container(
    widgets=[button_random_frame, button_loading],
    direction="horizontal",
)

card = Card(
    title="Video",
    content=Container(widgets=[video, buttons_container]),
)

layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@button_random_frame.click
def set_random_frame():
    video.set_current_frame(randint(0, video_info.frames_count - 1))


@button_loading.click
def video_loading():
    if video.loading:
        video.loading = False
    else:
        video.loading = True
    print(f"Loading: {video.loading}")
