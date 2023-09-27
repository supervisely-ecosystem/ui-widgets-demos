import os
import supervisely as sly
from supervisely.app.widgets import Button, Card, Container, Flexbox, Input, MessageBox
from dotenv import load_dotenv

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

message_box = MessageBox(title="Message Box title", message="Message Box message")

button_open = Button("open message")
button_set = Button("set")
buttons = Flexbox([button_open, button_set])

title_input = Input(placeholder="Enter title")
message_input = Input(placeholder="Enter message")
type_input = Input(placeholder="Enter type")
inputs  = Container(widgets=[title_input, message_input, type_input])

card = Card(
    "Compare Images",
    content=Container([message_box, inputs, buttons]),
)

layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@button_open.click
def on_click():
    message_box.open()


@button_set.click
def on_click():
    data = {}
    if title_input.get_value() != "":
        data["title"] = title_input.get_value()
    if message_input.get_value() != "":
        data["message"] = message_input.get_value()
    if type_input.get_value() != "":
        data["type"] = type_input.get_value()
    message_box.set(data)
