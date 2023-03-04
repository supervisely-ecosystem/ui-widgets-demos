import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, TabsDynamic


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

yaml_path = "misc/tabs_dynamic/src/yaml"
tabs_dynamic = TabsDynamic(yaml_path)

card = Card(title="TabsDynamic", content=Container([tabs_dynamic]))
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
