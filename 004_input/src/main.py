import os
from random import choice

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, Input

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

input_text = Input(placeholder="Please input")
button_random_planet = Button(text="Random planet name")
button_clean_input = Button(text="Clean input")
button_set_readonly = Button(text="Set readonly")

buttons_container = Container(
    widgets=[
        button_random_planet,
        button_clean_input,
        button_set_readonly,
    ],
    direction="horizontal",
)

card = Card(
    title="Input",
    content=Container(widgets=[input_text, buttons_container]),
)

layout = Container(widgets=[card], direction="vertical")
app = sly.Application(layout=layout)


@button_random_planet.click
def random_planet():
    input_text.set_value(
        choice(
            [
                "Mercury",
                "Venus",
                "Earth",
                "Mars",
                "Jupiter",
                "Saturn",
                "Uranus",
                "Neptune",
            ]
        )
    )


@button_clean_input.click
def random_word():
    input_text.set_value("")


@button_set_readonly.click
def set_readonly():
    if input_text.is_readonly():
        input_text.disable_readonly()
        print("Readonly: Disabled")
    else:
        input_text.enable_readonly()
        print("Readonly: Enabled")
