import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Field, TagMetaView, ProjectThumbnail

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

project_id = sly.env.project_id()

# get project info and meta from server
project_info = api.project.get_info_by_id(id=project_id)
project_meta = api.project.get_meta(id=project_id)
project_meta = sly.ProjectMeta.from_json(project_meta)

tag_metas = project_meta.tag_metas

# initialize widget TagMetaView
tag_meta_view = [
    TagMetaView(
        tag_meta=tag_meta,
        show_type_text=True,
        limit_long_names=False,
    )
    for tag_meta in tag_metas
]

tag_metas_container = Container(widgets=tag_meta_view)
tag_metas_field = Field(
    content=tag_metas_container,
    title="Project tags:",
)

# create widget ProjectThumbnail
project_thumbnail = ProjectThumbnail(project_info)

card = Card(
    title="TagMetaView",
    content=Container(widgets=[project_thumbnail, tag_metas_field]),
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
