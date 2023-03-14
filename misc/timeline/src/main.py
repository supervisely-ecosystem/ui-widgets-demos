import os

from dotenv import load_dotenv
import supervisely as sly
from supervisely.app.widgets import Button, Card, Container, Field, Timeline
from supervisely.app.widgets import FileStorageUpload, Flexbox, Input, Text

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

intervals = [
    [1, 1],
    [3, 9],
    [10, 20],
    [40, 70],
    [80, 90],
    [100, 300],
    [320, 330],
    [340, 345],
    [400, 450],
    [500, 540],
    [650, 680],
    [700, 750],
    [900, 1100],
    [1200, 1230],
    [1240, 1243],
]

colors = [
    "#99d162",
    "#99d162",
    "#99d162",
    "#99d162",
    "#99d162",
    "#99d162",
    "#99d162",
    "#99d162",
    "#99d162",
    "#99d162",
    "#99d162",
    "#99d162",
    "#99d162",
    "#99d162",
    "#99d162",
]

pointer_color = (255, 0, 127, 1)
timeline = Timeline(
    frames_count=1243, intervals=intervals, colors=colors, pointer_color=pointer_color
)

card = Card(
    # title="File Storage Upload",
    content=Container([timeline]),
)

layout = Container(widgets=[card])

app = sly.Application(layout=layout)
