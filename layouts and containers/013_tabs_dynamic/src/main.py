import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, TabsDynamic


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

yaml_path = "layouts and containers/013_tabs_dynamic/yaml/file_1.yaml"

# initialize widget TabsDynamic we will use in UI
tabs_dynamic = TabsDynamic(yaml_path)

card = Card(title="TabsDynamic", content=Container([tabs_dynamic]))
layout = Container(widgets=[card])

app = sly.Application(layout=layout)
