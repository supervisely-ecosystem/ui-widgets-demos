import os
import random
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, ElementTag

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api: sly.Api = sly.Api.from_env()

all_tag_types = [ElementTag(text="Tag")]
for tag_type in ["primary", "gray", "success", "warning", "danger"]:
    curr_tag = ElementTag(text=f"Tag {tag_type}", type=tag_type, hit=True)
    all_tag_types.append(curr_tag)


card = Card(
    "ElementTag",
    content=Container(widgets=[all_tag_types], direction="horizontal"),
)


layout = Container(widgets=[card])
app = sly.Application(layout=layout)
