import os
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import FileViewer, Container, Card, Text

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
team_id = int(os.environ["modal.state.slyTeamId"])

path = "/"  # root of Team Files or specify your directory

files = api.file.list(team_id, path)
tree_items = []
for file in files:
    path = file["path"]
    tree_items.append({"path": path, "size": file["meta"]["size"]})


file_viewer = FileViewer(files_list=tree_items)
selected_values = Text()
curr_path = Text()

layout = Card(
    content=Container(widgets=[curr_path, selected_values, file_viewer]), title="File Viewer"
)
app = sly.Application(layout=layout)


@file_viewer.path_changed
def refresh_tree(current_path):
    curr_path.set(text=f"Current path: {current_path}", status="text")


@file_viewer.value_changed
def print_selected(selected_items):
    selected_values.set(text=f"Selected items: {', '.join(selected_items)}", status="text")
