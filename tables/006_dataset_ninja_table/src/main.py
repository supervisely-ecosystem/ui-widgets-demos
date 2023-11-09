import os
import json

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import (
    Card,
    Container,
    DatasetNinjaTable,
)

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

data_path = "data.json"

meta_path = "meta.json"

with open(meta_path, "r") as json_file:
    meta = json.load(json_file)

ninja_table = DatasetNinjaTable(
    data=data_path,
    project_meta=meta,
    clickable_rows=True,
)

card = Card(
    title="Dataset Ninja Table",
    content=ninja_table,
)
layout = Container(widgets=[card])

app = sly.Application(layout=layout)


@ninja_table.row_click
def handle_table_row(datapoint: sly.app.widgets.DatasetNinjaTable.ClickedDataRow):
    sly.app.show_dialog(
        f"{datapoint.row[0]}",
        f"You clicked table row with idx={datapoint.row_index} in source data",
    )
