import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import (
    Button,
    Card,
    Container,
    CompareImages,
    Text,
    LabeledImage,
    Image,
)

load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

left_image = LabeledImage()
right_image = LabeledImage()

# compare_images = CompareImages(left=left_image, right=right_image)

compare_images = CompareImages(left=left_image)


project_id = 14957
dataset_id = 52733
project_meta = sly.ProjectMeta.from_json(data=api.project.get_meta(id=project_id))
images_infos = api.image.get_list(dataset_id=dataset_id)
anns_infos = api.annotation.get_list(dataset_id=dataset_id)

image_name_left = images_infos[0].name
image_url_left = images_infos[0].full_storage_url
image_ann_left = sly.Annotation.from_json(data=anns_infos[0].annotation, project_meta=project_meta)

image_name_right = images_infos[1].name
image_url_right = images_infos[1].full_storage_url
image_ann_right = sly.Annotation.from_json(data=anns_infos[1].annotation, project_meta=project_meta)

left_image.set(title=image_name_left, image_url=image_url_left, ann=image_ann_left)
right_image.set(title=image_name_right, image_url=image_url_right, ann=image_ann_right)

image_set_left = Image(url=images_infos[2].full_storage_url)
image_set_right = Image(url=images_infos[3].full_storage_url)
# compare_images.set_left(image_set_left)
# compare_images.set_right(image_set_right)


button = Button("set image")


# a = compare_images.get_left()
# b = compare_images.get_right()


card = Card(
    "Compare Images",
    content=Container([compare_images, button]),
)


layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@button.click
def add():
    compare_images.set_right(image_set_right)
