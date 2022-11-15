import os
from random import randint

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, Video


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

video_id = int(os.environ["modal.state.slyVideoId"])
video_info = api.video.get_info_by_id(id=video_id)
video = Video(video_id=video_id)

button_random_frame = Button(text="Random", icon="zmdi zmdi-tv")
button_play = Button(text="Play", icon="zmdi zmdi-play")
button_pause = Button(text="Pause", icon="zmdi zmdi-pause")
button_loading = Button(text="Loading", icon="zmdi zmdi-refresh")

buttons_container = Container(
    widgets=[button_random_frame, button_play, button_pause, button_loading],
    direction="horizontal",
)

card = Card(
    title="Video",
    content=Container(widgets=[video, buttons_container]),
)

layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@video.play_clicked
def play(start_frame: int):
    print(f"Start play frame: {start_frame}")


@video.pause_clicked
def pause(current_frame: int):
    print(f"Pause frame: {current_frame}")


@video.frame_change_started
def change_frame_start(current_frame: int):
    print(f"Frame change started: {current_frame}")


@video.frame_change_finished
def change_frame_end(current_frame: int):
    print(f"Frame change finished: {current_frame}")


@button_random_frame.click
def set_random_frame():
    video.set_current_frame(randint(0, video_info.frames_count - 1))


# @button_play.click
# def play_video():
#     from time import sleep
#     video.frame = video.get_current_frame()
#     if video.frame == video_info.frames_count - 1:
#         video.frame == 0
#     video.playing = True
#     while video.frame != video_info.frames_count - 1:
#         video.frame += 1
#         sleep(0.04)
#         if not video.playing:
#             break


@button_pause.click
def pause_video():
    video.set_current_frame(value=video.get_current_frame())


@button_loading.click
def video_loading():
    if video.loading:
        video.loading = False
    else:
        video.loading = True
    print(f"Loading: {video.loading}")
