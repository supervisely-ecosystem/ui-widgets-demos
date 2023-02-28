import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, OneOf, Select, Image

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# initialize widgets we will use in UI
image_1 = Image(
    url="https://user-images.githubusercontent.com/79905215/218269544-2e126d4a-20eb-4ace-8933-d36732bb0634.jpeg"
)
image_2 = Image(
    url="https://user-images.githubusercontent.com/79905215/218269547-5b5316f9-9ae2-4b0c-aedb-b2238e44f95d.jpeg"
)
image_3 = Image(
    url="https://user-images.githubusercontent.com/79905215/218269550-a5caba65-1f0f-4986-8711-7d36c7911e51.jpeg"
)
items = [
    Select.Item(value="image 1", label="image 1", content=image_1),
    Select.Item(value="image 2", label="image 2", content=image_2),
    Select.Item(value="image 3", label="image 3", content=image_3),
]

select_items = Select(items=items)
one_of = OneOf(conditional_widget=select_items)
card = Card(
    title="One of",
    content=Container(widgets=[select_items, one_of]),
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
