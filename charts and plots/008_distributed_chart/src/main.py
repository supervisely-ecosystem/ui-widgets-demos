import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import DistributedChart, Card, Text, Container

load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))
api = sly.Api()

# Colors are optional. If not specified, the default colors will be used.
colors = [
    "#008FFB",
    "#00E396",
    "#FEB019",
]
dc = DistributedChart(title="Distributed Chart", colors=colors)

# Both lists must have the same length, otherwise ValueError will be raised.
# Values should be int or float.
names = ["cats", "dogs", "birds", "fish", "snakes"]
values = [10, 4, 35, 12, 5]

# Setting new series to the chart (aware that it will delete all previous series if they existed)
dc.set_series(names, values)

clicked_datapoint = Text(status="info")


@dc.click
def clicked(datapoint):
    # Datapoint is a namedtuple with fields: series_index, data_index, data
    # data is a dict with fields: name, value
    clicked_datapoint.text = datapoint


# Creating Card widget, which will contain the Transfer widget and the Text widget.
card = Card(title="DistributedChart", content=Container(widgets=[dc, clicked_datapoint]))
# Creating the application layout.
layout = Container(widgets=[card])

app = sly.Application(layout=layout)
