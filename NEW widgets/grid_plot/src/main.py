import os
from time import sleep

import numpy as np
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.content import StateJson, DataJson
from supervisely.app.widgets import Card, Container, LinePlot, GridPlot, Button
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

def get_points(size: int=10, x_counter = -1, increasing=False):
    if increasing:
        return [{"x": x + x_counter + 1, "y": np.random.normal(loc=0.5, scale=1.0) + np.sqrt(x + x_counter + 1)} for x in range(size)]
    else:
        return [{"x": x + x_counter + 1, "y": np.random.normal(loc=0.5, scale=1.0) - np.sqrt(x + x_counter + 1)} for x in range(size)]



line_plot_1 = LinePlot(
    title="Box loss",
    series=[{"name": "Train", "data": []}, {"name": "Val", "data": []}],
)
line_plot_2 = LinePlot(
    title="Obj loss",
    series=[{"name": "Train", "data": []}, {"name": "Val", "data": []}],
)
line_plot_3 = LinePlot(
    title="Cls loss",
    series=[{"name": "Train", "data": []}, {"name": "Val", "data": []}],
)
line_plot_4 = LinePlot(
    title="PR + Rec",
    series=[{"name": "Train", "data": []}, {"name": "Val", "data": []}],
)
line_plot_5 = LinePlot(
    title="mAP",
    series=[{"name": "Train", "data": []}, {"name": "Val", "data": []}],
)

grid_plot = GridPlot(widgets=[line_plot_1, line_plot_2, line_plot_3, line_plot_4, line_plot_5], columns=3)
card = Card(title="Card with grid of lineplots", content=grid_plot)

generate = {'val': False}
button_run_generation = Button('Run series generation for 1 and 4 chart (0.1 sec)')
@button_run_generation.click
def add_new_point_to_series():
    print('Generation running')
    generate['val'] = True
    while generate['val']:
        for line_plot in (line_plot_1, line_plot_2, line_plot_3):
            for series in DataJson()[line_plot.widget_id]['series']:
                if len(series['data']) > 0:
                    x_max = max(series['data'], key=lambda point: point['x'])['x']
                else:
                    x_max = 0
                line_plot.add_to_series(name_or_id=series['name'], data=get_points(1, x_counter=x_max, increasing=False))
        sleep(0.1)

generate2 = {'val': False}
button_run_generation2 = Button('Run series generation for 2 and 3 chart (5 sec)')
@button_run_generation2.click
def add_new_point_to_series():
    print('Generation running')
    generate2['val'] = True
    while generate2['val']:
        for line_plot in (line_plot_4, line_plot_5):
            for series in DataJson()[line_plot.widget_id]['series']:
                if len(series['data']) > 0:
                    x_max = max(series['data'], key=lambda point: point['x'])['x']
                else:
                    x_max = 0
                line_plot.add_to_series(name_or_id=series['name'], data=get_points(1, x_counter=x_max, increasing=True))
        sleep(5)

button_stop_generation = Button('Stop series generation')
@button_stop_generation.click
def add_new_point_to_series():
    generate['val'] = False
    generate2['val'] = False
    print('Generation stopped')

buttons_container = Container([button_run_generation, button_run_generation2, button_stop_generation], direction='horizontal')
container = Container([card, buttons_container])
app = sly.Application(layout=container)
