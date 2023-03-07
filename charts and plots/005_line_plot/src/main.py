import os
import random
import numpy as np
import supervisely as sly
from supervisely.app.widgets import Card, Container, LinePlot
from dotenv import load_dotenv


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

line_chart = LinePlot(
    title="Max vs Denis",
    series=[{"name": "Max", "data": s1}, {"name": "Denis", "data": s2}],
    yaxis_autorescale=True,
)
line_chart2 = LinePlot(
    title="Max vs Denis",
    series=[{"name": "Max", "data": s1}, {"name": "Denis", "data": s2}],
    yaxis_autorescale=False,
)

x1 = list(range(1, 11))
y1 = [random.randint(10, 148) for _ in range(1, 11)]

x2 = list(range(1, 31))
y2 = [random.randint(1, 300) for _ in range(1, 31)]

line_plot = LinePlot("My Line Plot")
line_plot.add_series("Line 1", x1, y1)
line_plot.add_series("Line 2", x2, y2)

card = Card(
    title="Line Plot",
    content=Container([line_chart, line_chart2], direction="horizontal"),
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
