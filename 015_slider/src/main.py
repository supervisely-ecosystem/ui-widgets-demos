import os
import math
from dotenv import load_dotenv
from random import randint, choice
import supervisely as sly


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
app = sly.Application(
    templates_dir=os.path.join(os.getcwd(), "015_slider", "templates")
)


default_slider = sly.app.widgets.Slider(value=[210, 110], range=True)

value_button = sly.app.widgets.Button(text="Set random value")
show_steps_button = sly.app.widgets.Button(text="Show steps")
set_steps_button = sly.app.widgets.Button(text="Set step to 10")
set_min_button = sly.app.widgets.Button(text="Set minimum random value")
set_max_button = sly.app.widgets.Button(text="Set maximum random value")
show_tooltip_button = sly.app.widgets.Button(text="Show tooltip")
show_input_button = sly.app.widgets.Button(text="Show input")
show_input_controls_button = sly.app.widgets.Button(text="Show input controls")


@value_button.click
def set_value():
    min_val = default_slider.get_min()
    max_val = default_slider.get_max()
    random_val = randint(min_val, max_val)
    if default_slider.get_step() == 10:
        random_val = randint(math.floor(min_val / 10), math.floor(max_val / 10))
        random_val = math.floor(
            random_val * (max_val / 10 - min_val / 10 + 1) + min_val / 10
        )
        default_slider.set_value(math.floor(random_val / 10) * 10)
    else:
        default_slider.set_value(random_val)


@show_steps_button.click
def show_steps():
    if default_slider.is_step_enabled():
        show_steps_button.text = "Show steps"
        default_slider.hide_steps()
    else:
        show_steps_button.text = "Hide steps"
        default_slider.show_steps()


@set_steps_button.click
def set_step():
    if default_slider.get_step() == 1:
        set_steps_button.text = "Set step to 1"
        default_slider.set_step(10)
    else:
        set_steps_button.text = "Set step to 10"
        default_slider.set_step(1)


@set_min_button.click
def set_min_value():
    default_slider.set_min(choice([10, 20, 30]))


@set_max_button.click
def set_max_value():
    default_slider.set_max(choice([80, 90, 100]))


@show_input_button.click
def show_input():
    if default_slider.is_input_enabled():
        show_input_button.text = "Show input"
        default_slider.hide_input()
    else:
        show_input_button.text = "Hide input"
        default_slider.show_input()


@show_input_controls_button.click
def show_input_controls():
    if default_slider.is_input_controls_enabled():
        show_input_controls_button.text = "Show input controls"
        default_slider.hide_input_controls()
    else:
        show_input_controls_button.text = "Hide input controls"
        default_slider.show_input_controls()


step_slider = sly.app.widgets.Slider(value=50, step=10, show_stops=True)
input_slider = sly.app.widgets.Slider(
    value=80, show_input=True, show_input_controls=True
)
range_slider = sly.app.widgets.Slider(
    value=[20, 60], show_input=False, show_input_controls=False, range=True
)
vertical_slider = sly.app.widgets.Slider(
    value=64, min=0, max=100, vertical=True, height=300
)

