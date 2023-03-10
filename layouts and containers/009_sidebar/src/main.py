import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Select, Sidebar, Text

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

left = Text(text="left part", status="success")
items = [
    Select.Item(label="CPU", value="cpu"),
    Select.Item(label="GPU 0", value="cuda:0"),
    Select.Item(value="option3"),
]
right = Select(items=items, filterable=True, placeholder="select me")

sidebar = Sidebar(left_content=left, right_content=right)
app = sly.Application(layout=sidebar)
