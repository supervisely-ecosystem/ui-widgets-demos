import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import (
    Card,
    Container,
    CopyToClipboard,
    Editor,
    Text,
    TextArea,
    Input,
)

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()


editor = Editor('{ "Editor": 42 }', show_line_numbers=True)
input = Input(value="Input", size="large")
text = Text(text="Text", status="success")
text_area = TextArea(value="TextArea")
string = "Some string"

copytoclipboard1 = CopyToClipboard(content=editor)
copytoclipboard2 = CopyToClipboard(content=input)
copytoclipboard3 = CopyToClipboard(content=text)
copytoclipboard4 = CopyToClipboard(content=text_area)
copytoclipboard5 = CopyToClipboard(content=string)

card = Card(
    title="Copy To Clipboard",
    content=Container(
        [
            copytoclipboard1,
            copytoclipboard2,
            copytoclipboard3,
            copytoclipboard4,
            copytoclipboard5,
        ]
    ),
)
layout = Container(widgets=[card], direction="vertical")

app = sly.Application(layout=layout)
