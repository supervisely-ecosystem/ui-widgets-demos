import os

import supervisely as sly
from dotenv import load_dotenv

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
app = sly.Application(
    templates_dir=os.path.join(os.getcwd(), "013_select_list", "templates")
)

items_list = [
    {"label": "a", "key": 1, "value": "Cat"},
    {"label": "b", "key": 2, "value": "Dog"},
    {"label": "c", "key": 3, "value": "Mouse"},
]
select_list = sly.app.widgets.SelectList(items=items_list)
print(select_list.get_items())
print(select_list.get_selected_item())

# select_list.set_selected_item(id=1, value="value")
