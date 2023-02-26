import os
import supervisely as sly
from supervisely.app.widgets import Card, Container, Stepper, Text, Button
from dotenv import load_dotenv


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()


text_info = Text(text="My info text", status="info")
text_success = Text(text="My success text", status="success")
text_warning = Text(text="My warning text", status="warning")

card_info = Card(title="Info text", content=text_info)
card_success = Card(title="Success text", content=text_success)
card_warning = Card(title="Warning text", content=text_warning)


stepper = Stepper(
    widgets=[card_info, card_success, card_warning],
    titles=["Text step", "Success step", "Warning step"],
)

card = Card(
    title="Stepper",
    content=stepper,
)

button_increase = Button(text="Increase step")
button_decrease = Button(text="Decrease step")

buttons_container = Container(widgets=[button_increase, button_decrease])
buttons_card = Card(content=buttons_container)

layout = Container(widgets=[card, buttons_card])
app = sly.Application(layout=layout)


@button_increase.click
def click_button():
    curr_step = stepper.get_active_step()
    curr_step += 1
    stepper.set_active_step(curr_step)


@button_decrease.click
def click_button():
    curr_step = stepper.get_active_step()
    curr_step -= 1
    stepper.set_active_step(curr_step)
