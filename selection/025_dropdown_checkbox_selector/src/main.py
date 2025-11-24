import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Text, DropdownCheckboxSelector


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))
api = sly.Api()


items = [
    DropdownCheckboxSelector.Item(
        id="item1", name="First Item", description="Description for first item"
    ),
    DropdownCheckboxSelector.Item(
        id="item2", name="Second Item", description="Description for second item"
    ),
    DropdownCheckboxSelector.Item(
        id="item3", name="Third Item", description="Description for third item"
    ),
    DropdownCheckboxSelector.Item(id="item4", name="Fourth Item"),
]

checkbox_selector = DropdownCheckboxSelector(items=items, label="Select items:", multiple=True)

selection_changed_info = Text(status="info")
selection_changed_info.hide()


@checkbox_selector.value_changed
def selection_changed(selected_items):
    if selected_items:
        try:
            item_names = [item.name for item in selected_items]
            text = f"Selected items: {', '.join(item_names)}"
            selection_changed_info.text = text
            selection_changed_info.show()
        except Exception as e:
            selection_changed_info.text = f"Error getting selected items: {str(e)}"
            selection_changed_info.show()
    else:
        selection_changed_info.text = "No items selected"
        selection_changed_info.show()


card = Card(
    title="DropdownCheckboxSelector Demo",
    content=Container(widgets=[checkbox_selector, selection_changed_info]),
)

layout = Container(widgets=[card])
app = sly.Application(layout=layout)
