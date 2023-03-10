import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, TaskLogs


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))


api = sly.Api()

task_id = 28628

test = TaskLogs(task_id=task_id)

card = Card(title="Task Logs", content=Container([test]))
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
