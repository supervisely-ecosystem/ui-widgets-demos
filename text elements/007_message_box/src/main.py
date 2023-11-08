import os
from dotenv import load_dotenv
import supervisely as sly
from supervisely.app.widgets import Card, Flexbox, MessageBox

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))


api = sly.Api()

message_box_info = MessageBox(
    title="Info",
    message="Lorem ipsum dolor sit amet ...",
    type="info",
    button_text="Info",
)

message_box_warning = MessageBox(
    title="Warning",
    message="Lorem ipsum dolor sit amet ...",
    type="warning",
    button_text="Warning",
)

message_box_error = MessageBox(
    title="Error",
    message="Lorem ipsum dolor sit amet ...",
    type="error",
    button_text="Error",
)

message_box_text = MessageBox(
    title="Text",
    message="Lorem ipsum dolor sit amet ...",
    type="text",
    button_text="Text",
)


card = Card(
    title="MessageBox",
    content=Flexbox(
        [message_box_info, message_box_warning, message_box_error, message_box_text],
        center_content=True,
    ),
)
layout = card

app = sly.Application(layout=layout)
