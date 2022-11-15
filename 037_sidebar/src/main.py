import os
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Sidebar, Select, Text

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

l = Text(text="left part", status="success")
items = [
    Select.Item(label="CPU", value="cpu"),
    Select.Item(label="GPU 0", value="cuda:0"),
    Select.Item(value="option3"),
]
r = Select(items=items, filterable=True, placeholder="select me")

sidebar = Sidebar(left_content=l, right_content=r)
app = sly.Application(layout=sidebar)
