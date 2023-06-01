import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Transfer, Container, Text

load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))
api = sly.Api()

# Preparing list of items as Transfer.Item objects.
domestic_animals = [
    Transfer.Item(key="cat", label="Cat", disabled=True),
    Transfer.Item(key="dog"),
    Transfer.Item(key="cow"),
    Transfer.Item(key="sheep"),
]

# Preparing list of items as strings, which will be converted to Transfer.Item objects.
wild_animals = ["mouse", "bird"]

# Initializing Transfer widget with first list of items.
transfer = Transfer(
    # List of all items for the widget (both left and right).
    items=domestic_animals,
    # List of items that will in the right list when the widget is initialized.
    transferred_items=["cat", "cow"],
    # Making the widget filterable.
    filterable=True,
    # Setting the placeholder for the filter input.
    filter_placeholder="Search...",
    # Setting the title for the both lists.
    titles=["Available", "Transferred"],
    # Setting the names for the buttons.
    button_texts=["Remove", "Add"],
    # Setting the items which will be checked in the left list when the widget is initialized.
    left_checked=["dog"],
    # Setting the items which will be checked in the right list when the widget is initialized.
    right_checked=["cow"],
)

# Adding new items to the widget.
transfer.add(wild_animals)

# Updating the transferred items, which will be shown in the right list.
# Note: if you want to ADD items (not REPLACE them), don't forget to pass the old transferred items to the method.
transfer.set_transferred_items(transfer.get_transferred_items() + ["mouse"])

# Printing the keys of items in the left list.
print("Keys of items in the left list ", transfer.get_untransferred_items())
# Printing the keys of items in the right list.
print("Keys of items in the right list ", transfer.get_transferred_items())

# Removing item from widget by its key.
transfer.remove(["sheep"])

# Printing the keys of all items in the widget.
print("Keys of all items in the widget ", transfer.get_items_keys())

# Preparing text widget to show the message about the value change.
value_changed_message = Text(status="info")


# Creating decorated function to show the current state of the widget.
@transfer.value_changed
def show_message_with_keys(Items):
    # The Items object is a named tuple containing two lists:
    # keys of items in the left list and keys of items in the right list.
    value_changed_message.text = (
        f"Left list: {Items.untransferred_items}. Right list: {Items.transferred_items}."
    )


# Creating Card widget, which will contain the Transfer widget and the Text widget.
card = Card(title="Transfer", content=Container(widgets=[transfer, value_changed_message]))
# Creating the application layout.
layout = Container(widgets=[card])
# Initializing the application.
app = sly.Application(layout=layout)
