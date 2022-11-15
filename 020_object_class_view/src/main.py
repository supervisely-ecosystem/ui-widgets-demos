import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, ObjectClassView

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

obj_class = sly.ObjClass(name="cat", geometry_type=sly.Bitmap, color=[255, 0, 0])

# initialize widgets we will use in UI
obj_class_view = ObjectClassView(
    obj_class=obj_class,
    show_shape_text=True,
    show_shape_icon=True,
)

card = Card(
    title="ObjClass View",
    content=obj_class_view,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
