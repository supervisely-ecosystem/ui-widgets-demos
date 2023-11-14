import os
import json
import pandas as pd

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import (
    Card,
    Container,
    SmartTable,
)

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

data = [["apple", "21"], ["banana", "15"]]

columns = ["Class", "Items"]

dataframe = pd.DataFrame(data=data, columns=columns)

columns_options = [
    {"type": "class"},
    {"maxValue": 21, "postfix": "pcs", "tooltip": "description text", "subtitle": "boxes"},
]

meta_path = "meta.json"
with open(meta_path, "r") as json_file:
    meta = json.load(json_file)

smart_table = SmartTable(
    data=dataframe,
    project_meta=meta,
    columns_options=columns_options,
    clickable_rows=True,
)

card = Card(
    title="Smart Table",
    content=smart_table,
)
layout = Container(widgets=[card])

app = sly.Application(layout=layout)


@smart_table.row_click
def handle_table_row(datapoint: sly.app.widgets.SmartTable.ClickedDataRow):
    sly.app.show_dialog(
        f"{datapoint.row[0]}",
        f"You clicked table row with idx={datapoint.row_index} in source data",
    )
