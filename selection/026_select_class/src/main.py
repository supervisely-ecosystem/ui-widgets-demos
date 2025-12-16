import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, NotificationBox, SelectClass

# for convenient debug, has no effect in production
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
# initialize widgets we will use in UI
select_class = SelectClass(obj_classes, filterable=True, placeholder="Select a class", multiple=True, show_add_new_class=True)

notification_box = NotificationBox()

card = Card(
    title="Select Class",
    content=Container(widgets=[select_class, notification_box]),
)

layout = Container(widgets=[card])

app = sly.Application(layout=layout)


@select_class.value_changed
def on_class_selected(class_name):
    selected_class = select_class.get_selected_class()

@select_class.class_created
def on_class_created(new_class: sly.ObjClass):
    notification_box.set(
        title="New class created",
        description=f"You have created a new class: {new_class.name}",
    )
