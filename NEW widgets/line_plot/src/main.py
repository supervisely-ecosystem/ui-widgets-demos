import os

import numpy as np
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, LinePlot
from math import exp

load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

def get_points(size: int=10):
    x = list(range(size))
    y = sorted(np.random.exponential(scale=0.7, size=size).tolist(), reverse=True)
    return [{"x": x_, "y": y_} for x_, y_ in zip(x, y)]

line_chart = LinePlot(
    title="Model losses",
    series=[{"name": "Train loss", "data": get_points(100)}, {"name": "Test loss", "data": get_points(100)}],
)
card = Card(title="Card with line plot", content=line_chart)
app = sly.Application(layout=card)
