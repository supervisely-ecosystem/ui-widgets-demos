import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import DoneLabel, Empty, Menu, Text

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

text = Text(text="text", status="success")
done_label = DoneLabel("done")

g1_items = [
    Menu.Item(title="menu item 1", content=text),
    Menu.Item(title="menu item 2", content=done_label),
]

g2_items = [
    Menu.Item(title="menu item 3", content=Empty()),
    Menu.Item(title="menu item 4"),
]
group_1 = Menu.Group("group 1", g1_items)
group_2 = Menu.Group("group 2", g2_items)

menu = Menu(groups=[group_1, group_2])

app = sly.Application(layout=menu)
