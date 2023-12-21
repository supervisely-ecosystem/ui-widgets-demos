import os
import supervisely as sly
from supervisely.app.widgets import (
    Card,
    Container,
    ClassesColorMapping,
    ClassesListPreview,
    Button,
    Text,
)
from dotenv import load_dotenv


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()


cat_obj_class = sly.ObjClass("cat", sly.Rectangle, color=[255, 0, 0])
dog_obj_class = sly.ObjClass("dog", sly.Polygon, color=[0, 255, 0])
horse_obj_class = sly.ObjClass("horse", sly.Bitmap, color=[0, 0, 255])
cow_obj_class = sly.ObjClass("cow", sly.Polyline, color=[255, 255, 0])
zebra_obj_class = sly.ObjClass("zebra", sly.Point, color=[255, 0, 255])
obj_classes = [
    cat_obj_class,
    dog_obj_class,
    horse_obj_class,
    cow_obj_class,
    zebra_obj_class,
]

classes_color_mapping = ClassesColorMapping(obj_classes)

classes_list_preview = ClassesListPreview()
new_classes_names = Text(f"Press button to save changes", "info")
save_button = Button("Save", button_size="mini")

container = Container([classes_color_mapping, new_classes_names, save_button, classes_list_preview])

card = Card(
    title="Classes Color Mapping",
    content=container,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@save_button.click
def save_changes():
    new_classes = classes_color_mapping.get_selected_classes_edited()
    classes_list_preview.set(new_classes)
