import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Empty, Menu, Select, Text

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

g1_items = [
    Menu.Item(title="m1", content=r),
    Menu.Item(title="m2", content=l),
]
g2_items = [
    Menu.Item(title="m3", content=Empty()),
    Menu.Item(title="m4"),
]
g1 = Menu.Group("g1", g1_items)
g2 = Menu.Group("g2", g2_items)
menu = Menu(groups=[g1, g2])
app = sly.Application(layout=menu)
