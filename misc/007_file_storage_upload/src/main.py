import os

from dotenv import load_dotenv
import supervisely as sly
from supervisely.app.widgets import Button, Card, Container
from supervisely.app.widgets import FileStorageUpload, Input, Text

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

team_id = sly.env.team_id()

file_upload = FileStorageUpload(path="folder")

input = Input(placeholder="Please enter path")
button_change_path = Button("Change path name")
button_get_paths = Button("Get upoaded paths")

text = Text()

btn_container = Container(
    [button_change_path, button_get_paths],
    direction="horizontal",
)
controls_container = Container([input, btn_container, text])

card = Card(
    title="Image Preview",
    content=Container([file_upload, controls_container]),
)

layout = Container(widgets=[card])

app = sly.Application(layout=layout)


@button_change_path.click
def change_path():
    path = input.get_value()
    file_upload.set_path(path)
    text.status = "success"
    text.text = "Upload path has been changed."


@button_get_paths.click
def show_uploaded_paths():
    paths = file_upload.get_uploaded_paths()
    text.status = "text"
    text.text = "<br>".join(paths)
