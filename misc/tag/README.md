# Tag

## Introduction

**`Tag`** widget in Supervisely is a widget that allows users to display tag on the UI.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/widgets/misc/tag)

## Function signature

```python
Tag(text="", type=None, hit=False, color="", widget_id=None)
```

## Parameters

| Parameters  |                                Type                                |              Description               |
| :---------: | :----------------------------------------------------------------: | :------------------------------------: |
|   `text`    |                               `str`                                |               `Tag` text               |
|   `type`    | `Literal["primary", "gray", "success", "warning", "danger", None]` |              `Tag` theme               |
|    `hit`    |                               `bool`                               | Whether `Tag` has a highlighted border |
|   `color`   |                               `str`                                |     Background color of the `Tag`      |
| `widget_id` |                               `str`                                |            ID of the widget            |

### text

Determine `Tag` text.

**type:** `str`

```python
tag = Tag(text="Tag example")
```

![text](https://user-images.githubusercontent.com/120389559/226908793-2a620b84-0b72-4231-8639-ce1f3a458f89.png)

### type

Determine `Tag` theme.

**type:** `Literal["primary", "gray", "success", "warning", "danger", None]`

**default value:** `None`

```python
tag = Tag(text="Tag example", type="success")
```

![type](https://user-images.githubusercontent.com/120389559/226909285-8ad976b9-e16a-4ebc-b0f4-f76e9b7fb7c2.png)

### hit

Determine whether `Tag` has a highlighted border.

**type:** `bool`

**default value:** `False`

```python
tag = Tag(text="Tag example", hit=True, type="success")
```

![hit](https://user-images.githubusercontent.com/120389559/226909880-f21382df-01de-42fc-9c0d-81dad8522e7c.png)

### color

Determine background color of the `Tag`.

**type:** `str`

**default value:** `""`

```python
tag = Tag(text="Tag example", color="#E414D7", type="success")
```

![color](https://user-images.githubusercontent.com/120389559/226910422-d0dc98ec-40da-4c11-adb3-69feff45e57a.png)

### widget_id

ID of the widget

**type:** `str`

**default value:** `None`

## Methods and attributes

|                            Attributes and Methods                             | Description               |
| :---------------------------------------------------------------------------: | ------------------------- |
|                            `set_text(value: str)`                             | Set `Tag` text.           |
|                                 `get_text()`                                  | Return `Tag` text.        |
| `set_type(value: Literal["primary", "gray", "success", "warning", "danger"])` | Set `Tag` type.           |
|                                 `get_type()`                                  | Return `Tag` type.        |
|                           `is_border_highlighted()`                           | Return `Tag` `hit` value. |
|                        `enable_border_highlighting()`                         | Set `hit` to `True`.      |
|                        `disable_border_highlighting()`                        | Set `hit` to `False`.     |
|                                 `get_color()`                                 | Return `Tag` color.       |
|                            `set_color(value: str)`                            | Set `Tag` color.          |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/misc/tag/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/misc/tag/src/main.py)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Tag
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Initialize `Tag` widgets

```python
tag = Tag(text="Tag")

all_tag_types = [tag]
for tag_type in ["primary", "gray", "success", "warning", "danger"]:
    curr_tag = Tag(text=f"Tag {tag_type}", type=tag_type)
    all_tag_types.append(curr_tag)
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card = Card(
    "Tag",
    content=Container(widgets=all_tag_types, direction="horizontal"),
)

layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```

![layout_tag](https://user-images.githubusercontent.com/120389559/226914574-394c3629-4816-42c8-8a5a-82aec34239ad.png)
