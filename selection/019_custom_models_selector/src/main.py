import os
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, CustomModelsSelector, Container, Text, Button


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

team_id = sly.env.team_id()


train_infos = sly.nn.artifacts.YOLOv8(team_id).get_list()
trained_models_table = CustomModelsSelector(
    team_id,
    train_infos,
    show_custom_checkpoint_path=True,
    custom_checkpoint_task_types=["object detection", "instance segmentation", "pose estimation"],
)

model_name_preview = Text("", "text")
model_path_preview = Text("", "text")
model_task_type_preview = Text("", "text")
preview_container = Container([model_name_preview, model_path_preview, model_task_type_preview])
preview_container.hide()
preview_button = Button("Show preview")

container = Container([trained_models_table, preview_button, preview_container])
card = Card(title="TrainedModelsTable", content=container)
layout = card

app = sly.Application(layout=card)


@trained_models_table.value_changed
def get_selected_row(row: CustomModelsSelector.ModelRow):
    preview_container.hide()


@preview_button.click
def preview_button_click_handler():
    preview_container.hide()
    if not trained_models_table.use_custom_checkpoint_path():
        row = trained_models_table.get_selected_row()
        model_name = row.get_selected_checkpoint_name()
        model_path = row.get_selected_checkpoint_path()
        model_task_type = row.task_type
    else:
        model_path = trained_models_table.get_custom_checkpoint_path()
        model_name = trained_models_table.get_custom_checkpoint_name()
        model_task_type = trained_models_table.get_custom_checkpoint_task_type()

    model_name_preview.set(f"Model name: {model_name}", "text")
    model_path_preview.set(f"Model path: {model_path}", "text")
    model_task_type_preview.set(f"Model task type: {model_task_type}", "text")
    preview_container.show()
