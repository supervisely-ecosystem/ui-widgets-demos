import os
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, ElementTagsList

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api: sly.Api = sly.Api.from_env()

el_tag = ElementTagsList.Tag(text="Tag", closable=True, close_transition=False)

all_tag_types = [el_tag]
for tag_type in ["primary", "gray", "success", "warning", "danger"]:
    curr_tag = ElementTagsList.Tag(
        text=f"Tag {tag_type}", type=tag_type, hit=True, closable=True, close_transition=False
    )
    all_tag_types.append(curr_tag)

el_tags = ElementTagsList(tags=all_tag_types)

card = Card(
    "ElementTag",
    content=Container(widgets=[el_tags], direction="horizontal"),
)


layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@el_tags.close
def close_tag(current_tags):
    info = current_tags
    el_tags.add_tags([ElementTagsList.Tag(text="Tag213123123")])
