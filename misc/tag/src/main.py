import os
import random
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Tag, Button

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api: sly.Api = sly.Api.from_env()

tag = Tag(text="Tag")

button = Button(text="Change Color")

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


@button.click
def change_color():
    colors = ["orange", "purple", "black", "blue", "green"]
    for tag in all_tag_types:
        tag.set_color(random.choice(colors))
