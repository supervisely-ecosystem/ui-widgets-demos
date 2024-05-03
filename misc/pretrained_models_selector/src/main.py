import os
import supervisely as sly
from supervisely.app.widgets import Card, Container, PretrainedModelsSelector
from dotenv import load_dotenv

from misc.pretrained_models_selector.src.models_mmdet import models as mmdet_models
from misc.pretrained_models_selector.src.models_yolov8 import models as yolov8_models

load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()


team_id = sly.env.team_id()
workspace_id = sly.env.workspace_id()
project_id = sly.env.project_id()

# parse data to create task type and arch type selectors
model_selector = PretrainedModelsSelector(mmdet_models)
# model_selector.set_models()
# model_selector.disable()


card = Card(
    title="Project Selector",
    content=model_selector,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@model_selector.arch_type_changed
def arch_type_changed(arch_type):
    print(f"arch_type_changed: {arch_type}")


@model_selector.task_type_changed
def task_type_changed(task_type):
    print(f"task_type_changed: {task_type}")


@model_selector.model_changed
def model_changed(model):
    print(f"model_changed: {model}")

    model_row = model_selector.get_selected_row()

    task_type = model_selector.get_selected_task_type()
    arch_type = model_selector.get_selected_arch_type()

    config_url = model_row["meta"]["config_url"]
    checkpoint_url = model_row["meta"]["weights_url"]
    checkpoint_filename = model_row["Model"]

    model_params = {
        "model_source": "Pretrained models",
        "task_type": task_type,
        "checkpoint_name": checkpoint_filename,
        "checkpoint_url": checkpoint_url,
        "arch_type": arch_type,
        "config_url": config_url,
    }
