import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Carousel, Text

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api: sly.Api = sly.Api.from_env()

items = [
    Carousel.Item(name="Slide 1", label="https://www.w3schools.com/howto/img_nature.jpg"),
    Carousel.Item(name="Slide 2", label="https://i.imgur.com/35pUPD2.jpg"),
    Carousel.Item(name="Slide 3", label="label 3", is_link=False),
    Carousel.Item(name="Slide 4", label="https://www.quackit.com/pix/samples/18m.jpg"),
    Carousel.Item(name="Slide 5", label="https://i.imgur.com/OpSj3JE.jpg"),
]

text = Text()

carousel = Carousel(items=items, autoplay=False, trigger="click", height=500)

card = Card(
    "Carousel",
    content=Container([carousel, text]),
)


layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@carousel.value_changed
def test(res):
    info = f"Current slide index: {res}"
    text.set(text=info, status="info")
