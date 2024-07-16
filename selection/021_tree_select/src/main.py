import os

import supervisely as sly
from dotenv import load_dotenv
from typing import List
from supervisely.app.widgets import Card, TreeSelect, Container, Text, Button, Flexbox

load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))
api = sly.Api()

# Preparing list of TreeSelect.Item objects for the widget.
domestic_animals = [
    TreeSelect.Item(
        id="cat",
        label="Cat",
        children=[
            TreeSelect.Item(id="siamese", label="Siamese"),
            TreeSelect.Item(id="persian", label="Persian"),
        ],
    ),
    TreeSelect.Item(
        id="dog",
        label="Dog",
        children=[
            TreeSelect.Item(id="bulldog", label="Bulldog"),
            TreeSelect.Item(id="beagle", label="Beagle"),
        ],
    ),
    TreeSelect.Item(id="cow", label="Cow"),
    TreeSelect.Item(id="sheep", label="Sheep"),
]

# Ititializing TreeSelect widget without any items, since
# it's a common case when the data for the widget will be obtained
# in the process of the application work.
tree_select = TreeSelect(
    multiple_select=True,
    flat=True,
    always_open=False,
)

# Now, when some data is available, we can set it to the widget.
# When using the set_items method, the items will be replaced with the new ones.
tree_select.set_items(domestic_animals)

# Let's prepare a new list of items, which will be added dynamically to the widget.
wild_animals = [
    TreeSelect.Item(
        id="mouse",
        label="Mouse",
        children=[
            TreeSelect.Item(id="field_mouse", label="Field mouse"),
            TreeSelect.Item(id="house_mouse", label="House mouse"),
        ],
    ),
    TreeSelect.Item(id="bird", label="Bird"),
]

# And prepare a button, which will add the new items to the widget.
add_button = Button("Add wild animals")


# We also need to set the handler for the button click event.
@add_button.click
def add_wild_animals():
    print("Adding wild animals")
    tree_select.add_items(wild_animals)

    # Since we've added new items, we can disable the button to prevent adding the same items again.
    add_button.disable()


# Now, let's create a button, which will show selected items in UI.
# And create a simple text widget to show the selected items.
show_selected_button = Button("Show selected")
selected_info = Text(status="info")
# Since at the beginning no items are selected, we can hide the text widget.
selected_info.hide()


# Same as for the previous button, we need to set the handler for the click event.
@show_selected_button.click
def show_selected():
    print("Showing selected items")
    selected_items = tree_select.get_selected()
    if selected_items and isinstance(selected_items, list):
        # We need to check if the selected items is a list
        # since in not multiple select mode it will be a single item.
        # It's not necessary in this tutorial, since we're setting the multiple_select=True,
        # just remember about it in your applications.

        labels = ", ".join([item.label for item in selected_items])
        text = "Selected items: {}".format(labels)

        # Setting the text to the widget and showing it.
        selected_info.text = text
        selected_info.show()
    else:
        selected_info.hide()


# Now, let's create a event handler for the TreeSelect widget, when
# the value of the widget is changed.
value_changed_info = Text(status="info")
value_changed_info.hide()


@tree_select.value_changed
def new_items_selected(items: List[TreeSelect.Item]):
    print("Value changed")
    if items:
        # We're processing the event the same way as for the button click event.
        labels = ", ".join([item.label for item in items])
        text = "Value changed: {}".format(labels)

        # Setting the text to the widget and showing it.
        value_changed_info.text = text
        value_changed_info.show()
    else:
        value_changed_info.hide()


# Let's group our buttons in a Flexbox widget to make them look better.
buttons_flexbox = Flexbox(
    widgets=[add_button, show_selected_button],
)

# Creating Card widget, which will contain all the widgets.
card = Card(
    title="TreeSelect",
    content=Container(widgets=[buttons_flexbox, selected_info, value_changed_info, tree_select]),
)
# Creating the application layout.
layout = Container(widgets=[card])
# Initializing the application.
app = sly.Application(layout=layout)
