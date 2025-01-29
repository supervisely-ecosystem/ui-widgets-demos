import os
import supervisely as sly
from supervisely.app.widgets import Card, Container, RunAppButton, Button
from dotenv import load_dotenv

load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely_umar.env"))

api = sly.Api()

workspace_id = 211
module_id = 252
payload = {}


tensorboard_button = Button(
    "Open Tensorboard",
    button_type="info",
    plain=True,
    icon="zmdi zmdi-chart",
    visible_by_vue_field="!isStaticVersion",
)

run_app_button = RunAppButton(
    text="Open Tensorboard",
    button_type="info",
    button_size="l",
    plain=True,
    icon="zmdi zmdi-chart",
    workspace_id=workspace_id,
    module_id=module_id,
    payload=payload,
    available_in_offline=False,
    visible_by_vue_field="",
)

container = Container([tensorboard_button, run_app_button])

card = Card(
    title="Run App Button",
    content=container,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
