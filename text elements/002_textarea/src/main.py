import os
import supervisely as sly
from supervisely.app.widgets import Card, Container, TextArea, Button
from dotenv import load_dotenv
import random
import string


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()


button_random_text = Button(text="Generate random text")
button_clean_input = Button(text="Clean input")
buttons_container = Container(
    widgets=[button_random_text, button_clean_input], direction="horizontal"
)

text_area = TextArea()

card = Card(
    title="TextArea",
    content=Container(widgets=[text_area, buttons_container]),
)

layout = Container(widgets=[card], direction="vertical")
app = sly.Application(layout=layout)


@button_random_text.click
def random_text():
    random_text = "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(1000)
    )
    text_area.set_value(value=random_text)


@button_clean_input.click
def clear():
    text_area.set_value(value="")
