import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, NotificationBox


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

note_box_desc = "Lorem ipsum dolor sit amet... anim id est laborum."

# initialize widgets we will use in UI
note_box_success = NotificationBox(
    title="Box type: SUCCESS", description=note_box_desc, box_type="success"
)
note_box_info = NotificationBox(
    title="Box type: INFO", description=note_box_desc, box_type="info"
)
note_box_warning = NotificationBox(
    title="Box type: WARNING", description=note_box_desc, box_type="warning"
)
note_box_error = NotificationBox(
    title="Box type: ERROR", description=note_box_desc, box_type="error"
)

notification_container = Container(
    widgets=[note_box_success, note_box_info, note_box_warning, note_box_error]
)

card = Card(
    title="Notification Box",
    content=notification_container,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
