import os

import supervisely as sly
from dotenv import load_dotenv

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
app = sly.Application(
    templates_dir=os.path.join(os.getcwd(), "007_notification_box", "templates")
)

note_box_desc = "Lorem ipsum dolor sit amet... anim id est laborum."

# initialize widgets we will use in UI
note_box_success = sly.app.widgets.NotificationBox(
    title="Box type: SUCCESS", description=note_box_desc, box_type="success"
)
note_box_info = sly.app.widgets.NotificationBox(
    title="Box type: INFO", description=note_box_desc, box_type="info"
)
note_box_warning = sly.app.widgets.NotificationBox(
    title="Box type: WARNING", description=note_box_desc, box_type="warning"
)
note_box_error = sly.app.widgets.NotificationBox(
    title="Box type: ERROR", description=note_box_desc, box_type="error"
)
