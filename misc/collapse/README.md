# Collapse

## Introduction

In this tutorial you will learn how to use `Collapse` widget in Supervisely app.

<!-- [Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/slider) -->

## Function signature

```python
Collapse(
    labels=['Description', 'Widget1'],
    contents=[text, my_widget],
    accordion=False,
    widget_id=None,
)
```

## Parameters

| Parameters  |            Type            |                                 Description                                  |
| :---------: | :------------------------: | :--------------------------------------------------------------------------: |
|  `labels`   |        `List[str]`         |                               Collapses titles. Only distinct values are allowed.                              |
| `contents`  | `List[Union[str, Widget]]` |          Collapses content. Raw text or other widgets are possible.          |
| `accordion` |           `bool`           | Whether to activate accordion mode. If true, only one panel could be active. |
| `widget_id` |           `str`            |                               Id of the widget                               |

### labels

Determine `Collapse` titles.

**type:** `List[str]`


### contents

Determine `Collapse` content.

**type:** `List[Union[str, Widget]]`

```python
labels = ['Description', 'Table']

table_data = {
    "col1": [1, 2, 3],
    "col2": [2, 3, 4]
}

tabel = Table(data=table_data)  # table widget
contents = [
    'Text sample',
    table,
]

slider = Slider(
    labels=labels,
    contents=contents,
)
```

![accordion_false](https://user-images.githubusercontent.com/87002239/228161946-279b1647-e765-43cc-8130-796a6214309b.gif)


### accordion

Activate accordion mode. If true, only one panel could be active.

**type:** `bool`

**default value:** `False`

```python
slider = Slider(
    labels=labels,
    contents=contents,
    accordion=True,
)
```

![accordion_true](https://user-images.githubusercontent.com/87002239/228161318-9a734351-0b9d-4c73-a27c-3e88fc30d52a.gif)


### widget_id

ID of the widget.

**type:** `str`

**default value:** `None`

## Methods and attributes

|              Attributes and Methods              | Description                                                                 |
| :----------------------------------------------: | --------------------------------------------------------------------------- |
| `set_active_panel(value: Union[str, List[str]])` | Set `Collapse` active panel. In accordion mode, only strings are permitted. |
|               `get_active_panel()`               | Return name/names of active panel(s).                                       |
|                  `get_items()`                   | Return panels description.                                                  |
|     `set_items(value: List[Collapse.Item])`      | Set `Collapse` items.                                                       |
|     `add_items(value: List[Collapse.Item])`      | Extends list of `Collapse` items. |

## Mini App Example

<!-- You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/misc/slider/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/misc/slider/src/main.py) -->

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Collapse, Table
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Initialize `Collapse` content and widget

```python
table_data = {
    "index": [0, 1, 2],
    "x": [1, 2, 3],
    "-x^2": [-1, -4, -9],
}

table = Table(data=df)
sample_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
collapse = Collapse(
    labels=["Collapse with text", "Collapse with table"],
    contents=[sample_text, table],
    accordion=False,
)
```

### Add new item manually

```python
collapse.add_items([Collapse.Item("Random added item", title="Added item")])
```

### Create text widget

This text widget will show the collapse widget's current active item(s).

```python
text = Text("Active item: Collapse with text")
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card = Card(title="Slider", content=Container([collapse]))
layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```

### Update text widget state

`collapse.value_changed` decorator handle collapse changes and pass active collapse items to `show_active_item` function. 

```python
@collapse.value_changed
def show_active_item(value):
    if isinstance(value, list):
        act_items = ", ".join(value)
    text.text = f"Active item: {act_items}"
```

`tbl.click` decorator handle table changes (sorting, searching etc.).
```
@tbl.click
def handle_table_button(datapoint: sly.app.widgets.Table.ClickedDataPoint):
    if datapoint.button_name is None:
        return
```