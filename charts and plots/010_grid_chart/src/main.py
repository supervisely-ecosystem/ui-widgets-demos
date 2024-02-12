import supervisely as sly
from supervisely.app.widgets import Card, Container, GridChart
from dotenv import load_dotenv
import numpy as np

load_dotenv("local.env")
api = sly.Api.from_env()

size1 = 10
x1 = list(range(size1))
y1 = np.random.randint(low=10, high=148, size=size1).tolist()
s1 = [{"x": x, "y": y} for x, y in zip(x1, y1)]

size2 = 30
x2 = list(range(size2))
y2 = np.random.randint(low=0, high=300, size=size2).tolist()
s2 = [(x, y) for x, y in zip(x2, y2)]

data_max = {"title": "Max", "series": [{"name": "Max", "data": s1}]}
data_denis = {"title": "Denis", "series": [{"name": "Denis", "data": s2}]}
data_all = {
    "title": "Max vs Denis",
    "series": [{"name": "Max", "data": s1}, {"name": "Denis", "data": s2}],
}

grid_chart = GridChart(data=[data_max, data_denis, data_all], columns=2)
card = Card(
    title="GridChart",
    content=grid_chart,
)

layout = Container(widgets=[card], direction="vertical")

app = sly.Application(layout=layout)
