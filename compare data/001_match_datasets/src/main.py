import os
import supervisely as sly
from supervisely.app.widgets import Card, Container, MatchDatasets
from dotenv import load_dotenv


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

project_id1 = 17198
project_id2 = 17199

datasets_left = api.dataset.get_list(project_id1)
datasets_right = api.dataset.get_list(project_id2)

match_datasets = MatchDatasets(
    left_datasets=datasets_left,
    right_datasets=datasets_right,
)


card = Card(
    title="Match Datasets",
    content=match_datasets,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
