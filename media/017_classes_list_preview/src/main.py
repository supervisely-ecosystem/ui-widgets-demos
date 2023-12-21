import os
import supervisely as sly
from supervisely.app.widgets import (
    Card,
    Container,
    ClassesListPreview,
    ClassesListSelector,
    Text,
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

classes_list_selector = ClassesListSelector(obj_classes, multiple=True)

classes_list_preview = ClassesListPreview()
preview_text = Text(f"Selected Classes: 0 / {len(obj_classes)}", "text")
preview_container = Container([preview_text, classes_list_preview])

container = Container(widgets=[classes_list_selector, preview_container])

card = Card(
    title="Classes List Preview",
    content=container,
)

layout = card
app = sly.Application(layout=layout)


@classes_list_selector.selection_changed
def on_selection_changed(selected_classes):
    preview_text.set(f"Selected Classes: {len(selected_classes)} / {len(obj_classes)}", "text")
    classes_list_preview.set(selected_classes)
