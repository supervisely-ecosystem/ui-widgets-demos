import os

from dotenv import load_dotenv
import supervisely as sly
from supervisely.app.widgets import Button, Card, Container, Icons

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

button_url = Button("Set url")
button_round = Button("Round icon")
button_standart = Button("Standart icon")
button_add_bg = Button("Add bg")
button_start = Button("Start icon")
btn_container = Container(
    [button_round, button_standart, button_add_bg, button_url, button_start], direction="horizontal"
)

icon_name = "zmdi zmdi-car-taxi"
icon = Icons(class_name=icon_name)

card = Card(
    title="Icons",
    content=Container([icon, btn_container]),
)

layout = Container(widgets=[card])

app = sly.Application(layout=layout)


@button_url.click
def set_url():
    icon.set_image_url("https://i.imgur.com/0E8d8bB.png")


@button_round.click
def set_round():
    icon.set_rounded()


@button_standart.click
def set_standart():
    icon.set_standart()


@button_add_bg.click
def set_bg():
    icon.set_bg_color("#000000")


@button_start.click
def start():
    icon.set_image_url("")
    icon.set_standart()
    icon.set_bg_color("")
    icon.set_class_name(icon_name)
