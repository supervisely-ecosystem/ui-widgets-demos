import os
import supervisely as sly
from supervisely.app.widgets import Card, Container, MatchDatasets
from dotenv import load_dotenv


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

dataset_left_id = int(os.environ["modal.state.slyDatasetId_left"])
dataset_left = api.dataset.get_info_by_id(id=dataset_left_id)

dataset_right_id = int(os.environ["modal.state.slyDatasetId_right"])
dataset_right = api.dataset.get_info_by_id(id=dataset_right_id)

dataset_left_id2 = int(os.environ["modal.state.slyDatasetId_left2"])
dataset_left2 = api.dataset.get_info_by_id(id=dataset_left_id2)

dataset_right_id2 = int(os.environ["modal.state.slyDatasetId_right2"])
dataset_right2 = api.dataset.get_info_by_id(id=dataset_right_id2)

dataset_left_id3 = int(os.environ["modal.state.slyDatasetId_left3"])
dataset_left3 = api.dataset.get_info_by_id(id=dataset_left_id3)

dataset_right_id3 = int(os.environ["modal.state.slyDatasetId_right3"])
dataset_right3 = api.dataset.get_info_by_id(id=dataset_right_id3)

match_datasets = MatchDatasets(
    left_datasets=[dataset_left, dataset_left2, dataset_left3],
    right_datasets=[dataset_right, dataset_right2, dataset_right3],
)


card = Card(
    title="Match Datasets",
    content=match_datasets,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
