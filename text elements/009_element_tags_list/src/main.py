import os
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, ElementTagsList

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api: sly.Api = sly.Api.from_env()


el_tag = ElementTagsList.Tag(text="Tag")
all_tag_types = [el_tag]
for tag_type in ["primary", "gray", "success", "warning", "danger"]:
    curr_tag = ElementTagsList.Tag(
        text=f"Tag {tag_type}", type=tag_type, hit=True, closable=True, close_transition=False
    )
    all_tag_types.append(curr_tag)

el_tags_list = ElementTagsList(tags=all_tag_types)

card = Card(
    "Element Tags List",
    content=el_tags_list,
)

layout = card
app = sly.Application(layout=layout)


@el_tags_list.close
def close_tag(current_tags):
    el_tags_list.add_tags([ElementTagsList.Tag(text="New Tag", closable=True)])
