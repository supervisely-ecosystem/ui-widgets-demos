import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Carousel, Text

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api: sly.Api = sly.Api.from_env()

image_id = 22683828
static = os.path.join(sly.app.get_data_dir(), "static")
api.image.download_path(image_id, os.path.join(static, "image.jpg"))

items = [
    Carousel.Item(name="Slide 1", label="https://www.w3schools.com/howto/img_nature.jpg"),
    Carousel.Item(name="Slide 2", label="https://i.imgur.com/35pUPD2.jpg"),
    Carousel.Item(name="Slide 3", label=f"{os.path.join('static', 'image.jpg')}"), # for images from local directory
    Carousel.Item(name="Slide 4", label="https://www.quackit.com/pix/samples/18m.jpg"),
    Carousel.Item(name="Slide 5", label="https://i.imgur.com/OpSj3JE.jpg"),
]

text = Text()

carousel = Carousel(items=items, height=200, type="card")

card = Card(
    "Carousel",
    content=Container([carousel, text]),
)


layout = Container(widgets=[card])
app = sly.Application(layout=layout, static_dir=static)


@carousel.value_changed
def test(res):
    info = f"Current slide index: {res}"
    text.set(text=info, status="info")
