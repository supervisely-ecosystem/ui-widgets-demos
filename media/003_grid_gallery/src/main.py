import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, GridGallery

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

project_id = sly.env.project_id()
dataset_id = sly.env.dataset_id()
project_meta = sly.ProjectMeta.from_json(data=api.project.get_meta(id=project_id))

# initialize widgets we will use in UI
grid_gallery = GridGallery(columns_number=3, enable_zoom=False)

images_infos = api.image.get_list(dataset_id=dataset_id)[: grid_gallery.columns_number]
anns_infos = api.annotation.get_list(dataset_id=dataset_id)[: grid_gallery.columns_number]
for idx, (image_info, ann_info) in enumerate(zip(images_infos, anns_infos)):
    image_name = image_info.name
    image_url = image_info.full_storage_url
    image_ann = sly.Annotation.from_json(data=ann_info.annotation, project_meta=project_meta)

    grid_gallery.append(
        title=image_name, image_url=image_url, annotation=image_ann, column_index=idx
    )

card = Card(
    title="Grid Gallery",
    content=grid_gallery,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
