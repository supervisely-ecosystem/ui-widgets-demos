import os
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, LabeledImage

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

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
labeled_image = LabeledImage()

# set image
labeled_image.set(title=image.name, image_url=image.preview_url, ann=ann)

card = Card(
    title="Labeled Image",
    content=labeled_image,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
