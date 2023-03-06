import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, SelectTagMeta

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

project_id = sly.env.project_id()

# initialize widgets we will use in UI
select_tag_meta = SelectTagMeta(default="cat", project_id=project_id)
from supervisely.annotation.tag_meta import TagValueType

allowed_types = [TagValueType.ANY_STRING]
select_tag_meta = SelectTagMeta(project_id=project_id, allowed_types=allowed_types)

card = Card(
    title="Select TagMeta",
    content=select_tag_meta,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
