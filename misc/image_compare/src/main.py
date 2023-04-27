import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import (
    Button,
    Card,
    Container,
    CompareImages,
    LabeledImage,
    Image,
)

load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()


project_id = sly.env.project_id()
dataset_id = sly.env.dataset_id()
project_meta = sly.ProjectMeta.from_json(data=api.project.get_meta(id=project_id))
images_infos = api.image.get_list(dataset_id=dataset_id)
anns_infos = api.annotation.get_list(dataset_id=dataset_id)

image_names = []
image_urls = []
image_anns = []
for idx in range(len(images_infos)):
    image_names.append(images_infos[idx].name)
    image_urls.append(images_infos[idx].full_storage_url)
    image_anns.append(
        sly.Annotation.from_json(data=anns_infos[idx].annotation, project_meta=project_meta)
    )


image_name_left = images_infos[0].name
image_url_left = images_infos[0].full_storage_url
image_ann_left = sly.Annotation.from_json(data=anns_infos[0].annotation, project_meta=project_meta)

image_name_right = images_infos[1].name
image_url_right = images_infos[1].full_storage_url
image_ann_right = sly.Annotation.from_json(data=anns_infos[1].annotation, project_meta=project_meta)

left_labeled_image = LabeledImage()
right_labeled_image = LabeledImage()
left_labeled_image.set(title=image_names[0], image_url=image_urls[0], ann=image_anns[0])
right_labeled_image.set(title=image_names[1], image_url=image_urls[1], ann=image_anns[1])

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
    compare_images.set_left(title=image_names[2], image_url=image_urls[2], ann=image_anns[2])


@button_set_right.click
def add():
    compare_images.set_right(title=image_names[4], image_url=image_urls[4], ann=image_anns[4])
