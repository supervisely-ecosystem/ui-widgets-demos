import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import (
    Button,
    Card,
    Container,
    Flexbox,
    Input,
    InputNumber,
    PieChart,
    Text,
)

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

pie_chart = PieChart(
    title="Simple Pie",
    series=series,
    stroke_width=1,
    data_labels=True,
    height=350,
    type="pie",
)

text = Text("Click on the slice to see it's value", status="info")
container_chart = Container(widgets=[pie_chart, text])


input_name = Input(value="Team F", maxlength=10)
input_value = InputNumber(value=10)
button_add = Button("Add slice")
button_set = Button("Set slice")
button_remove = Button("Delete selected slice", "danger")
button_remove.disable()

buttons_flex = Flexbox(widgets=[button_add, button_set, button_remove])
container_add = Container(widgets=[input_name, input_value, buttons_flex])
main_container = Container(widgets=[container_chart, container_add])
card = Card(title="Pie Chart", content=main_container)
layout = card
app = sly.Application(layout=layout)


@pie_chart.click
def show_selection(datapoint: PieChart.ClickedDataPoint):
    data_name = datapoint.data["name"]
    data_value = datapoint.data["value"]
    data_index = datapoint.data_index
    text.set(f"Selected slice: {data_name}, Value: {data_value}, Index: {data_index}", "info")
    button_remove.enable()


@button_add.click
def add_slice():
    name = input_name.get_value()
    value = input_value.get_value()
    pie_chart.add_series(names=[name], values=[value])


@button_set.click
def set_slice():
    name = input_name.get_value()
    value = input_value.get_value()
    pie_chart.set_series(names=[name], values=[value])


@button_remove.click
def remove_slice():
    datapoint: PieChart.ClickedDataPoint = pie_chart.get_clicked_datapoint()
    datapoint.data_index
    pie_chart.delete_series(datapoint.data_index)
    button_remove.disable()
