import os
import supervisely as sly
from supervisely.app.widgets import Card, Container, ClassesListSelector, NotificationBox, Text
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
    obj_classes, multiple=True, empty_notification=notification_box
)

selected_classes_cnt = Text(f"Selected classes: 0 / {len(obj_classes)}")
container = Container(widgets=[selected_classes_cnt, classes_list_selector])

card = Card(
    title="Classes List Selector",
    content=container,
)

layout = card
app = sly.Application(layout=layout)


@classes_list_selector.selection_changed
def selection_changed(classes):
    selected_classes_cnt.set(f"Selected classes: {len(classes)} / {len(obj_classes)}", "text")
