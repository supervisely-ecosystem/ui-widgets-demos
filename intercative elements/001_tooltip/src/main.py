import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import (
    Card,
    Container,
    Button,
    Tooltip,
)

load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))
api = sly.Api()

# Create widgets, that will be shown on app initialization.
new_button = Button("Button")

# Create a Tooltip object.
tooltip = Tooltip("Just text", new_button)

# Put widgets into the Container.
main_container = Container(widgets=[tooltip])

# Create Card widget, which will contain widget with the 'tooltip'.
card = Card(title="Tooltip", content=main_container)

# Initialize the application.
app = sly.Application(layout=card)

# Set the multiline text in 'tooltip'
tooltip.set_content(["set", "content"])

# Set where to show a 'tooltip' around the element
tooltip.set_placement("right-end")

# Change 'tooltip' offset
tooltip.set_offset(10)

# Change 'tooltip' animation
tooltip.set_transition("el-fade-in")

# Hide arrow for 'tooltip'
tooltip.set_arrow_visibility(False)

# Set 'tooltip' opening delay in milliseconds
tooltip.set_open_delay(2000)

# Set 'tooltip' hide delay in milliseconds
tooltip.set_hide_after(4000)
