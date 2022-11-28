import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Flexbox, ObjectClassView

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# initialize widgets we will use in UI
obj_class_cat = sly.ObjClass(name="cat", geometry_type=sly.Bitmap, color=[255, 0, 0])
obj_class_dog = sly.ObjClass(name="dog", geometry_type=sly.Bitmap, color=[0, 255, 0])
obj_class_sheep = sly.ObjClass(
    name="sheep", geometry_type=sly.Bitmap, color=[0, 0, 255]
)
obj_class_horse = sly.ObjClass(
    name="horse", geometry_type=sly.Bitmap, color=[255, 255, 0]
)
obj_class_squirrel = sly.ObjClass(
    name="squirrel", geometry_type=sly.Bitmap, color=[255, 0, 255]
)

obj_classes = [
    obj_class_cat,
    obj_class_dog,
    obj_class_sheep,
    obj_class_horse,
    obj_class_squirrel,
]

# initialize widgets we will use in UI
obj_class_view_widgets = [
    ObjectClassView(obj_class=obj_class) for obj_class in obj_classes
]

flexbox = Flexbox(
    widgets=obj_class_view_widgets,
    gap=100,
    center_content=True,
)

card = Card(
    title="Flexbox",
    content=flexbox,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
