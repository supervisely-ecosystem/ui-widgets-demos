import os

from dotenv import load_dotenv
import supervisely as sly
from supervisely.app.widgets import Button, Card, Container
from supervisely.app.widgets import FileStorageUpload, Input, Text, MessageBox

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

# app requires TASK_ID in local.env

api = sly.Api()

# team_id = sly.env.team_id()

# file_upload = FileStorageUpload(team_id=team_id, path="folder")

# input = Input(placeholder="Please enter path")
# button_change_path = Button("Change path name")
# button_get_paths = Button("Get upoaded paths")

# text = Text()

# btn_container = Container(
#     [button_change_path, button_get_paths],
#     direction="horizontal",
# )
# controls_container = Container([input, btn_container, text])

message_box = MessageBox()

card = Card(
    title="MessageBox",
    content=Container([message_box]),
)

layout = Container(widgets=[card])

app = sly.Application(layout=layout)
