import os
import supervisely as sly
from supervisely.app.widgets import Card, Container, PretrainedModelsSelector
from dotenv import load_dotenv

from misc.pretrained_models_selector.src.models import models

load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()


team_id = sly.env.team_id()
workspace_id = sly.env.workspace_id()
project_id = sly.env.project_id()

# parse data to create task type and arch type selectors
model_selector = PretrainedModelsSelector(models)
model_selector.set_models(models[:3])
model_selector.disable()


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
