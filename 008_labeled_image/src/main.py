from curses import meta
import os
from time import sleep
from dotenv import load_dotenv
import supervisely as sly


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
app = sly.Application(
    templates_dir=os.path.join(os.getcwd(), "008_labeled_image", "templates")
)


# get project info from server
project_id = int(os.environ["modal.state.slyProjectId"])
project = api.project.get_info_by_id(project_id)
meta_json = api.project.get_meta(id=project_id)
meta = sly.ProjectMeta.from_json(data=meta_json)

# get image info and annotation from server
image_id = int(os.environ["modal.state.slyImageId"])
image = api.image.get_info_by_id(id=image_id)
ann_json = api.annotation.download_json(image_id=image_id)
ann = sly.Annotation.from_json(data=ann_json, project_meta=meta)


# initialize widgets we will use in UI
labeled_image = sly.app.widgets.LabeledImage()

# set image
labeled_image.set(title=image.name, image_url=image.preview_url, ann=ann)
