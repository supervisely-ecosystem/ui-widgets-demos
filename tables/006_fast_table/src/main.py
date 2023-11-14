import os
import json
import pandas as pd

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import (
    Card,
    Container,
    FastTable,
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

meta_path = "./tables/006_fast_table/src/meta.json"
with open(meta_path, "r") as json_file:
    meta = json.load(json_file)

fast_table = FastTable(
    data=data,
    columns=columns,
    project_meta=meta,
    columns_options=columns_options,
)

card = Card(
    title="Fast Table",
    content=fast_table,
)
layout = Container(widgets=[card])

app = sly.Application(layout=layout)


@fast_table.row_click
def handle_table_row(clicked_row: sly.app.widgets.FastTable.ClickedRow):
    sly.app.show_dialog(
        f"{clicked_row.row[0]}",
        f"You clicked table row with idx={clicked_row.row_index} in source data",
    )
