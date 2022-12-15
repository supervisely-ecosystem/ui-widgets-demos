import os
from time import sleep

import numpy as np
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.content import StateJson, DataJson
from supervisely.app.widgets import Card, Container, Grid, LinePlot, GridPlot, Button
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

def get_y(x, increasing=False): 
    if increasing:
        return np.random.normal(loc=0.5, scale=1.0) + np.sqrt(x)
    else:
        return np.random.normal(loc=0.5, scale=1.0) - np.sqrt(x)

def get_points(size: int=10, x_counter = -1, increasing=False):
    if increasing:
        return [{"x": x + x_counter + 1, "y": get_y(x, increasing)} for x in range(size)]
    else:
        return [{"x": x + x_counter + 1, "y": get_y(x, increasing)} for x in range(size)]


grid_plot = GridPlot([
    {"title":"Box loss", "series":[{"name": "Train", "data": []}, {"name": "Val", "data": []}]},
    {"title":"Obj loss", "series":[{"name": "Train", "data": []}, {"name": "Val", "data": []}]},
    {"title":"Cls loss", "series":[{"name": "Train", "data": []}, {"name": "Val", "data": []}]},
    {"title":"Pr + Rec", "series":[{"name": "Train", "data": []}, {"name": "Val", "data": []}]},
    {"title":"mAP", "series":[{"name": "Train", "data": []}]},
    ], columns=3)

card = Card(title="Card with grid of lineplots", content=grid_plot)

generate = {'val': False, 'losses_last_x': 0, 'metrics_last_x': 0, }
button_run_generation = Button('Run losses generation (Freq = 0.1 sec)')
@button_run_generation.click
def run_losses_generation():
    print('Generation running')
    generate['val'] = True
    while generate['val']:
        grid_plot.add_scalars('Box loss', {'Train': get_y(generate["losses_last_x"])}, generate["losses_last_x"])
        grid_plot.add_scalars('Obj loss', {'Train': get_y(generate["losses_last_x"]), 'Val': get_y(generate["losses_last_x"])}, generate["losses_last_x"])
        grid_plot.add_scalars('Cls loss', {'Train': get_y(generate["losses_last_x"]), 'Val': get_y(generate["losses_last_x"])}, generate["losses_last_x"])
        grid_plot.add_scalars('Box loss', {'Train': get_y(generate["losses_last_x"]), 'Val': get_y(generate["losses_last_x"])}, generate["losses_last_x"])
        generate["losses_last_x"] += 1
        sleep(0.1)

button_run_generation2 = Button('Run metrics generation (Freq = 5 sec)')
@button_run_generation2.click
def run_metrics_generation():
    print('Generation running')
    generate['val'] = True
    while generate['val']:
        grid_plot.add_scalar('Pr + Rec/Train', get_y(generate["metrics_last_x"], increasing=True), generate["metrics_last_x"])
        grid_plot.add_scalar('mAP/Train', get_y(generate["metrics_last_x"], increasing=True), generate["metrics_last_x"])
        generate["metrics_last_x"] += 1
        sleep(5)


button_stop_generation = Button('Stop generation')
@button_stop_generation.click
def stop_generation():
    generate['val'] = False
    print('Generation stopped')

button_add_point = Button('Add point')
@button_add_point.click
def add_new_point_to_plot():
    line_plot = grid_plot._widgets['Box loss']
    series = next((series for series in DataJson()[line_plot.widget_id]['series'] if series['name'] == 'Train'), (None, None))
    if len(series['data']) > 0:
        x_max = max(series['data'], key=lambda point: point['x'])['x'] + 1
    else:
        x_max = 0
    grid_plot.add_scalar('Box loss/Train', np.random.random(), x_max)
    print(f"\nAdded new x: {x_max}\n with random value")

buttons_container = Container([button_run_generation, button_run_generation2, button_stop_generation, button_add_point], direction='horizontal')
container = Container([card, buttons_container])
app = sly.Application(layout=container)
