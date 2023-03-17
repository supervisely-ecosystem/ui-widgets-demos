import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Select, Cascader

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()


# initialize widgets we will use in UI
animals = [
    Cascader.Item(value="cat", label="cat"),
    Cascader.Item(value="dog", label="dog"),
    Cascader.Item(value="horse", label="horse"),
    Cascader.Item(value="sheep", label="sheep"),
]

select_items = Cascader(items=animals)


card = Card(
    title="Cascader",
    content=Container(widgets=[select_items]),
)

layout = Container(widgets=[card])
app = sly.Application(layout=layout)
