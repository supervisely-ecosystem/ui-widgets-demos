import os
import random
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, ElementTag, Button

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api: sly.Api = sly.Api.from_env()

el_tag = ElementTag(text="Tag")

# button = Button()

all_tag_types = [el_tag]
for tag_type in ["primary", "gray", "success", "warning", "danger"]:
    curr_tag = ElementTag(
        text=f"Tag {tag_type}", type=tag_type, closable=True, close_transition=True
    )
    all_tag_types.append(curr_tag)

card = Card(
    "ElementTag",
    content=Container(widgets=all_tag_types, direction="horizontal"),
)


layout = Container(widgets=[card])
app = sly.Application(layout=layout)


# @tag.close_tag
# def taggg(res):
#     info = res
#     a = 0
