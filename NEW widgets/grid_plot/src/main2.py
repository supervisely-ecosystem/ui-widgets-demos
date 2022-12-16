import os
import asyncio
import concurrent
from time import sleep

import numpy as np
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.content import StateJson, DataJson
from supervisely.app.widgets import Card, Container, Grid, LinePlot, GridPlot, Button
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
executor = concurrent.futures.ThreadPoolExecutor()
loop = asyncio.get_event_loop()

def get_pseudo_random(x, increasing=False): 
    if increasing:
        return np.random.normal(loc=0.5, scale=1.0) + np.sqrt(x)
    else:
        return np.random.normal(loc=0.5, scale=1.0) - np.sqrt(x)

plots_config = [
    {"title":"Box loss", "show_legend": False}, 
    {"title":"Obj loss", "show_legend": True}, 
    {"title":"Cls loss", "show_legend": False}, 
    {"title":"Pr + Rec", "show_legend": True}, 
    {"title":"mAP", "show_legend": False}
]
generate = False #  just flag for control plot points generation 
losses_x =  0 # last value for x-axis of losses plots
metrics_x = 0  # last value for x-axis of metrics plots
grid_plot = GridPlot(plots_config, columns=3)

def long_task():
    print('Generation running')
    global generate, losses_x
    generate = True
    while generate:
        for plot_title in ('Box loss', 'Obj loss', 'Cls loss', 'Box loss'):
            grid_plot.add_scalars(plot_title, {'Train': get_pseudo_random(losses_x), 'Val': get_pseudo_random(losses_x)}, losses_x)
        losses_x += 1
        sleep(0.1)

def callback(future):
    if future.exception():
        print(repr(future.exception()))
    else:
        print(future.result())
    button_run_generation.loading = False

button_run_generation = Button('Run losses generation (Freq = 0.1 sec)')
@button_run_generation.click
def run_losses_generation():
    print('Generation running')
    my_future = loop.run_in_executor(executor, long_task)
    task = asyncio.ensure_future(my_future, loop=loop)
    task.add_done_callback(callback)

button_run_generation2 = Button('Run metrics generation (Freq = 5 sec)')
@button_run_generation2.click
def run_metrics_generation():
    print('Generation running')
    global generate, metrics_x
    generate = True
    while generate:
        for plot_title in ('Pr + Rec/Train', 'mAP/Train'):
            grid_plot.add_scalar(plot_title, get_pseudo_random(metrics_x, increasing=True), metrics_x)
        metrics_x += 1
        sleep(5)

button_stop_generation = Button('Stop generation')
@button_stop_generation.click
def stop_generation():
    global generate
    generate = False
    print('Generation stopped')

card = Card(title="Card with grid of lineplots", content=grid_plot)
buttons_container = Container([button_run_generation, button_run_generation2, button_stop_generation], direction='horizontal')
container = Container([card, buttons_container])
app = sly.Application(layout=container)
