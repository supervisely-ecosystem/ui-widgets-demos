# Launch this app with:
# misc.ctbupdates.select_class.src.main:app

import os
import supervisely as sly
from supervisely.app.widgets import Card, Container, SelectClass
from dotenv import load_dotenv


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

cat_obj_class = sly.ObjClass("cat", sly.Rectangle)
dog_obj_class = sly.ObjClass("dog", sly.Rectangle)
horse_obj_class = sly.ObjClass("horse", sly.Rectangle)
sheep_obj_class = sly.ObjClass("sheep", sly.Rectangle)
obj_classes = [
    cat_obj_class,
    dog_obj_class,
    horse_obj_class,
    sheep_obj_class,
]
select_class = SelectClass(obj_classes, multiple=True, show_add_new_class=True)

container = Container([select_class])
card = Card(title="Select Class", content=container)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@select_class.value_changed
def on_value_changed(selected_classes: list[sly.ObjClass]):
    print(f"Selected classes: {[cls.name for cls in selected_classes]}")
    print(f"Selected classes count: {len(selected_classes)}")


@select_class.class_created
def on_class_created(new_class: sly.ObjClass):
    print(f"New class created: {new_class.name}, geometry: {new_class.geometry_type}")
