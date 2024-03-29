import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, TeamFilesSelector, Text


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

team_id = sly.env.team_id()

file_selector = TeamFilesSelector(
    team_id=team_id,
    max_height=300,
    multiple_selection=True,
    hide_header=False,
    selection_file_type="folder",
    additional_fields=["createdAt", "type", "size"],
)

text = Text()
button = Button()

card = Card(
    title="Team Files Selector",
    content=Container([file_selector, button, text]),
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@button.click
def show_selected():
    selected_paths = file_selector.get_selected_paths()
    text.text = "<br>".join(selected_paths)
