import os

import supervisely as sly
from dotenv import load_dotenv
from typing import List

from supervisely.app.widgets import SelectDatasetTree, Card, Container


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))
api = sly.Api()

project_id = 39396
default_id = 93446

select_dataset_tree = SelectDatasetTree(
    project_id=project_id, default_id=default_id, multiselect=True, flat=True
)

# Creating Card widget, which will contain all the widgets.
card = Card(
    title="SelectDatasetTree",
    content=Container(widgets=[select_dataset_tree]),
)

# Creating the application layout.
layout = Container(widgets=[card])
# Initializing the application.
app = sly.Application(layout=layout)


@select_dataset_tree.value_changed
def on_change(dataset_ids: List[int]) -> None:
    print(f"Selected dataset ids: {dataset_ids}")
