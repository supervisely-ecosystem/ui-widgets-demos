import os

from dotenv import load_dotenv
import supervisely as sly
from supervisely.app.widgets import Card, Container, Timeline, Text

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

intervals = [
    [1, 60],
    [100, 300],
    [320, 330],
    [340, 345],
    [400, 450],
    [500, 700],
    [800, 900],
]

colors = ["#99d162", "#00f0b0", "#e41436", "#14d7e4", "#99d162", "#ffff00", "#00ff00"]

pointer_color = "#ffffff"

text = Text()

timeline = Timeline(pointer=220, intervals=intervals, colors=colors)

intervals = [
    [0, 50],
    [60, 90],
]

colors = ["#000772", "#00ff00"]


# a = timeline.get_intervals()
# timeline.add_intervals(intervals, colors)
# b = timeline.get_intervals()

# timeline.set_height(500)
# timeline.set_pointer_color(pointer_color)

# timeline = Timeline(intervals=intervals, colors=colors)

card = Card(
    title="Timeline",
    content=Container([timeline, text]),
)

layout = Container(widgets=[card])

app = sly.Application(layout=layout)


# @timeline.click
# def show_item(res):
#     text.set(text=res, status="info")
