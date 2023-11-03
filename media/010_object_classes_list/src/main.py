import os
from random import randint

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import (
    Button,
    Card,
    Container,
    Image,
    ObjectClassesList,
    ProjectThumbnail,
)

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

project_id = sly.env.project_id()
dataset_id = sly.env.dataset_id()

# get proect info and meta from server
project_info = api.project.get_info_by_id(id=project_id)

# initialize widgets we will use in UI
project_meta = sly.ProjectMeta.from_json(api.project.get_meta(project_id))


obj_classes_list = ObjectClassesList(
    object_classes=project_meta.obj_classes,
    selectable=True,
    columns=3,
)

# create widget ProjectThumbnail
project_thumbnail = ProjectThumbnail(project_info)

cls_select_btn = Button(text="PREVIEW")

select_class_container = Container(widgets=[obj_classes_list, cls_select_btn])
image = Image()

preview_container = Container(
    widgets=[select_class_container, image],
    direction="horizontal",
    fractions=[2, 1],
)

card = Card(
    title="Object Classes List",
    content=Container(widgets=[project_thumbnail, preview_container]),
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@cls_select_btn.click
def show_info():
    classes = obj_classes_list.get_selected_classes()
    if len(classes) > 0:
        obj_classes = api.object_class.get_list(
            project_id=project_id, filters=[{"field": "name", "operator": "in", "value": classes}]
        )
        imgs = api.image.get_filtered_list(
            dataset_id=dataset_id,
            filters=[{"type": "objects_class", "data": {"classId": obj.id}} for obj in obj_classes],
        )
    else:
        obj_classes = api.object_class.get_list(project_id=project_id)
        imgs = api.image.get_list(dataset_id=dataset_id)

    if len(imgs) == 0:
        image.clean_up()
        return
    index = randint(0, len(imgs) - 1)
    image.set(imgs[index].full_storage_url)
