import os
from supervisely.app.widgets import Card, Container, Select

import supervisely as sly
from dotenv import load_dotenv

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

project_id = int(os.environ["modal.state.slyProjectId"])
project_meta_json = api.project.get_meta(id=project_id)
project_meta = sly.ProjectMeta.from_json(data=project_meta_json)

dataset_id = int(os.environ["modal.state.slyDatasetId"])

# initialize widgets we will use in UI
animals_domestic = [
    Select.Item(value="cat", label="cat"),
    Select.Item(value="dog", label="dog"),
    Select.Item(value="horse", label="horse"),
    Select.Item(value="sheep", label="sheep"),
]

animals_wild = [
    Select.Item(value="squirrel", label="squirrel"),
]

select_items = Select(
    items=animals_domestic + animals_wild,
    filterable=True,
)

groups = [
    Select.Group(label="domestic", items=animals_domestic),
    Select.Group(label="wild", items=animals_wild),
]

select_groups = Select(groups=groups)

card = Card(
    title="Select",
    content=Container(widgets=[select_items, select_groups]),
)

layout = Container(widgets=[card])
app = sly.Application(layout=layout)
