import os

from dotenv import load_dotenv
import supervisely as sly
from supervisely.app.widgets import Card, Container, Text, ImageSlider, Button

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()


image_urls = [
    "https://www.w3schools.com/howto/img_nature.jpg",
    "https://www.quackit.com/pix/samples/18m.jpg",
    "https://i.imgur.com/35pUPD2.jpg",
    "https://i.imgur.com/fB2DBcM.jpeg",
    "https://i.imgur.com/OpSj3JE.jpg",
]


image_slider = ImageSlider(data=image_urls, selectable=True, height=250)


image_url = Text(status="info")
image_index = Text(status="info")

button_url = Button(text="Get image url")
button_index = Button(text="Get image index")

buttons_container = Container(
    widgets=[button_url, button_index],
    direction="vertical",
)


card = Card(
    title="Image Slider",
    content=Container([image_slider, image_url, image_index, buttons_container]),
)

layout = Container(widgets=[card])

app = sly.Application(layout=layout)


@button_url.click
def get_url():
    image_url.text = f"Image URL: {image_slider.get_preview_url()}"


@button_index.click
def get_index():
    image_index.text = f"Image index on slider: {image_slider.get_preview_idx()}"
