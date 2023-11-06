import os
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, Dialog, Text

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()


dialog_text = Text(text="Hello world!", status="text", font_size=32)
close_dialog_btn = Button("Click me!")
dialog_container = Container([dialog_text, close_dialog_btn])

dialog = Dialog(title="Dialog window", content=dialog_container, size="small")
open_dialog_btn = Button("Open dialog")

card = Card(title="Dialog", content=open_dialog_btn)
app = sly.Application(layout=Container([card, dialog]))


@open_dialog_btn.click
def show_dialog():
    dialog.show()


@close_dialog_btn.click
def hide_dialog():
    dialog.hide()
