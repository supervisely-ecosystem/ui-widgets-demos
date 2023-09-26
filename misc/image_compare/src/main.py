import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, CompareImages, LabeledImage, Image

if sly.is_development():
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

left_labeled_image = LabeledImage(view_height=300)
right_labeled_image = LabeledImage(view_height=300)
left_labeled_image.set(title=image_names[0], image_url=image_urls[0], ann=image_anns[0])
right_labeled_image.set(title=image_names[1], image_url=image_urls[1], ann=image_anns[1])
left_image = Image(url=image_urls[2], width="100%")
right_image = Image(url=image_urls[3], width="100%")

button_set_left = Button("set left image")
button_set_right = Button("set right image")
btn_clean = Button("clean")
btn_clean_left = Button("clean left")
btn_clean_right = Button("clean right")
buttons = Container(
    [button_set_left, button_set_right, btn_clean, btn_clean_left, btn_clean_right],
    direction="horizontal",
)

# compare_images = CompareImages(left=left_labeled_image, right=right_labeled_image)
compare_images = CompareImages(left=left_image, right=right_image)

card = Card(
    "Compare Images",
    content=Container([compare_images, buttons]),
)


layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@button_set_left.click
def add():
    # compare_images.update_left(title=image_names[2], image_url=image_urls[2], ann=image_anns[2])
    compare_images.update_left(url=image_urls[2])


@button_set_right.click
def add():
    # compare_images.update_right(title=image_names[4], image_url=image_urls[4], ann=image_anns[4])
    compare_images.update_right(url=image_urls[4])


@btn_clean_left.click
def add():
    compare_images.clean_up_left()


@btn_clean_right.click
def add():
    compare_images.clean_up_right()
