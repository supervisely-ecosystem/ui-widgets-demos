import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, TeamFilesSelector


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

test = TeamFilesSelector(439)

a = test.get_selected_id()

card = Card(title="Team Files Selector", content=Container([test]))
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
