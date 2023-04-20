import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, CompareImages, Text, GridGallery

load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

compare_images = CompareImages()

compare_images.append(title="left image", image_url="https://i.imgur.com/o9iUwji.jpg")
compare_images.append(title="right image", image_url="https://i.imgur.com/RWoYlXf.jpg")

# compare_images.set_left(title="left image", image_url="https://i.imgur.com/o9iUwji.jpg")
# compare_images.set_right(
#     title="right image", image_url="https://i.imgur.com/RWoYlXf.jpg"
# )

card = Card(
    "Compare Images",
    content=Container([compare_images]),
)


layout = Container(widgets=[card])
app = sly.Application(layout=layout)
