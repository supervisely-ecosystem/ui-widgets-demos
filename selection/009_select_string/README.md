# Select String

## Introduction

**`SelectString`** widget in Supervisely is a dropdown menu that allows users to select a single string value from a list of predefined options. It is commonly used when a specific string value is required as input, such as when selecting a specific class name or annotation type. Selected value can be accessed programmatically in the code.

[Read this tutorial in developer portal.](https://developer.supervisely.com/app-development/widgets/selection/selectstring)

## Function signature

```python
SelectString(
    values=["cat", "dog","horse", "sheep", "squirrel"],
    labels=None,
    filterable=False,
    placeholder="select",
    size=None,
    multiple=False,
    widget_id=None,
)
```

![default](https://user-images.githubusercontent.com/79905215/223374487-566d4ff7-ac2e-40b8-afca-44b9c3e21ec9.png)

## Parameters

|     Parameters     |                        Type                         |                     Description                     |
| :----------------: | :-------------------------------------------------: | :-------------------------------------------------: |
|      `values`      |                     `List[str]`                     | Determine list of strings for `SelectString` widget |
|      `labels`      |                `Optional[List[str]]`                |           Determine list of label strings           |
|    `filterable`    |                  `Optional[bool]`                   |        Whether `SelectString` is filterable         |
|   `placeholder`    |                   `Optional[str]`                   |                  Input placeholder                  |
|       `size`       | `Optional[Literal["large", "small", "mini", None]]` |                    Size of input                    |
|     `multiple`     |                  `Optional[bool]`                   |        Whether multiple-select is activated         |
| `items_right_text` |                     `List[str]`                     |    Determine text on the right side of each item    |
|   `items_links`    |                     `List[str]`                     |     Display help text with links for each item      |
|    `widget_id`     |                   `Optional[str]`                   |                  ID of the widget                   |

### values

Determine list of strings for `SelectString` widget.

**type:** `List[str]`

```python
select_string = SelectString(["cat", "dog","horse", "sheep", "squirrel"])
```

![default](https://user-images.githubusercontent.com/79905215/223374487-566d4ff7-ac2e-40b8-afca-44b9c3e21ec9.png)

### labels

Determine list of label strings.

**type:** `List[str]` or `None`

**default value:** `None`

```python
select_string = SelectString(
    ["string1", "string2", "string3"], labels=["label1", "label2", "label3"]
)
```

![labels](https://user-images.githubusercontent.com/79905215/223374951-a6dd4363-fa30-49ce-a799-c9e41a81294a.png)

### filterable

Whether `SelectString` is filterable.

**type:** `Optional[bool]`

**default value:** `False`

```python
select_string = SelectString(
    ["cat", "dog", "horse"],
    filterable=True,
)
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/79905215/223085189-dc9eb603-b41a-4b62-bd92-7cb18674c4b8.gif" alt="filterable" />
</p>

### placeholder

Input placeholder.

**type:** `Optional[str]`

**default value:** `"select"`

```python
select_string = SelectString(
    ["cat", "dog", "horse"],
    filterable=True,
    placeholder="Select string please",
)
```

![placeholder](https://user-images.githubusercontent.com/79905215/223085874-976cf6a9-ebfe-4330-9941-aa93e51246a8.png)

### size

Size of input.

**type:** `Optional[Literal["large", "small", "mini", None]]`

**default value:** `None`

```python
select_string = SelectString(["cat"])
select_string_mini = SelectString(["cat"], size="mini")
select_string_small = SelectString(["cat"], size="small")
select_string_large = SelectString(["cat"], size="large")
```

![size](https://user-images.githubusercontent.com/120389559/222192756-5d997539-615a-441f-b854-3155b0a8320c.png)

### multiple

Whether multiple-select is activated.

**type:** `Optional[bool]`

**default value:** `False`

```python

select_string = SelectString(
    values=["cat", "dog","horse", "sheep", "squirrel"],
    multiple=True,
)
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/79905215/223376026-d98243ed-7b43-476c-9219-9955aba2809a.gif" alt="multiple" />
</p>

### items_right_text

Determine text on the right side of each item.

**type:** `List[str]` or `None`

**default value:** `None`

```python
select_string = SelectString(
    values=["cat", "dog", "horse"],
    items_right_text=["cat", "dog", "horse"],
)
```

![right_text](https://user-images.githubusercontent.com/79905215/223087480-acbed850-3ffa-47df-8b63-0f9fd1c08668.png)

### items_links

Display help text with links for each item.

**type:** `List[str]` or `None`

**default value:** `None`

```python
images = api.image.get_list(60402)

select_string = SelectString(
    values=[sly.fs.get_file_name(image.name) for image in images],
    items_links=[image.full_storage_url for image in images],
)
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/79905215/223114067-37fd261d-9968-42ac-bd23-0676fbdd34e2.gif" alt="item_links" />
</p>

### widget_id

ID of the widget.

**type:** `Optional[str]`

**default value:** `None`

## Methods and attributes

|                                        Attributes and Methods                                         | Description                                                |
| :---------------------------------------------------------------------------------------------------: | ---------------------------------------------------------- |
|                                             `get_value()`                                             | Return selected item value.                                |
| `set(values: List[str], labels: Optional[List[str]] = None, right_text: Optional[List[str]] = None,)` | Define string options to widget.                           |
|                                             `get_items()`                                             | Return list of items from widget.                          |
|                                           `@value_changed`                                            | Decorator function is handled when input value is changed. |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/selection/009_select/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/selection/009_select/src/main.py)

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

### Get Dataset ID from environment variables

```python
dataset_id = sly.env.dataset_id()
```

### Get images infos from current dataset

```python
images = api.image.get_list(dataset_id=dataset_id)
```

### Create `Image` widget we will use in UI in this tutorial for demo

```python
image = Image()
```

### Initialize `SelectString` widget

```python
select_string = SelectString(
    values=[img.name for img in images],
    items_links=[img.full_storage_url for img in images],
)
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card = Card(
    title="Select string",
    content=Container(
        [select_string, image],
        direction="horizontal",
        fractions=[1, 1],
    ),
)

layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```

### Add functions to control widget from code

```python
@select_string.value_changed
def display_select_string(value):
    if value is not None:
        img = api.image.get_info_by_name(dataset_id, value)
        image.set(url=img.full_storage_url)
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/79905215/223118592-f80e745b-38ea-482e-8c50-d6638f542b68.gif" alt="layout" />
</p>
