import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, TagsTable

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

project_id = 36160
tags_table = TagsTable(project_id=project_id)
card = Card(title="TagsTable", content=tags_table)
app = sly.Application(layout=card)


# @agent_selector.value_changed
# def get_agent_id(id):
#     print(id)
