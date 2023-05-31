import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, ColorPicker, Text

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api: sly.Api = sly.Api.from_env()


color_picker_hex = ColorPicker()
color_picker_hex_a = ColorPicker(show_info=True, color_format='hex', show_alpha=True)

color_picker_hsl = ColorPicker(show_info=True, color_format='hsl')
color_picker_hsl_a = ColorPicker(show_info=True, color_format='hsl', show_alpha=True)

color_picker_hsv = ColorPicker(color_format='hsv')
color_picker_hsv_a = ColorPicker(color_format='hsv', show_info=True, show_alpha=True)

color_picker_rgb = ColorPicker(color_format='rgb')
color_picker_rgb_a = ColorPicker(color_format='rgb', show_info=True, show_alpha=True)

card = Card(
    "Color Picker",
    content=Container([
        color_picker_hex,
        color_picker_hex_a,
        color_picker_hsl,
        color_picker_hsl_a, 
        color_picker_hsv,
        color_picker_hsv_a,
        color_picker_rgb, 
        color_picker_rgb_a,
    ]),
)

layout = Container(widgets=[card])
app = sly.Application(layout=layout)