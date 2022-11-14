import os
from time import sleep

import supervisely as sly
from dotenv import load_dotenv

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
app = sly.Application(
    templates_dir=os.path.join(os.getcwd(), "005_project_thumbnail", "templates")
)


# get project info from server
project_id = int(os.environ["modal.state.slyProjectId"])
project = api.project.get_info_by_id(project_id)


# initialize widgets we will use in UI
project_info = sly.app.widgets.ProjectThumbnail(project)

