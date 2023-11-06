import os
from random import choice
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, ImageAnnotationPreview

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# get project id and meta
project_id = sly.env.project_id()
project_meta_json = api.project.get_meta(project_id)
project_meta = sly.ProjectMeta.from_json(project_meta_json)


# get first dataset and first image of the dataset for initial preview
dataset = api.dataset.get_list(project_id)[0]
images = api.image.get_list(dataset.id)
image = images[0]

# get annotation for the image
ann_json = api.annotation.download(image.id).annotation
ann = sly.Annotation.from_json(ann_json, project_meta)


# initialize widget ImageAnnotationPreview with image
image_preview = ImageAnnotationPreview(
    annotations_opacity=0.5,
    enable_zoom=False,
    line_width=1,
)
image_preview.set(image_url=image.preview_url, ann=ann, project_meta=project_meta)

# create button to change image
random_button = Button("Random image")

# create card with image preview and button and put it to the app layout
card = Card(title="ImageAnnotationPreview", content=Container([image_preview, random_button]))
app = sly.Application(layout=card)


# this function will change image when user clicks on the button
@random_button.click
def set_random_image():
    random_image = choice(images)
    random_ann_json = api.annotation.download(random_image.id).annotation
    random_ann = sly.Annotation.from_json(random_ann_json, project_meta)
    image_preview.set(image_url=random_image.preview_url, ann=random_ann, project_meta=project_meta)
