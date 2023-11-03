import os
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, TagMetasList, ProjectThumbnail, Text, Button

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

project_id = sly.env.project_id()

# get proect info and meta from server
project_info = api.project.get_info_by_id(id=project_id)
project_meta = sly.ProjectMeta.from_json(api.project.get_meta(project_id))

# initialize widget TagMetasList
tag_metas_list = TagMetasList(
    tag_metas=project_meta.tag_metas,
    show_type_text=True,
    limit_long_names=True,
    selectable=True,
    columns=1,
)

# create widget ProjectThumbnail
project_thumbnail = ProjectThumbnail(project_info)

show_selected_button = Button("Show tags")
tags_preview = Text("", "text")

card = Card(
    title="TagMetasList",
    content=Container(
        widgets=[project_thumbnail, tag_metas_list, show_selected_button, tags_preview]
    ),
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@show_selected_button.click
def show_selected_tags():
    selected_tag_names = tag_metas_list.get_selected_tag_names()
    tags_preview.set(" ,".join(selected_tag_names), "text")
