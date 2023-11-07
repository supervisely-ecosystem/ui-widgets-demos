import os
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, ColorPicker, Text

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api: sly.Api = sly.Api.from_env()

color_picker = ColorPicker(show_alpha=False, color_format="hex", compact=True)
color_info = Text("Current color: #20A0FF", "info")
text = Text("Hello, World!", color="#20A0FF", font_size=22)

layout = Card(
    "Color Picker",
    content=Container([color_picker, color_info, text]),
)

app = sly.Application(layout=layout)


@color_picker.value_changed
def on_color_change(color):
    color_info.set(f"Current color: {color}", "info")
    text.color = color
