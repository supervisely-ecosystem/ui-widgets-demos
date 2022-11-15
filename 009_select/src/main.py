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
anns_infos = api.annotation.get_list(dataset_id=dataset_id)
anns_jsons = [ann_info.annotation for ann_info in anns_infos]
anns = [
    sly.Annotation.from_json(data=ann_json, project_meta=project_meta)
    for ann_json in anns_jsons
]

# initialize widgets we will use in UI
select = Select(
    items=anns,
    filterable=True,
)
card = Card(
    title="Select",
    content=Container(widgets=[select]),
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
