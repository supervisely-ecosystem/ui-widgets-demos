import os
import random
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Tag

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api: sly.Api = sly.Api.from_env()

tag = Tag(text="Tag")

all_tag_types = [tag]
for tag_type in ["primary", "gray", "success", "warning", "danger"]:
    curr_tag = Tag(text=f"Tag {tag_type}", type=tag_type)
    all_tag_types.append(curr_tag)

card = Card(
    "Tag",
    content=Container(widgets=all_tag_types, direction="horizontal"),
)


layout = Container(widgets=[card, button])
app = sly.Application(layout=layout)
