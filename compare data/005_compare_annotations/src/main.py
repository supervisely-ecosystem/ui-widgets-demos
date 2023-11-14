# "compare data.005_compare_annotations.src.main:app"

import os
from random import choice
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import (
    Button,
    Card,
    Container,
    CompareAnnotations,
)
from pathlib import Path
from supervisely import Annotation, Rectangle
from supervisely.io.fs import get_file_name_with_ext


def ann_to_bbox(annotation: Annotation):
    labels = []
    mapping = {}
    for label in annotation.labels:
        if label.obj_class.name not in mapping:
            new_obj_class = sly.ObjClass(label.obj_class.name, Rectangle)
            mapping[label.obj_class] = new_obj_class
            label = label.scale(choice(range(90, 100)) / 100)
            labels.append(label)
    annotation = annotation.clone(labels=labels)
    annotation = annotation.to_detection_task(mapping)
    return annotation


if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

project_id = sly.env.project_id()
dataset_id = sly.env.dataset_id()

project_meta = sly.ProjectMeta.from_json(data=api.project.get_meta(id=project_id))

# Use data from local machine
# static_dir = Path("compare data/005_compare_annotations/images")
# ann_dir = Path("compare data/005_compare_annotations/annotations")
# image_urls = sorted([f"/static/{get_file_name_with_ext(path)}" for path in static_dir.iterdir() if path.is_file()])
# local_annotations = sorted([str(path) for path in ann_dir.iterdir() if path.is_file()])

# image_anns = []
# for local_ann in local_annotations:
#     ann = sly.Annotation.from_json(
#         data=sly.json.load_json_file(local_ann), project_meta=project_meta
#     )
#     image_anns.append(ann)

# Use data from Supervisely server
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

ann_names = [f"Model inference {idx+1}" for idx in range(len(image_anns))]

compare_annotations = CompareAnnotations(columns_number=3)
compare_annotations.set_image_url(image_url=image_urls[0])

for i in range(compare_annotations.columns_number):
    ann = ann_to_bbox(image_anns[0])
    compare_annotations.append(
        annotation=ann,
        title=ann_names[i],
        column_index=i,
    )

change_image_btn = Button("Change image")
clean_up_btn = Button("Clean up")

card = Card(
    "Compare Annotations",
    content=Container([compare_annotations, change_image_btn, clean_up_btn]),
)

layout = card
app = sly.Application(layout=layout)  # add static_dir to use data from local machine


@clean_up_btn.click
def clean_up():
    compare_annotations.clean_up()


@change_image_btn.click
def set_image():
    compare_annotations.clean_up()
    rnd_idx = choice(range(len(image_urls)))
    compare_annotations.set_image_url(image_urls[rnd_idx])
    for i in range(compare_annotations.columns_number):
        ann = ann_to_bbox(image_anns[rnd_idx])
        compare_annotations.append(
            annotation=ann,
            title=f"{ann_names[i]}",
            column_index=i,
        )
