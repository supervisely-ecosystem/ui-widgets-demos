import os

import numpy as np
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, LineChart, Table

# for convenient debug, has no effect in production
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

line_chart = LineChart(
    title="Max vs Denis",
    series=[{"name": "Max", "data": s1}],
    xaxis_type="category",
    yaxis_title="sales",
    height=250
)

row_id = 1
columns = ["id", "Line", "x", "y"]
result_table = Table(data=[], columns=columns, width="25%")


container = Container(widgets=[line_chart])
card = Card(title="Line Chart", content=container)
app = sly.Application(layout=card)


@line_chart.click
def add_row_to_table(datapoint: LineChart.ClickedDataPoint):
    global row_id
    row = [row_id, datapoint.series_name, datapoint.x, datapoint.y]
    row_id += 1
    result_table.insert_row(row)
