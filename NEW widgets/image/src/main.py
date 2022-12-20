import os

from dotenv import load_dotenv
import supervisely as sly
from supervisely.app.widgets import Card, Container, Image

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

IMAGE_ID1 = 11073637
IMAGE_ID2 = 17526002
IMAGE_ID3 = 17526001

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
image_3 = Image(image_url_3)

# create new card
card = Card(
    title="Image Preview",
    content=Container([image_1, image_2, image_3], direction="horizontal"),
)

layout = Container(widgets=[card])
app = sly.Application(layout=layout)
