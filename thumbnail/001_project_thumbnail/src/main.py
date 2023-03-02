import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, ProjectThumbnail

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# get project info from server
project_id = sly.env.project_id()
project = api.project.get_info_by_id(project_id)

# initialize widgets we will use in UI
project_thumbnail = ProjectThumbnail(project)
card = Card(
    title="Project Thumbnail",
    content=Container(widgets=[project_thumbnail]),
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
