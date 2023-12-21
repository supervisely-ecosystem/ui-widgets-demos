import os
import supervisely as sly
from supervisely.app.widgets import (
    Card,
    Container,
    ClassesMapping,
    ClassesMappingPreview,
    Button,
    NotificationBox,
)
from dotenv import load_dotenv


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()


cat_obj_class = sly.ObjClass("cat", sly.Rectangle)
dog_obj_class = sly.ObjClass("dog", sly.Polygon)
horse_obj_class = sly.ObjClass("horse", sly.Bitmap)
cow_obj_class = sly.ObjClass("cow", sly.Polyline)
zebra_obj_class = sly.ObjClass("zebra", sly.Point)
obj_classes = [
    cat_obj_class,
    dog_obj_class,
    horse_obj_class,
    cow_obj_class,
    zebra_obj_class,
]

empty_notification = NotificationBox(
    title="No classes", description="Provide classes to widget in order to map new names."
)
classes_mapping = ClassesMapping(obj_classes, empty_notification=empty_notification)


classes_mapping_preview = ClassesMappingPreview()
save_button = Button("Save", button_size="mini")

container = Container([classes_mapping, save_button, classes_mapping_preview])

card = Card(
    title="Classes Mapping Preview",
    content=container,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@save_button.click
def save_mapping():
    mapping = classes_mapping.get_mapping()
    classes_mapping_preview.set(obj_classes, mapping)
