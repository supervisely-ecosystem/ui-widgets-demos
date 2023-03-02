import os
import supervisely as sly
from supervisely.app.widgets import Card, Container, GridPlot
from dotenv import load_dotenv
import numpy as np


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

size1 = 10
x1 = list(range(size1))
y1 = np.random.randint(low=10, high=148, size=size1).tolist()
s1 = [{"x": x, "y": y} for x, y in zip(x1, y1)]

size2 = 30
x2 = list(range(size2))
y2 = np.random.randint(low=0, high=300, size=size2).tolist()
s2 = [{"x": x, "y": y} for x, y in zip(x2, y2)]

data_max = {"title": "Max", "series": [{"name": "Max", "data": s1}]}

data_denis = {
    "title": "Denis",
    "series": [{"name": "Denis", "data": s2}],
}

data_all = {
    "title": "Max vs Denis",
    "series": [{"name": "Max", "data": s1}, {"name": "Denis", "data": s2}],
}

grid_plot = GridPlot(data=[data_max, data_denis, data_all], columns=2)

card = Card(
    title="GridPlot",
    content=grid_plot,
)

layout = Container(widgets=[card])
app = sly.Application(layout=layout)
