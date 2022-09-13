import os
from random import choice
from dotenv import load_dotenv
import supervisely as sly


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
app = sly.Application(templates_dir=os.path.join(os.getcwd(), "012_input", "templates"))

input_text = sly.app.widgets.Input(value="AACCXX", placeholder="Type: Text")
button_random_planet = sly.app.widgets.Button(text="Random planet name")
button_clean_input = sly.app.widgets.Button(text="Clean input")
button_set_readonly = sly.app.widgets.Button(text="Set readonly")


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
    if input_text.readonly:
        input_text.readonly = False
    else:
        input_text.readonly = True

