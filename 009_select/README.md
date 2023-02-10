# Select

## Introduction

This widget is a select type input, clicking on it can be processed from python code. In this tutorial you will learn how to use `Select` widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/Select)

## Function signature

```python
Select(items=None, groups=None, filterable=False, placeholder="select", size=None, multiple=False, widget_id=None)
```

![default](https://user-images.githubusercontent.com/120389559/217835655-5a888104-dd74-4dc9-b68f-88ab956898f3.png)

## Parameters

| Parameters  |               Type                |             Description              |
| :---------: | :-------------------------------: | :----------------------------------: |
|    items    |         List[Select.Item]         |    list of `Select.Item` widgets     |
|   groups    |        List[Select.Group]         |    list of `Select.Group` widgets    |
| filterable  |               bool                |     whether Select is filterable     |
| placeholder |                str                |             placeholder              |
|    size     | Literal["large", "small", "mini"] |            size of input             |
|  multiple   |               bool                | whether multiple-select is activated |
|  widget_id  |                int                |           id of the widget           |

### items

Determine list of `Select.Item` widgets.

**type:** `List[Select.Item]`

**default value:** `None`

### groups

Determine list of `Select.Group` widgets.

**type:** `List[Select.Group]`

**default value:** `None`

**Function signature**

Prepare select items and groups:

```python
animals_domestic = [
    Select.Item(value="cat", label="cat"),
    Select.Item(value="dog", label="dog"),
]
animals_wild = [
    Select.Item(value="squirrel", label="squirrel"),
]
```

Initialize widget with given items:

```python
select_items = Select(
    items=animals_domestic + animals_wild,
    filterable=True,
)
```

![items](https://user-images.githubusercontent.com/120389559/217835655-5a888104-dd74-4dc9-b68f-88ab956898f3.png)

or initialize widget with given groups of items:

```python
groups = [
    Select.Group(label="domestic", items=animals_domestic),
    Select.Group(label="wild", items=animals_wild),
]

select_groups = Select(groups=groups)
```

![groups](https://user-images.githubusercontent.com/120389559/217837265-105f89c7-3c12-4232-94c8-59692bfb160a.png)

### filterable

Whether Select is filterable.

**type:** `bool`

**default value:** `false`

### placeholder

Placeholder.

**type:** `str`

**default value:** `select`

### size

Size of input.

**type:** `Literal["large", "small", "mini"]`

**default value:** `None`

### multiple

Whether multiple-select is activated.

**type:** `bool`

**default value:** `false`

```python
select_items = Select(
    items=animals_domestic + animals_wild,
    multiple=True,
)
```

![multiple](https://user-images.githubusercontent.com/120389559/218096915-b300c3d6-7a17-4cca-befe-36a2ee4828de.gif)

### widget_id

ID of the widget.

**type:** `int`

**default value:** `None`

**Methods and attributes**

|                          Attributes and Methods                           | Description                                                      |
| :-----------------------------------------------------------------------: | ---------------------------------------------------------------- |
|                               `get_value()`                               | Return selected item value.                                      |
| `set(items: List[Select.Item] = None, groups: List[Select.Group] = None)` | Set select input items or group of items. items.                 |
|                               `get_items()`                               | Return list of items from widget.                                |
|                             `@value_changed`                              | Decorator function is handled when radio input value is changed. |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/009_select/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/009_select/src/main.py)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Select
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Prepare items or group of items for `Select` widget using `Select.Item` and `Select.Group`

```python
animals_domestic = [
    Select.Item(value="cat", label="cat"),
    Select.Item(value="dog", label="dog"),
    Select.Item(value="horse", label="horse"),
    Select.Item(value="sheep", label="sheep"),
]
animals_wild = [
    Select.Item(value="squirrel", label="squirrel"),
]
```

```python
groups = [
    Select.Group(label="domestic", items=animals_domestic),
    Select.Group(label="wild", items=animals_wild),
]
```

### Initialize `Select` widget

```python
select_items = Select(
    items=animals_domestic + animals_wild,
    filterable=True,
)
```

```python
select_groups = Select(groups=groups)
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card = Card(
    title="Select",
    content=Container(widgets=[select_items, select_groups]),
)

layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```

![layout](https://user-images.githubusercontent.com/120389559/218097482-c5d94009-036c-43dd-85c4-f8f6c413f984.gif)
