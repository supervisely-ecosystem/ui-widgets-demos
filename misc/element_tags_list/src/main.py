import os
import random
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, ElementTagsList

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api: sly.Api = sly.Api.from_env()

el_tag = ElementTagsList.ElementTag(text="Tag", closable=True, close_transition=False)

# button = Button()

all_tag_types = [el_tag]
for tag_type in ["primary", "gray", "success", "warning", "danger"]:
    curr_tag = ElementTagsList.ElementTag(
        text=f"Tag {tag_type}", type=tag_type, hit=True, closable=True, close_transition=True
    )
    all_tag_types.append(curr_tag)

# el_tag = ElementTag(
#     text="Element Tag", type="primary", hit=True, closable=True, close_transition=True
# )

taggggs = all_tag_types  # ["tag 1", "tag 2", "tag 3"]

el_tags = ElementTagsList(tags=taggggs)

card = Card(
    "ElementTag",
    content=Container(widgets=[el_tags], direction="horizontal"),
)


layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@el_tags.close
def close_tag(res):
    info = res
    el_tags.add_tags([ElementTagsList.ElementTag(text="Tag213123123")])
