import os

import numpy as np
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Grid, LinePlot, GridPlot

load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

def get_points(size: int=10):
    x = list(range(size))
    y = sorted(np.random.exponential(scale=0.7, size=size).tolist(), reverse=True)
    return [{"x": x_, "y": y_} for x_, y_ in zip(x, y)]

line_chart = LinePlot(
    title="Model losses",
    series=[{"name": "Train loss", "data": get_points(10)}, {"name": "Test loss", "data": get_points(15)}],
)
card1 = Card(title="Card with line plot", content=line_chart)


grid_plot2 = GridPlot(widgets=[
    LinePlot(
        title="Model losses 1",
        series=[{"name": "Train loss", "data": get_points(10)}, {"name": "Test loss", "data": get_points(15)}],
    ), 
    LinePlot(
        title="Model losses 2",
        series=[{"name": "Train loss", "data": get_points(10)}, {"name": "Test loss", "data": get_points(15)}],
    ),
    LinePlot(
        title="Model losses 3",
        series=[{"name": "Train loss", "data": get_points(10)}, {"name": "Test loss", "data": get_points(15)}],
    ),
    LinePlot(
        title="Model losses 4",
        series=[{"name": "Train loss", "data": get_points(10)}, {"name": "Test loss", "data": get_points(15)}],
    ),
    ], 
    columns=2)
card2 = Card(title="Card with 2 columns grid for the 4 line plots", content=grid_plot2)


grid_plot3 = GridPlot(widgets=[
    LinePlot(
        title="Model losses 1",
        series=[{"name": "Train loss", "data": get_points(10)}, {"name": "Test loss", "data": get_points(15)}],
    ), 
    LinePlot(
        title="Model losses 2",
        series=[{"name": "Train loss", "data": get_points(10)}, {"name": "Test loss", "data": get_points(15)}],
    ),
    LinePlot(
        title="Model losses 3",
        series=[{"name": "Train loss", "data": get_points(10)}, {"name": "Test loss", "data": get_points(15)}],
    ),
    LinePlot(
        title="Model losses 4",
        series=[{"name": "Train loss", "data": get_points(10)}, {"name": "Test loss", "data": get_points(15)}],
    ),
    LinePlot(
        title="Model losses 5",
        series=[{"name": "Train loss", "data": get_points(10)}, {"name": "Test loss", "data": get_points(15)}],
    ),
    LinePlot(
        title="Model losses 6",
        series=[{"name": "Train loss", "data": get_points(10)}, {"name": "Test loss", "data": get_points(15)}],
    ),
    LinePlot(
        title="Model losses 7",
        series=[{"name": "Train loss", "data": get_points(10)}, {"name": "Test loss", "data": get_points(15)}],
    ),
    ], 
    columns=3)
card3 = Card(title="Card with 3 columns grid for 7 line plots", content=grid_plot3)

container = Container(widgets=[card1, card2, card3])
app = sly.Application(layout=container)
