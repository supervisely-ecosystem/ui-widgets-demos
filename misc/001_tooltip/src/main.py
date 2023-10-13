import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import (
    Card,
    Container,
    Button,
    Tooltip,
)

# load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))
api = sly.Api()

# Create widgets, that will be shown on app initialization.
new_button = Button("Button")

# Create a tooltip.
tooltip = Tooltip("Just text", new_button)

# Put widgets into the Container.
main_container = Container(widgets=[tooltip])

# Creating Card widget, which will contain widget with the tooltip.
card = Card(title="Tooltip", content=main_container)

# Initializing the application.
app = sly.Application(layout=card)

# To set multiline text
tooltip.set_content(["set", "content"])

# Set where to show tooltip around the element
tooltip.set_placement("right-end")

# To change tooltip offset
tooltip.set_offset(10)

# To change tooltip animation
tooltip.set_transition("el-fade-in")

# To set tooltip opening delay in milliseconds
tooltip.set_open_delay(2000)

# To disable tooltip
tooltip.set_disabled(False)
