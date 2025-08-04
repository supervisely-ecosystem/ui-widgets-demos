import os
import random

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, Image

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

IMAGE_URL = "https://github.com/supervisely-ecosystem/ui-widgets-demos/releases/download/v0.0.6/pexels-lenin-estrada-117221-2896297.jpg"

lock_btn = Button("Lock")
collapse_btn = Button("Collapse")
loading_btn = Button("Loading True")

unlock_btn = Button("Unlock", button_type="success")
uncollapse_btn = Button("Uncollapse", button_type="success")
refresh_btn = Button("Loading False", button_type="success")

btn_container_1 = Container(widgets=[loading_btn, refresh_btn])
btn_container_2 = Container(widgets=[lock_btn, unlock_btn])
btn_container_3 = Container(widgets=[collapse_btn, uncollapse_btn])

containers = Container(
    widgets=[btn_container_1, btn_container_2, btn_container_3],
    direction="horizontal",
)

preview_btn = Button("Preview")
image = Image()

btns_card = Card(content=containers)

image_card = Card(
    title="Card",
    description="Card Description",
    content=image,
    collapsable=True,
    content_top_right=preview_btn,
)

layout = Container(
    widgets=[btns_card, image_card],
    direction="horizontal",
    fractions=[1, 1],
)

app = sly.Application(layout=layout)


@unlock_btn.click
def lock_card():
    image_card.unlock()


@uncollapse_btn.click
def lock_card():
    image_card.uncollapse()


@refresh_btn.click
def lock_card():
    image_card.loading = False


@lock_btn.click
def lock_card():
    image_card.lock()


@collapse_btn.click
def lock_card():
    image_card.collapse()


@loading_btn.click
def lock_card():
    image_card.loading = True


@preview_btn.click
def load_preview_image():
    image_card.loading = True
    image.set(IMAGE_URL)
    image_card.loading = False
