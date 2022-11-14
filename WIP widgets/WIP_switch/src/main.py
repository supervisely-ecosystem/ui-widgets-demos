import os
from re import T
from tkinter import N

import supervisely as sly
from dotenv import load_dotenv

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
app = sly.Application(
    templates_dir=os.path.join(os.getcwd(), "016_switch", "templates")
)

switch = sly.app.widgets.Switch()

turn_switch_button = sly.app.widgets.Button("Turn ON")
set_text_switch_button = sly.app.widgets.Button("With Text")
color_switch_button = sly.app.widgets.Button("Set colors")


@turn_switch_button.click
def turn_switch():
    if switch.is_switched():
        turn_switch_button.text = "Turn ON"
        switch.off()
    else:
        turn_switch_button.text = "Turn OFF"
        switch.on()
    print(f"Switched: {switch.is_switched()}")


@set_text_switch_button.click
def set_text():
    if switch.get_on_text() is None and switch.get_off_text() is None:
        set_text_switch_button.text = "Remove text"
        switch.set_on_text("ON")
        switch.set_off_text("OFF")
    else:
        set_text_switch_button.text = "Set text"
        switch.set_on_text(None)
        switch.set_off_text(None)


@color_switch_button.click
def color_switch():
    if switch.get_on_color() == "#20a0ff" and switch.get_off_color() == "#bfcbd9":
        color_switch_button.text = "Set default color"
        switch.set_on_color("#13ce66")
        switch.set_off_color("#ff4949")
    else:
        color_switch_button.text = "Set color"
        switch.set_on_color("#20a0ff")
        switch.set_off_color("#bfcbd9")
