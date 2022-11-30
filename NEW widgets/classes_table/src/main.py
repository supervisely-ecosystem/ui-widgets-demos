import os
from dotenv import load_dotenv
import supervisely as sly
from supervisely.project.project_meta import ProjectMeta
from supervisely.app.widgets import Container, ClassesTable, Text, Card

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

project_id = int(os.environ["modal.state.slyProjectId"])
class_table = ClassesTable(project_id=project_id)
label = Text("")

data_dir = sly.app.get_data_dir()
project_dir = os.path.join(data_dir, 'sly_project')
sly.Project.download(api, project_id, project_dir)
project = sly.Project(project_dir, sly.OpenMode.READ)
local_class_table =  ClassesTable(project_fs=project)
local_label = Text("")

card = Card(
    title="Classes Table",
    content=Container([class_table, label], gap=5)
)
card_local = Card(
    title="Classes Table Local",
    content=Container([local_class_table, local_label], gap=5)
)
layout = Container(widgets=[card, card_local])

app = sly.Application(
    layout=layout
)


@class_table.value_changed
def class_table_value_changed(selected_classes):
    label.text = f"Selected classes: {', '.join(selected_classes)}"


@local_class_table.value_changed
def class_table_value_changed(selected_classes):
    local_label.text = f"Selected classes: {', '.join(selected_classes)}"
