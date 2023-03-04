import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, TrainValSplits, Button, Text


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

project_id = int(os.environ["modal.state.slyProjectId"])
project_info = api.project.get_info_by_id(project_id)
project_dir = os.path.join(sly.app.get_data_dir(), project_info.name)
sly.fs.remove_dir(project_dir)
sly.Project.download(api, project_id, project_dir)
project_fs = sly.Project(project_dir, sly.OpenMode.READ)

# initialize widgets we will use in UI
splits = TrainValSplits(project_fs=project_fs)
button = Button("Get splits")
text = Text("")
text.hide()

card = Card(title="Train Val Splits", content=Container([splits, button, text], gap=5))
layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@button.click
def get_splits():
    train_set, val_set = splits.get_splits()
    text.text = f"Train split: {len(train_set)} images, Val split: {len(val_set)} images"
    text.show()
