from typing import List
import os
import supervisely
import supervisely as sly
from supervisely.nn.artifacts.artifacts import TrainInfo
from supervisely.app.widgets import Card, Container, ExperimentSelector, Button
from dotenv import load_dotenv

import supervisely.nn.artifacts.utils
import supervisely.nn.experiments


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

team_id = 8
workspace_id = 349

artifacts = sly.nn.artifacts.MMDetection3(team_id)
legacy_experiment_infos = artifacts.get_list_experiment_info()
experiment_infos = supervisely.nn.experiments.get_experiment_infos(api, team_id, "RT-DETRv2")
infos = experiment_infos + legacy_experiment_infos

experiment_selector = ExperimentSelector(team_id, infos)

button = Button("Button")
container = Container([experiment_selector, button])
card = Card(
    title="Experiment Selector",
    content=container,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
