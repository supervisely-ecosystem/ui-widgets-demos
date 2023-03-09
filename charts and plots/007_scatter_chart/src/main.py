import os
import numpy as np
import supervisely as sly
from supervisely.app.widgets import Card, Container, Text, ScatterChart
from dotenv import load_dotenv


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

size1 = 10
xy = np.random.normal(15, 6, (size1, 2)).tolist()
s1 = [{"x": x, "y": y} for x, y in xy]

size2 = 30
x2 = list(range(size2))
y2 = np.random.uniform(low=0, high=30, size=size2).tolist()
s2 = [{"x": x, "y": y} for x, y in zip(x2, y2)]

scatter_chart = ScatterChart(
    title="Max vs Denis",
    series=[{"name": "Max", "data": s1}, {"name": "Denis", "data": s2}],
    xaxis_type="numeric",
)


text = Text("Try clicking on point!")
layout = Container([scatter_chart, text])
card = Card(title="Scatter Chart", content=layout)
app = sly.Application(layout=card)


@scatter_chart.click
def on_click(datapoint: ScatterChart.ClickedDataPoint):
    print(f"Line: {datapoint.series_name}")
    print(f"x = {datapoint.x}")
    print(f"y = {datapoint.y}")
    text.set(f"x = {round(datapoint.x, 4)}, y = {round(datapoint.y, 4)}", "info")
    scatter_chart.add_points_to_serie("Max", [51, 52], [51, 52])
    scatter_chart.add_points_to_serie("Denis", 59, 40)
