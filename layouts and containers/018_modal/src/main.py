import os
import supervisely as sly
from supervisely.app.widgets import Card, Container, Input, Text, Modal, Button
from dotenv import load_dotenv


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

input_widget = Input("Enter value")
text_widget = Text("This is modal content")
button = Button("Open modal")

# Create modal with multiple widgets
modal = Modal(title="My Modal Window", widgets=[text_widget, input_widget], size="small")

container = Container(widgets=[modal, button])

layout = Card(
    title="Modal Example",
    content=container,
)
app = sly.Application(layout=layout)


@button.click
def on_button_click():
    modal.show()


@modal.value_changed
def on_value_changed(value):
    print(f"Modal value changed: {value}")
    print("Modal closed")
