import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Select, OneOf


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# initialize widgets we will use in UI
animals = [
    Select.Item(value="cat", label="cat"),
    Select.Item(value="dog", label="dog"),
    Select.Item(value="horse", label="horse"),
    Select.Item(value="sheep", label="sheep"),
]

select_items = Select(items=animals)
one_of = OneOf(conditional_widget=select_items)
card = Card(
    title="One of",
    content=one_of,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
