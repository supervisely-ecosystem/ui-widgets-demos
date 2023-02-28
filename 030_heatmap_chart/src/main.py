import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, HeatmapChart

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# function to build example chart
def multiplication_chart():
    data = []
    for row in list(range(1, 11)):
        temp = [round(row * number, 1) for number in list(range(1, 11))]
        data.append(temp)
    return data


# initialize widgets we will use in UI
chart = HeatmapChart(
    title="Multiplication Table",
    xaxis_title="xaxis_title",
    color_range="table",
    tooltip="Result multiplication of {x} * {series_name}",
)

data = multiplication_chart()

lines = [{"name": idx + 1, "x": list(range(1, 11)), "y": line} for idx, line in enumerate(data)]

chart.add_series_batch(lines)
card = Card(
    title="Heatmap Chart",
    content=chart,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
