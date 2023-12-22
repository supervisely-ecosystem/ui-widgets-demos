import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, TrainedModelsTable, Select

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# remote_path_to_custom_models = "/yolov8_train/object detection/ANIMALS SMALL/38881/weights/best_0.pt"
remote_path_to_custom_models = "/yolov8_train/"

trained_models_table = TrainedModelsTable(8, remote_path_to_custom_models, "instance segmentation")

card = Card(title="TrainedModelsTable", content=trained_models_table)
app = sly.Application(layout=card)

a = trained_models_table.get_selected_row()
b = trained_models_table.get_selected_row_index()


@trained_models_table.value_changed
def get_selected_row(row: TrainedModelsTable.ModelRow):
    selector_val = row.artifacts_selector.get_value()
    selector_lab = row.artifacts_selector.get_label()
