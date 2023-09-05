import os

from dotenv import load_dotenv
import supervisely as sly
from supervisely.app.widgets import Button, Card, Container, Field
from supervisely.app.widgets import FileStorageUpload, Flexbox, Input, Text

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

# NOTE: app requires to define TASK_ID for active app session for current team

api = sly.Api()

team_id = sly.env.team_id()

file_upload_1 = FileStorageUpload(
    team_id=team_id,
    path="folder",
)

upload_1 = Field(
    title="Existing directory",
    description="Upload files/folders to an existing directory in Team files",
    content=file_upload_1,
)


file_upload_2 = FileStorageUpload(
    team_id=team_id,
    path="folder",
    change_name_if_conflict=True,
)

upload_2 = Field(
    title="New path",
    description="Enter a new path and set it by clicking on button",
    content=file_upload_2,
)


input = Input(placeholder="Please enter path")
button_change_path = Button("Change path name")
button_get_paths_1 = Button("Get upoaded paths")
button_get_paths_2 = Button("Get upoaded paths")

text = Text()

upload_container = Container([upload_1, upload_2])
btns_box = Flexbox([button_change_path, button_get_paths_1, button_get_paths_2])
controls_container = Container([input, btns_box, text])

card = Card(
    title="File Storage Upload",
    content=Container([upload_container, controls_container]),
)

layout = Container(widgets=[card])

app = sly.Application(layout=layout)


@button_change_path.click
def change_path():
    path = input.get_value()
    file_upload_2.set_path(path)
    file_upload_1.set_path(path)
    text.status = "success"
    text.text = "Upload path has been changed."


@button_get_paths_1.click
def show_uploaded_paths():
    paths = file_upload_1.get_uploaded_paths()
    text.status = "text"
    text.text = "<br>".join(paths)


@button_get_paths_2.click
def show_uploaded_paths():
    paths = file_upload_2.get_uploaded_paths()
    text.status = "text"
    text.text = "<br>".join(paths)
