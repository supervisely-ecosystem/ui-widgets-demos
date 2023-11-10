import os
from random import choice
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import (
    Button,
    Card,
    Container,
    CompareImages,
    ImageAnnotationPreview,
    LabeledImage,
    Image,
)

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
image_storage_urls = []
image_preview_urls = []
image_anns = []
for idx in range(len(images_infos)):
    image_names.append(images_infos[idx].name)
    image_storage_urls.append(images_infos[idx].full_storage_url)
    image_preview_urls.append(images_infos[idx].preview_url)
    image_anns.append(
        sly.Annotation.from_json(data=anns_infos[idx].annotation, project_meta=project_meta)
    )


# Image
# left_image_widget = Image()
# left_image_widget.set(url=image_storage_urls[0])


# right_image_widget = Image()
# right_image_widget.set(url=image_storage_urls[1])

# LabeledImage
# left_image_widget = LabeledImage()
# left_image_widget.set(
#     title=image_names[0],
#     image_url=image_storage_urls[0],
#     ann=image_anns[0],
#     image_id=images_infos[0].id,
# )

# right_image_widget = LabeledImage()
# right_image_widget.set(
#     title=image_names[1],
#     image_url=image_storage_urls[1],
#     ann=image_anns[1],
#     image_id=image_preview_urls[1],
# )

# ImageAnnotationPreview
left_image_widget = ImageAnnotationPreview()
left_image_widget.set(image_url=image_preview_urls[0], ann=image_anns[0], project_meta=project_meta)

right_image_widget = ImageAnnotationPreview()
right_image_widget.set(
    image_url=image_preview_urls[1], ann=image_anns[1], project_meta=project_meta
)

compare_images = CompareImages(left=left_image_widget, right=right_image_widget)

button_set_left = Button("Set left image")
button_set_right = Button("Set right image")
btn_set_both = Button("Update left & right")
btn_clean_left = Button("Clean left")
btn_clean_right = Button("Clean right")
buttons = Container(
    [button_set_left, btn_clean_left, btn_set_both, btn_clean_right, button_set_right],
    direction="horizontal",
)

card = Card(
    "Compare Images",
    content=Container([compare_images, buttons]),
)

layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@button_set_left.click
def add():
    random_idx = choice(range(len(image_names)))
    # ImageAnnotationPreview
    compare_images.update_left(
        image_url=image_preview_urls[random_idx],
        ann=image_anns[random_idx],
        project_meta=project_meta,
    )

    # Image
    # compare_images.update_right(url=image_storage_urls[random_idx])

    # LabeledImage
    # compare_images.update_right(
    # title=image_names[random_idx],
    # image_url=image_storage_urls[random_idx],
    # ann=image_anns[random_idx],
    # image_id=images_infos[random_idx].id,
    # )


@button_set_right.click
def add():
    random_idx = choice(range(len(image_names)))
    # ImageAnnotationPreview
    compare_images.update_right(
        image_url=image_preview_urls[random_idx],
        ann=image_anns[random_idx],
        project_meta=project_meta,
    )

    # Image
    # compare_images.update_right(url=image_storage_urls[random_idx])

    # LabeledImage
    # compare_images.update_right(
    # title=image_names[random_idx],
    # image_url=image_storage_urls[random_idx],
    # ann=image_anns[random_idx],
    # image_id=images_infos[random_idx].id,
    # )


@btn_set_both.click
def update_left_n_right():
    random_idx_l = choice(range(len(image_names)))
    random_idx_r = choice(range(len(image_names)))
    if random_idx_r == random_idx_l:
        random_idx_r = choice(range(len(image_names)))

    # ImageAnnotationPreview
    compare_images.update_left(
        image_url=image_preview_urls[random_idx_l],
        ann=image_anns[random_idx_l],
        project_meta=project_meta,
    )

    compare_images.update_right(
        image_url=image_preview_urls[random_idx_r],
        ann=image_anns[random_idx_r],
        project_meta=project_meta,
    )


@btn_clean_left.click
def add():
    compare_images.clean_up_left()


@btn_clean_right.click
def add():
    compare_images.clean_up_right()
