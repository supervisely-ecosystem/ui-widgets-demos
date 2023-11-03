import os
from random import randint

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, TagMetasList, ProjectThumbnail

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

project_id = sly.env.project_id()
dataset_id = sly.env.dataset_id(raise_not_found=False)

# get proect info and meta from server
project_info = api.project.get_info_by_id(id=project_id)

# initialize widgets we will use in UI
project_meta = sly.ProjectMeta.from_json(api.project.get_meta(project_id))

# initialize widget TagMetasList
tag_metas_list = TagMetasList(
    tag_metas=project_meta.tag_metas,
    show_type_text=True,
    limit_long_names=False,
    selectable=True,
    columns=1,
)

# create widget ProjectThumbnail
project_thumbnail = ProjectThumbnail(project_info)

card = Card(
    title="Tag Metas List",
    content=Container(widgets=[project_thumbnail, tag_metas_list]),
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
