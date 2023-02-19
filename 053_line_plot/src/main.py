import os
import numpy as np
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, LinePlot, LineChart

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
    show_legend=False,
)

# element_button = LinePlot(title="LinePlot title")


card = Card(
    # title="Element Button",
    content=line_chart,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
