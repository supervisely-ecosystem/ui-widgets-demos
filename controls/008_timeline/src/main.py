import os
from random import randint
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import (
    Card,
    Container,
    Timeline,
    Text,
    InputNumber,
    VideoThumbnail,
)


def divide_to_ranges(total, n):
    step = total // n
    ranges = []
    for i in range(n):
        start = i * step
        end = start + step - 1 if i < n - 1 else total - 1
        ranges.append([start, end])
    return ranges, len(ranges)


def generate_hex_colors(n):
    colors = []
    for _ in range(n):
        color = "#{:06x}".format(randint(0, 0xFFFFFF))
        colors.append(color)
    return colors


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()


video_id = 350000  # set your video id here
video = api.video.get_info_by_id(video_id)
video_thumbnail = VideoThumbnail(video)

video_intervals, intervals_n = divide_to_ranges(video.frames_count, 5)
intervals_colors = generate_hex_colors(intervals_n)

timeline = Timeline(
    frames_count=video.frames_count,
    intervals=video_intervals,
    colors=intervals_colors,
    height="35px",
)

timeline_select_frame = InputNumber(value=1, min=0, max=video.frames_count, step=1)
timeline_text = Text("<span>Frame:</span>")
timeline_container = Container(
    widgets=[
        timeline,
        timeline_text,
        timeline_select_frame,
    ],
    direction="horizontal",
    fractions=[1, 0, 0],
    style="place-items: center;",
)

main_container = Container(widgets=[video_thumbnail, timeline_container])
card = Card(title="Timeline", content=main_container)
app = sly.Application(layout=card)


@timeline.click
def show_current_value(pointer):
    timeline_select_frame.value = pointer


@timeline_select_frame.value_changed
def set_timeline_pointer(frame):
    timeline.set_pointer(frame)
