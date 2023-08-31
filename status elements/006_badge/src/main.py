import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Badge, Button, Checkbox, Container, Card, Input, InputNumber

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

button_1 = Button("Hide badge")
text_input = Input(placeholder="Enter value")
text_badge = Badge(widget=button_1, value="new")
text_container = Container([text_badge, text_input])

button_2 = Button("Hide badge")
number_input = InputNumber(min=1, max=100)
number_badge = Badge(widget=button_2, value=1, max=10)
number_container = Container([number_badge, number_input])

button_3 = Button("Toggle visibility")
checkbox = Checkbox("Show badge")
dot_badge = Badge(widget=button_3, is_dot=True)
dot_container = Container([dot_badge, checkbox])


container = Container(
    widgets=[text_container, number_container, dot_container],
    direction="horizontal",
)
card = Card(content=container)

app = sly.Application(layout=card)


@text_input.value_changed
def set_badge_text(value):
    text_badge.set_value(value)


@number_input.value_changed
def set_badge_number(value):
    number_badge.set_value(value)


@checkbox.value_changed
def change_badge_visibility(value):
    dot_badge.toggle_visibility()


@button_1.click
def change_badge_visibility():
    text_badge.hide_badge()


@button_2.click
def change_badge_visibility():
    number_badge.hide_badge()


@button_3.click
def change_badge_visibility():
    dot_badge.toggle_visibility()
