import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, ModelStats

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

session_id = int(os.environ["context.sessionId"])

# initialize widgets we will use in UI
model_stats = ModelStats()
model_stats.set_session_id(session_id=session_id)

card = Card(
    title="",
    content=Container(widgets=[model_stats]),
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
