import os
import supervisely as sly
from supervisely.app.widgets import (
    Card,
    Container,
    ClassesListSelector,
    NotificationBox,
    Text,
)
from dotenv import load_dotenv


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

cat_obj_class = sly.ObjClass("cat", sly.Rectangle)
dog_obj_class = sly.ObjClass("dog", sly.Rectangle)
horse_obj_class = sly.ObjClass("horse", sly.Rectangle)
sheep_obj_class = sly.ObjClass("sheep", sly.Rectangle)
cow_obj_class = sly.ObjClass("cow", sly.Rectangle)
elephant_obj_class = sly.ObjClass("elephant", sly.Rectangle)
bear_obj_class = sly.ObjClass("bear", sly.Rectangle)
zebra_obj_class = sly.ObjClass("zebra", sly.Rectangle)
obj_classes = [
    cat_obj_class,
    dog_obj_class,
    horse_obj_class,
    sheep_obj_class,
    cow_obj_class,
    elephant_obj_class,
    bear_obj_class,
    zebra_obj_class,
]


notification_box = NotificationBox(title="No classes", description="Provide classes to the widget.")
classes_list_selector = ClassesListSelector(
    obj_classes, multiple=True, empty_notification=notification_box, allow_new_classes=True
)

selected_classes_cnt = Text(f"Selected classes: 0 / {len(obj_classes)}")
info_text = Text("You can create new classes using button Add new class", status="info")

container = Container(
    widgets=[
        info_text,
        selected_classes_cnt,
        classes_list_selector,
    ]
)

card = Card(
    title="Classes List Selector",
    content=container,
)

layout = card
app = sly.Application(layout=layout)


# Update counters helper
def update_counters():
    all_classes = classes_list_selector.get_all_classes()
    selected = classes_list_selector.get_selected_classes()
    selected_classes_cnt.set(f"Selected classes: {len(selected)} / {len(all_classes)}", "text")


@classes_list_selector.selection_changed
def selection_changed(classes):
    update_counters()


@classes_list_selector.class_created
def on_class_created(new_class):
    info_text.set(f"New class created: '{new_class.name}' ({new_class.geometry_type.name()})", "success")
    update_counters()
