import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, DatasetThumbnail

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# get project info from server
project_id = int(os.environ["modal.state.slyProjectId"])
project = api.project.get_info_by_id(project_id)
dataset_id = int(os.environ["modal.state.slyDatasetId"])
dataset = api.dataset.get_info_by_id(id=dataset_id)

# initialize widgets we will use in UI
dataset_thumbnail = DatasetThumbnail(project_info=project, dataset_info=dataset)
card = Card(
    title="Dataset Thumbnail",
    content=Container(widgets=[dataset_thumbnail]),
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
