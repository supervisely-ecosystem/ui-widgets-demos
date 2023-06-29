import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, ImageRegionSelector

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# get project info from server
project_id = sly.env.project_id()
project = api.project.get_info_by_id(project_id)
meta_json = api.project.get_meta(id=project_id)
meta = sly.ProjectMeta.from_json(data=meta_json)

# get image info and annotation from server
image_id = int(os.environ["modal.state.slyImageId"])
image = api.image.get_info_by_id(id=image_id)
ann_json = api.annotation.download_json(image_id=image_id)
ann = sly.Annotation.from_json(data=ann_json, project_meta=meta)

# initialize widgets we will use in UI
image_region_selector = ImageRegionSelector()

# set image
image_region_selector.set_image(image_info=image)

# set mask
mask = ann.labels[0].geometry.convert(sly.Bitmap)[0]
image_region_selector.set_mask(mask)

# set bbox
bbox = ann.labels[0].geometry.to_bbox()
bbox = [[bbox.left, bbox.top], [bbox.right, bbox.bottom]]
image_region_selector.set_bbox(bbox)

# set bbox change callback
@image_region_selector.bbox_changed
def bbox_changed(bbox):
    print("bbox changed", bbox)

# set positive points change callback
@image_region_selector.positive_points_changed
def positive_points_changed(points):
    print("positive points changed", points)

# set negative points change callback
@image_region_selector.negative_points_changed
def negative_points_changed(points):
    print("negative points changed", points)

card = Card(
    title="Image Region Selector",
    content=image_region_selector,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
