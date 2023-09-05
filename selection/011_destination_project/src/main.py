import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, DestinationProject, Text

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api: sly.Api = sly.Api.from_env()

workspace_id = sly.env.workspace_id()

destination = DestinationProject(workspace_id=workspace_id, project_type=sly.ProjectType.IMAGES)


button = Button()
text_project_id = Text()
text_project_name = Text()
text_dataset_id = Text()
text_dataset_name = Text()

container = Container(
    widgets=[
        button,
        text_project_id,
        text_project_name,
        text_dataset_id,
        text_dataset_name,
    ]
)

card = Card(
    "Destination Project",
    content=Container([destination, container]),
)


layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@button.click
def get_destination():
    text_project_id.text = f"project_id: {destination.get_selected_project_id()}"
    text_project_name.text = f"project_name: {destination.get_project_name()}"
    text_dataset_id.text = f"dataset_id: {destination.get_selected_dataset_id()}"
    text_dataset_name.text = f"dataset_name: {destination.get_dataset_name()}"
