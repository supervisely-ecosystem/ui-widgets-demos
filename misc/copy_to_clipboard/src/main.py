import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import (
    Card,
    Container,
    CopyToClipboard,
    Button,
    Editor,
    Text,
    TextArea,
    Input,
)


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

button_text = Button(text="Get text")

editor = Editor('{ "value": 10 }', show_line_numbers=False)
text = Text(text="some text", status="success")
text_area = TextArea(value="some text " * 10, readonly=True)
input = Input(value="Start input value", size="large")
string = "Only string"

copytoclipboard = CopyToClipboard(content=editor)

card = Card(
    title="Copy To Clipboard",
    content=Container([copytoclipboard]),
)

layout = Container(widgets=[card], direction="vertical")
app = sly.Application(layout=layout)
