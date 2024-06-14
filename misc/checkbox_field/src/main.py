import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, CheckboxField

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

checkbox_field = CheckboxField(title="Title", description="Description")
card = Card(title="CheckboxField", content=checkbox_field)
app = sly.Application(layout=card)


@checkbox_field.value_changed
def get_value(is_checked):
    print(is_checked)
    if is_checked:
        checkbox_field.set(title="Is Checked", checked=is_checked)
    else:
        checkbox_field.set(title="Is Not Checked", checked=is_checked)
