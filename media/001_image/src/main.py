import os
from pathlib import Path

from dotenv import load_dotenv
import supervisely as sly
from supervisely.app.widgets import Card, Container, Image

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

IMAGE_ID1 = 19369662
IMAGE_ID2 = 19369661
IMAGE_ID3 = 19369660

# get image info from server
image_info_1 = api.image.get_info_by_id(IMAGE_ID1)
image_info_2 = api.image.get_info_by_id(IMAGE_ID2)
image_info_3 = api.image.get_info_by_id(IMAGE_ID3)

# get image url and title
image_url_1 = image_info_1.preview_url
image_url_2 = image_info_2.preview_url
image_url_3 = image_info_3.preview_url

# initialize widget we will use in UI
image_1 = Image(image_url_1)
image_2 = Image(image_url_2)
image_3 = Image(image_url_3, width="25%")

# add local image
local_image_url = "/static/my-cats.jpg"

# initialize widget
local_image = Image(local_image_url)
local_image.set_image_size(width="25%")

# create new card
card = Card(
    title="Image Preview",
    content=Container([image_1, image_2, image_3, local_image], direction="horizontal"),
)

layout = Container(widgets=[card])

# declare static files directory path to use images from local directory
static_dir = Path("media/001_image/images")

app = sly.Application(layout=layout, static_dir=static_dir)
