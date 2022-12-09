import os
import uuid
from time import sleep

import numpy as np
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Container, Card, LinePlot, Button

load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

def get_points(size: int=10, x_counter = -1, increasing=False):
    if increasing:
        return [{"x": x + x_counter + 1, "y": np.random.normal(loc=0.5, scale=1.0) + np.sqrt(x + x_counter + 1)} for x in range(size)]
    else:
        return [{"x": x + x_counter + 1, "y": np.random.normal(loc=0.5, scale=1.0) - np.sqrt(x + x_counter + 1)} for x in range(size)]

line_chart1 = LinePlot(
    title="Model losses",
    series=[{"name": "Train loss", "data": get_points(100)}, {"name": "Test loss", "data": get_points(90)}],
)

button_add = Button('Add random series')
@button_add.click
def series_add():
    id = str(uuid.uuid4()).split("-")[0]
    x, y = list(zip(*[[*xy.values()] for xy in get_points(100)]))
    line_chart1.add_series(f"New series {id}", x, y)

button_add_many_series = Button('Add series batch')
@button_add_many_series.click
def series_add_batch():
    new_series = []
    for i in range(3):
        id = str(uuid.uuid4()).split("-")[0]
        x, y = list(zip(*[[*xy.values()] for xy in get_points(100)]))
        new_series.append(dict(name=f"New series {id}", x=x, y=y))

    line_chart1.add_series_batch(new_series)

manage_container1 = Container([button_add, button_add_many_series], direction='horizontal')
container1 = Container(widgets=[line_chart1, manage_container1])
card1 = Card(title="Card with line plot", content=container1)



generate = {'val': True}
line_chart2 = LinePlot(
    title="Model accuracy",
    series=[{"name": "Accuracy", "data": get_points(2)}],
)

button_run_generation = Button('Run series generation')
@button_run_generation.click
def add_new_point_to_series():
    print('Generation running')
    series_id, series_data = line_chart2.get_series_by_name(name="Accuracy")
    x_max = max(series_data['data'], key=lambda point: point['x'])['x']
    generate['val'] = True
    while generate['val']:
        line_chart2.add_to_series(name_or_id=series_id, data=get_points(1, x_counter=x_max, increasing=True))
        x_max += 1
        sleep(0.1)

button_stop_generation = Button('Stop series generation')
@button_stop_generation.click
def add_new_point_to_series():
    generate['val'] = False
    print('Generation stopped')

button_print_random = Button('Print random')
@button_print_random.click
def add_new_point_to_series():
    print(f"random: {uuid.uuid4()}")


manage_container2 = Container([button_run_generation, button_stop_generation, button_print_random], direction='horizontal')
container2 = Container(widgets=[line_chart2, manage_container2])
card2 = Card(title="Another card with line plot", content=container2)

container3 = Container(widgets=[card1, card2])
app = sly.Application(layout=container3)
