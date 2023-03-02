import os

import numpy as np
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Apexchart, Card, Container, Text

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

size1 = 22
x1 = list(range(size1))
y1 = np.random.randint(low=10, high=180, size=size1).tolist()
s1 = [{"x": x, "y": y} for x, y in zip(x1, y1)]

size2 = 30
x2 = list(range(size2))
y2 = np.random.randint(low=0, high=300, size=size2).tolist()
s2 = [{"x": x, "y": y} for x, y in zip(x2, y2)]

apexchart = Apexchart(
    series=[{"name": "Fred", "data": s1}, {"name": "Harry", "data": s2}],
    options={
        "chart": {"type": "line", "zoom": {"enabled": False}},
        "dataLabels": {"enabled": False},
        "stroke": {"curve": "smooth", "width": 2},
        "title": {"text": "Product sales by month", "align": "left"},
        "grid": {"row": {"colors": ["#f3f3f3", "transparent"], "opacity": 0.5}},
        "xaxis": {"type": "category"},
    },
    type="line",
)
info_text = Text(status="info")
info_text.hide()
card = Card(title="Apexchart", content=Container([apexchart, info_text]))
app = sly.Application(layout=card)


@apexchart.click
def show_info(datapoint: sly.app.widgets.Apexchart.ClickedDataPoint):
    info_text.show()
    x = datapoint.x
    y = datapoint.y
    name = datapoint.series_name
    info_text.text = f"On May {x}, {name} has sold {y} units of the product."
    if int(y) > 160:
        info_text.status = "success"
    elif int(y) < 50:
        info_text.status = "error"
    else:
        info_text.status = "info"
