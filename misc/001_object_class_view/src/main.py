import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Field, ObjectClassView, ProjectThumbnail

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

project_id = sly.env.project_id()

# get proect info and meta from server
project_info = api.project.get_info_by_id(id=project_id)
project_meta = api.project.get_meta(id=project_id)


# prepare dictionary to get geometry type by geometry name
SHAPES_TYPES = {
    "any": sly.AnyGeometry,
    "bitmap": sly.Bitmap,
    "point": sly.Point,
    "polygon": sly.Polygon,
    "rectangle": sly.Rectangle,
    "line": sly.Polyline,
}


# create ObjClass for each class in project
classes = [
    sly.ObjClass(
        name=obj["title"],
        geometry_type=SHAPES_TYPES[obj["shape"]],
    )
    for obj in project_meta["classes"]
]

# Create ObjClassCollection from ObjClasses
classes = sly.ObjClassCollection(classes)

# initialize widget ObjectClassView
obj_class_view = [
    ObjectClassView(
        obj_class=obj_class,
        show_shape_text=True,
        show_shape_icon=True,
    )
    for obj_class in classes
]

obj_class_container = Container(widgets=obj_class_view)
obj_class_field = Field(
    content=obj_class_container,
    title="Project classes:",
)

# create widget ProjectThumbnail
project_thumbnail = ProjectThumbnail(project_info)

card = Card(
    title="ObjectClassView",
    content=Container(widgets=[project_thumbnail, obj_class_field]),
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
