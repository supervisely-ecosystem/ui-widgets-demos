import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, Field, Input, InputNumber, Rate, Text


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api: sly.Api = sly.Api.from_env()

infos = ["oops", "disappointed", "normal", "good", "great"]
colors = ["#656565", "#F7BA2A", "#F6568E"]

########################### exmaple #1 ###########################
btn_1 = Button("Enable / Disable")

rate_1 = Rate(
    text_color="#656565",
    disabled=True,
    value=4,
    show_text=True,
    colors=colors,
    max=5,
    text_template="points",
)


@btn_1.click
def enable_btn_click():
    rate_1.enable() if rate_1.is_disabled else rate_1.disable()


card_1 = Card("Disabled rate", content=Container([rate_1, btn_1]))


########################### exmaple #2 ###########################

rate_2 = Rate(
    text_color="#656565",
    allow_half=True,
    value=4,
    show_text=True,
    colors=colors,
)

btn_2 = Button("Set value")
input_num = InputNumber(value=rate_2.get_value(), min=0, max=5, step=0.1)


@btn_2.click
def set_value_btn_click():
    new_value = input_num.get_value()
    rate_2.set_value(new_value)


card_2 = Card("Set rating", content=Container([rate_2, input_num, btn_2]))


########################### exmaple #3 ###########################

text_input = Input()
text_field = Field(
    content=text_input,
    title="Enter texts for rate",
    description="Enter 5 string values separated by commas",
)
text = Text(status="text")
btn_3 = Button("Set texts")

rate_3 = Rate(
    texts=infos,
    text_color="#656565",
    show_text=True,
    colors=colors,
    void_color="#F6568E",
)


card_3 = Card(
    "Rate",
    content=Container([rate_3, text, text_field, btn_3]),
)


@rate_3.value_changed
def rate_changed(value):
    text.text = f"Rate value: {value} stars"


@btn_3.click
def set_texts_btn_click():
    text = text_input.get_value()
    rates = [x.strip() for x in text.split(",")]
    if len(rates) != 5:
        return
    rate_3.set_texts(rates)


########################### App layout ###########################

layout = Container(widgets=[card_1, card_2, card_3])
app = sly.Application(layout=layout)
