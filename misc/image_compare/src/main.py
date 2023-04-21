import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, CompareImages, Text, LabeledImage

load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

left_image = LabeledImage()
right_image = LabeledImage()
# left_image.set(title="left image", image_url="https://i.imgur.com/4XE5Fe7.jpg")
# right_image.set(title="right image", image_url="https://i.imgur.com/o9iUwji.jpg")

compare_images = CompareImages(widget_left=left_image, widget_right=right_image)


# compare_images.set_right(title="right image", image_url="https://i.imgur.com/o9iUwji.jpg")
# compare_images.set_left(title="left image", image_url="https://i.imgur.com/4XE5Fe7.jpg")

project_id = 14957
dataset_id = 52733
project_meta = sly.ProjectMeta.from_json(data=api.project.get_meta(id=project_id))
images_infos = api.image.get_list(dataset_id=dataset_id)[:2]
anns_infos = api.annotation.get_list(dataset_id=dataset_id)[:2]

image_name_left = images_infos[0].name
image_url_left = images_infos[0].full_storage_url
image_ann_left = sly.Annotation.from_json(data=anns_infos[0].annotation, project_meta=project_meta)

image_name_right = images_infos[1].name
image_url_right = images_infos[1].full_storage_url
image_ann_right = sly.Annotation.from_json(data=anns_infos[1].annotation, project_meta=project_meta)

left_image.set(title=image_name_left, image_url=image_url_left, ann=image_ann_left)
right_image.set(title=image_name_right, image_url=image_url_right, ann=image_ann_right)


# compare_images.set_left(title=image_name_left, image_url=image_url_left, ann=image_ann_left)
# compare_images.set_right(title=image_name_right, image_url=image_url_right, ann=image_ann_right)

# compare_images.set_left(title="left image", image_url="https://i.imgur.com/o9iUwji.jpg")
# compare_images.set_right(title="right image", image_url="https://i.imgur.com/RWoYlXf.jpg")


card = Card(
    "Compare Images",
    content=Container([compare_images]),
)


layout = Container(widgets=[card])
app = sly.Application(layout=layout)
