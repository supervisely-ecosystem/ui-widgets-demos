import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Empty, OneOf, Select, Text

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# initialize widgets we will use in UI
empty = Empty()
text = Text("Some text")
items = [
    Select.Item("item_1", content=Empty()),
    Select.Item("item_2", content=text)
]
select = Select(items=items)
one_of = OneOf(select)

card = Card(
    title="Empty",
    content=empty,
)
layout = Container(widgets=[select, one_of])
app = sly.Application(layout=layout)
