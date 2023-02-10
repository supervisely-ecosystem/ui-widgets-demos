import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, OneOf, Select, Image

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# initialize widgets we will use in UI
cat_image = Image(
    url="https://user-images.githubusercontent.com/120389559/209821564-7917cbe5-fa8e-49dd-a1ca-519ee2b3a7ca.jpg"
)
dog_image = Image(
    url="https://user-images.githubusercontent.com/120389559/209821597-8670675b-5a18-480c-8fdc-1309e91086c7.jpg"
)
horse_image = Image(
    url="https://user-images.githubusercontent.com/120389559/209821602-ddb8196f-0ac5-4556-abae-178327ff734b.jpg"
)
sheep_image = Image(
    url="https://user-images.githubusercontent.com/120389559/209821609-c8396b3e-d7a3-4beb-b92b-539d31e91e90.jpg"
)
animals = [
    Select.Item(value="cat", label="cat", content=cat_image),
    Select.Item(value="dog", label="dog", content=dog_image),
    Select.Item(value="horse", label="horse", content=horse_image),
    Select.Item(value="sheep", label="sheep", content=sheep_image),
]

select_items = Select(items=animals)
one_of = OneOf(conditional_widget=select_items)
card = Card(
    title="One of",
    content=Container(widgets=[select_items, one_of]),
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
