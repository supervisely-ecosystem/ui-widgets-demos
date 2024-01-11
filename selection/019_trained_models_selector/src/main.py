import os
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, TrainedModelsSelector, Container, Text, Button


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

team_id = sly.env.team_id()


checkpoint_infos = sly.nn.checkpoints.yolov8.get_list(api, team_id)
trained_models_table = TrainedModelsSelector(team_id, checkpoint_infos)

model_name_preview = Text("", "text")
model_path_preview = Text("", "text")
preview_container = Container([model_name_preview, model_path_preview])
preview_container.hide()
preview_button = Button("Show preview")

container = Container([trained_models_table, preview_button, preview_container])
card = Card(title="TrainedModelsTable", content=container)
layout = card

app = sly.Application(layout=card)


@trained_models_table.value_changed
def get_selected_row(row: TrainedModelsSelector.ModelRow):
    preview_container.hide()


@preview_button.click
def preview_button_click_handler():
    preview_container.hide()
    row = trained_models_table.get_selected_row()
    model_name = row.get_selected_checkpoint_name()
    model_path = row.get_selected_checkpoint_path()

    model_name_preview.set(f"Model name: {model_name}", "text")
    model_path_preview.set(f"Model path: {model_path}", "text")
    preview_container.show()
