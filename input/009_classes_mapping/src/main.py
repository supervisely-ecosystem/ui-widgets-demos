import os
import supervisely as sly
from supervisely.app.widgets import Card, Container, ClassesMapping, Button, Text, NotificationBox
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

new_classes_names = Text(f"Press button to save changes", "info")
save_button = Button("Save", button_size="mini")

container = Container([classes_mapping, new_classes_names, save_button])

card = Card(
    title="Classes Mapping",
    content=container,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@save_button.click
def save_mapping():
    new_classes_names.hide()
    mapping = classes_mapping.get_mapping()
    new_class_names = []
    for obj_class in obj_classes:
        if obj_class.name in mapping:
            new_class_name = mapping[obj_class.name]["value"]
            if new_class_name != obj_class.name:
                new_class_names.append(new_class_name)
    if len(new_class_names) == 0:
        new_classes_names.set(f"No changes detected", "info")
    else:
        new_classes_names.set(f"New classes names: {','.join(new_class_names)}", "success")
    new_classes_names.show()
