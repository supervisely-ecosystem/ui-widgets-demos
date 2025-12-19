# DropdownCheckboxSelector

## Introduction

The **`DropdownCheckboxSelector`** widget in Supervisely is a user interface element that enables users to select multiple items from a dropdown list with checkboxes. It displays items in a dropdown format where each item can be independently selected or deselected. The widget supports custom labels, descriptions for items, and includes event handlers that activate when the selection changes.

## Function signature

```python
DropdownCheckboxSelector(
    items: List[Item],
    label: str = None,
    widget_id: str = None,
    multiple: bool = True
)
```

![default](https://github.com/supervisely-ecosystem/ui-widgets-demos/releases/download/v0.0.2/Screenshot.from.2025-11-24.16-30-32.png)

## Parameters

| Parameters  |      Type       |                        Description                        |
| :---------- | :-------------: | :-------------------------------------------------------: |
| `items`     |  `List[Item]`   |         List of items to display in the dropdown.         |
| `label`     | `Optional[str]` | Label text displayed above the widget. Default is `None`. |
| `widget_id` |      `str`      |              An optional ID for the widget.               |
| `multiple`  |     `bool`      |       Allow multiple selections. Default is `True`.       |

### items

List of items to display in the dropdown selector.
Each item is created using the `DropdownCheckboxSelector.Item` class.

**type:** `List[Item]`

Create items for the selector:

```python
items = [
    DropdownCheckboxSelector.Item(id="item1", name="First Item", description="Description for first item"),
    DropdownCheckboxSelector.Item(id="item2", name="Second Item", description="Description for second item"),
    DropdownCheckboxSelector.Item(id="item3", name="Third Item", description="Description for third item"),
    DropdownCheckboxSelector.Item(id="item4", name="Fourth Item"),
]
```

### label

Label text displayed above the widget.

**type:** `Optional[str]`

**default value:** `None`

Set a custom label:

```python
widget = DropdownCheckboxSelector(items=items, label="Select items:")
```

### widget_id

An optional ID for the widget.

**type:** `str`

**default value:** `None`

Initialize the widget with an ID:

```python
widget = DropdownCheckboxSelector(items=items, widget_id="dropdown_selector")
```

### multiple

Allow multiple item selection.

**type:** `bool`

**default value:** `True`

Allow single selection only:

```python
widget = DropdownCheckboxSelector(items=items, multiple=False)
```

## Methods and attributes

|  Methods and Attributes  |                 Description                  |
| :----------------------: | :------------------------------------------: |
|     `get_selected()`     |    Get currently selected items as list.     |
| `select(ids: List[str])` |          Select items by their IDs.          |
| `set(items: List[Item])` |      Update the widget with new items.       |
|  `value_changed(func)`   | Decorator to handle selection change events. |

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Text, DropdownCheckboxSelector
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))
api = sly.Api()
```

### Initialize the `DropdownCheckboxSelector` widget

Let's create items and initialize the `DropdownCheckboxSelector` widget:

```python
items = [
    DropdownCheckboxSelector.Item(id="item1", name="First Item", description="Description for first item"),
    DropdownCheckboxSelector.Item(id="item2", name="Second Item", description="Description for second item"),
    DropdownCheckboxSelector.Item(id="item3", name="Third Item", description="Description for third item"),
    DropdownCheckboxSelector.Item(id="item4", name="Fourth Item"),
]

checkbox_selector = DropdownCheckboxSelector(
    items=items,
    label="Select items:",
    multiple=True
)
```

### Create an event handler for the `DropdownCheckboxSelector` widget

Now, let's create an event handler for the DropdownCheckboxSelector widget, when items are selected.

```python
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
```

### Create app layout

Prepare a layout for the app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card = Card(
    title="DropdownCheckboxSelector Demo",
    content=Container(widgets=[checkbox_selector, selection_changed_info]),
)

layout = Container(widgets=[card])
```

### Create an app using the layout

Create an app object with the layout parameter.

```python
app = sly.Application(layout=layout)
```
