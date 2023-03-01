# Select String

## Introduction

In this tutorial you will learn how to use `SelectString` widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/selectstring)

## Function signature

```python
SelectString(values, labels=None, filterable=False, placeholder="select", size=None, multiple=False, widget_id=None)
```

![default](https://user-images.githubusercontent.com/120389559/217835655-5a888104-dd74-4dc9-b68f-88ab956898f3.png)

## Parameters

|  Parameters   |                   Type                    |             Description              |
| :-----------: | :---------------------------------------: | :----------------------------------: |
|   `values`    |                `List[str]`                |           List of strings            |
|   `labels`    |                `List[str]`                |           List of strings            |
| `filterable`  |                  `bool`                   |    Whether `Select` is filterable    |
| `placeholder` |                   `str`                   |             Placeholder              |
|    `size`     | `Literal["large", "small", "mini", None]` |            Size of input             |
|  `multiple`   |                  `bool`                   | Whether multiple-select is activated |
|  `widget_id`  |                   `str`                   |           Id of the widget           |

### values

Determine list of strings for `SelectString` widget.

**type:** `List[str]`

```python
select_string = SelectString(["string1", "string2", "string3"])
```

![default](https://user-images.githubusercontent.com/120389559/217835655-5a888104-dd74-4dc9-b68f-88ab956898f3.png)

### labels

Determine list of label strings.

**type:** `List[str]`

**default value:** `None`

```python
select_string = SelectString(
    ["string1", "string2", "string3"], labels=["label1", "label2", "label3"]
)
```

![labels](https://user-images.githubusercontent.com/120389559/222191338-6db067c2-0a79-4c9f-b3e5-fa9136b33b0d.gif)

### filterable

Whether `SelectString` is filterable.

**type:** `bool`

**default value:** `false`

### placeholder

Placeholder.

**type:** `str`

**default value:** `select`

### size

Size of input.

**type:** `Literal["large", "small", "mini", None]`

**default value:** `None`

```python
select_string = SelectString(["cat"])
select_string_mini = SelectString(["cat"], size="mini")
select_string_small = SelectString(["cat"], size="small")
select_string_large = SelectString(["cat"], size="large")

card = Card(content=Container(widgets=[select_string, select_string_mini, select_string_small, select_string_large]))
```

![size](https://user-images.githubusercontent.com/120389559/222192756-5d997539-615a-441f-b854-3155b0a8320c.png)

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

**type:** `str`

**default value:** `None`

## Methods and attributes

|                          Attributes and Methods                           | Description                                 |
| :-----------------------------------------------------------------------: | ------------------------------------------- |
|                               `get_value()`                               | Return selected item value.                 |
| `set(items: List[Select.Item] = None, groups: List[Select.Group] = None)` | Set `Select` input items or group of items. |
|                               `get_items()`                               | Return list of items from widget.           |
|                             `value_changed()`                             | Handled when input value is changed.        |

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

### Prepare items and groups of items for `Select` widget using `Select.Item` and `Select.Group`

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
