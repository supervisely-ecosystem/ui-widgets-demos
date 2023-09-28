import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, LineChart, Text

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

series = [
    {"name": "Team A", "data": 44},
    {"name": "Team B", "data": 55},
    {"name": "Team C", "data": 13},
    {"name": "Team D", "data": 43},
    {"name": "Team E", "data": 22},
]

pie_chart = LineChart(
    title="Simple Pie",
    series=series,
    stroke_curve="smooth",  # smooth or straight do nothing??
    stroke_width=1,  # width between slices
    data_labels=True,  # shows values on slices
    type="pie",  # pie or donut
    height=350,  # height of piechart
)

text = Text("Click on the slice to see it's value", status="info")
container = Container(widgets=[pie_chart, text])
card = Card(title="Pie Chart", content=container)
app = sly.Application(layout=card)


@pie_chart.click
def show_selection(slice: LineChart.ClickedSlice):
    selected_area = slice
    text.set(text=f"Selected area: {selected_area}", status="info")
