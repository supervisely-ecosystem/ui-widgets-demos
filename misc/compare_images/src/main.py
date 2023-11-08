import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import (
    Button,
    Card,
    Container,
    CompareImages,
    ImageAnnotationPreview,
)

load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()


project_id = 14088  # sly.env.project_id()
dataset_id = api.dataset.get_list(project_id)[0].id  # sly.env.dataset_id()
project_meta = sly.ProjectMeta.from_json(data=api.project.get_meta(id=project_id))
images_infos = api.image.get_list(dataset_id=dataset_id)
anns_infos = api.annotation.get_list(dataset_id=dataset_id)

image_names = []
image_urls = []
image_anns = []
for idx in range(len(images_infos)):
    image_names.append(images_infos[idx].name)
    image_urls.append(images_infos[idx].preview_url)
    image_anns.append(
        sly.Annotation.from_json(data=anns_infos[idx].annotation, project_meta=project_meta)
    )

left_labeled_image = ImageAnnotationPreview(enable_zoom=False)
right_labeled_image = ImageAnnotationPreview(enable_zoom=False)
left_labeled_image.set(image_url=image_urls[0], ann=image_anns[0], project_meta=project_meta)
right_labeled_image.set(image_url=image_urls[1], ann=image_anns[1], project_meta=project_meta)

button_set_left = Button("set left image")
button_set_right = Button("set right image")
buttons = Container([button_set_left, button_set_right], direction="horizontal")

compare_images = CompareImages(left=left_labeled_image, right=right_labeled_image)

card = Card(
    "Compare Images",
    content=Container([compare_images, buttons]),
)


layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@button_set_left.click
def add():
    compare_images.update_left(title=image_names[2], image_url=image_urls[2], ann=image_anns[2])


@button_set_right.click
def add():
    compare_images.update_right(title=image_names[4], image_url=image_urls[4], ann=image_anns[4])
