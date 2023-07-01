import os

from random import choice
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import (
    Card,
    ReloadableArea,
    Container,
    Text,
    Input,
    InputNumber,
    Checkbox,
    Button,
    Flexbox,
    Switch,
    Slider,
)

load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))
api = sly.Api()

# Create widgets, that will be shown on app initialization.
start_text = Text("Click a button to add or remove random widget.", status="info")
add_widget_button = Button("Add widget")
remove_widget_button = Button("Remove widget", button_type="danger")
buttons_flexbox = Flexbox([add_widget_button, remove_widget_button])

# Create a reloadable area.
reloadable_area = ReloadableArea()

# Put widgets into the Container.
main_container = Container(widgets=[start_text, buttons_flexbox])

# Add the Container to the reloadable area.
reloadable_area.set_content(main_container)


@add_widget_button.click
def add_widget():
    # Picking random widget from the list to add to the UI.
    random_widget = choice(
        [
            Input("Random input"),
            Checkbox("Random checkbox"),
            InputNumber(),
            Switch(),
            Slider(),
        ]
    )

    main_container._widgets.append(random_widget)

    # This is the most important part: we need to reload the ReloadableArea
    # to show the new widget in th UI.
    reloadable_area.reload()


@remove_widget_button.click
def remove_widget():
    if len(main_container._widgets) > 2:
        main_container._widgets.pop()

        # Same as above: we need to reload the ReloadableArea when removing the widget.
        reloadable_area.reload()


# Creating Card widget, which will contain the ReloadableArea widget.
card = Card(title="ReloadableArea", content=reloadable_area)

# Initializing the application.
app = sly.Application(layout=card)
