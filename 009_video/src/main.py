import os
from random import randint
from dotenv import load_dotenv
import supervisely as sly


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
app = sly.Application(templates_dir=os.path.join(os.getcwd(), "009_video", "templates"))


video_id = 25598
video_info = api.video.get_info_by_id(id=video_id)
video = sly.app.widgets.Video(video_id=video_id)

button_random_frame = sly.app.widgets.Button(text="Random", icon="zmdi zmdi-tv")
button_play = sly.app.widgets.Button(text="Play", icon="zmdi zmdi-play")
button_pause = sly.app.widgets.Button(text="Pause", icon="zmdi zmdi-pause")


@video.play_clicked
def play(start_frame: int):
    print(f"Start play frame: {start_frame}")


@video.pause_clicked
def pause(current_frame: int):
    print(f"Pause frame: {current_frame}")


@video.frame_change_start
def change_frame_start(current_frame: int):
    print(f"Frame change start: {current_frame}")


@video.frame_change_end
def change_frame_end(current_frame: int):
    print(f"Frame change end: {current_frame}")


@button_random_frame.click
def set_random_frame():
    video.frame = randint(0, video_info.frames_count - 1)


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
    video.playing = False
    video.frame = video.get_current_frame()
