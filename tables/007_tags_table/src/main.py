import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, TagsTable, Text

# for convenient debug, has no effect in production
if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

project_id = 38857
tags_table = TagsTable(project_id=project_id)
tags_text = Text("Selected tags: ")
card = Card(title="TagsTable", content=Container([tags_table, tags_text]))
app = sly.Application(layout=card)

@tags_table.value_changed
def display_selected_tags(value):
    tags_text.text = f"Selected tags: {', '.join(value)}"