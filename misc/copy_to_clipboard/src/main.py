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

editor = Editor('{ "value": 10 }', show_line_numbers=True)
text = Text(text="Text", status="success")
text_area = TextArea(value="TextArea")
input = Input(value="Input", size="large")
string = "Only string"

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

print(
                copytoclipboard1.text,
            copytoclipboard2.text,
            copytoclipboard3.text,
            copytoclipboard4.text,
            copytoclipboard5.text,
)