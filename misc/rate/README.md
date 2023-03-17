# Rate

## Introduction

**`Rate`** is a widget in Supervisely that allows for displaying stars rate on the UI.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/widgets/charts-and-plots/rate)

## Function signature

```python
Rate(
    max=5,
    colors=["#F7BA2A", "#F7BA2A", "#F7BA2A"],
    disabled=False,
    allow_half=False,
    texts=[],
    show_text=False,
    text_color="#1F2D3D",
    void_color="#C6D1DE",
    disabled_void_color="#EFF2F7",
    widget_id=None,
)
```

![rate_default](https://user-images.githubusercontent.com/120389559/225903196-c2d60aa6-529a-4874-aac0-41571d52135c.gif)

## Parameters

|      Parameters       |    Type     |              Description              |
| :-------------------: | :---------: | :-----------------------------------: |
|         `max`         |    `int`    |           Max rating score            |
|       `colors`        | `List[str]` |         Color array for icons         |
|      `disabled`       |   `bool`    |      Whether `Rate` is read-only      |
|     `allow_half`      |   `bool`    | Whether picking half start is allowed |
|        `texts`        | `List[str]` |              Text array               |
|      `show_text`      |   `bool`    |       Whether to display texts        |
|     `text_color`      |    `str`    |            Color of texts             |
|     `void_color`      |    `str`    |       Color of unselected icons       |
| `disabled_void_color` |    `str`    |  Color of unselected read-only icons  |
|      `widget_id`      |    `str`    |           ID of the widget            |

### max

Determine max rating score.

**type:** `int`

**default value:** `5`

```python
rate = Rate(max=15)
```

![max](https://user-images.githubusercontent.com/120389559/225904319-6b017a51-456d-4c12-bff6-b8467bc94630.png)

### colors

Determine color array for icons.

**type:** `List[str]`

**default value:** `["#F7BA2A", "#F7BA2A", "#F7BA2A"]`

```python
rate = Rate(colors=["#1414E4", "#2DE414", "#F7BA2A"])
```

![colors](https://user-images.githubusercontent.com/120389559/225905073-7c529057-7e7b-4617-8f2d-de17ea9252de.gif)

### disabled

Determine whether `Rate` is read-only.

**type:** `bool`

**default value:** `False`

```python
rate = Rate(disabled=True)
```

![disabled](https://user-images.githubusercontent.com/120389559/225905381-5b5455f9-b45e-4b0f-9b44-511445431981.png)

### allow_half

Determine whether picking half start is allowed.

**type:** `bool`

**default value:** `False`

```python
rate = Rate(allow_half=True)
```

![allow_half](https://user-images.githubusercontent.com/120389559/225905792-bc5fa368-abb0-41f7-b40a-938b7e5f08a5.gif)

### texts

Determine text array for each star.

**type:** `List[str]`

**default value:** `[]`

### show_text

Determine whether to display texts.

**type:** `bool`

**default value:** `False`

```python
rate = Rate(texts=infos, show_text=True)
```

![texts](https://user-images.githubusercontent.com/120389559/225906480-ce45b8ab-6af4-4444-b279-68691a6e98cd.gif)

### text_color

Determine color of texts.

**type:** `str`

**default value:** `"#1F2D3D"`

```python
rate = Rate(texts=infos, show_text=True, text_color="#E414BB")
```

![text_color](https://user-images.githubusercontent.com/120389559/225906932-fcb00268-f55a-4762-bf8e-2fe254609f01.png)

### void_color

Determine color of unselected icons.

**type:** `str`

**default value:** `"#C6D1DE"`

```python
rate = Rate(void_color="#1459E4")
```

![void_color](https://user-images.githubusercontent.com/120389559/225907283-ab4c02a6-5acb-4538-8f84-b50dd5bfe6a4.png)

### disabled_void_color

Determine color of unselected read-only icons.

**type:** `str`

**default value:** `"#C6D1DE"`

```python
rate = Rate(disabled_void_color="#5D6D7E", disabled=True)
```

![disabled_void_color](https://user-images.githubusercontent.com/120389559/225908159-b285ef4a-910a-410b-b3ca-2b970ae7d408.png)

## Methods and attributes

|        Attributes and Methods         | Description                                              |
| :-----------------------------------: | -------------------------------------------------------- |
|         `get_current_value()`         | Return `ClassBalance` max value.                         |
|    `set_current_value(value: int)`    | Set `ClassBalance` max value.                            |
|           `get_max_value()`           | Set `ClassBalance` max height.                           |
|      `set_max_value(value: int)`      | Return `ClassBalance` max height.                        |
|            `get_colors()`             | Set `selectable` to `False`.                             |
|            `set_colors()`             | Set `selectable` to `True`.                              |
|           `set_disabled()`            | Return `ClassBalance` `selectable` value.                |
|            `set_unabled()`            | Set `collapsable` to `False`.                            |
|           `get_disabled()`            | Set `collapsable` to `True`.                             |
|         `unable_allow_half()`         | Return `ClassBalance` `collapsable` value.               |
|        `disable_allow_half()`         | Set `clickable_name` to `False`.                         |
|          `get_allow_half()`           | Set `clickable_name` to `True`.                          |
|             `get_texts()`             | Return `ClassBalance` `clickable_name` value.            |
|     `add_texts(value: List[str])`     | Set `clickable_segment` to `False`.                      |
|     `set_texts(value: List[str])`     | Set `clickable_segment` to `True`.                       |
|         `unable_show_text()`          | Return `ClassBalance` `clickable_segment` value.         |
|         `disable_show_text()`         | Add new `segments` to now existing in `ClassBalance`.    |
|           `get_show_text()`           | Return `ClassBalance` `segments`.                        |
|          `get_text_color()`           | Set new `segments` in `ClassBalance`.                    |
|     `set_text_color(value: str)`      | Add new `rows_data` to now existing in `ClassBalance`.   |
|          `get_void_color()`           | Return `ClassBalance` `rows_data`.                       |
|     `set_void_color(value: str)`      | Set new `rows_data` in `ClassBalance`.                   |
|      `get_disabled_void_color()`      | Add new `slider_data` to now existing in `ClassBalance`. |
| `set_disabled_void_color(value: str)` | Return `ClassBalance` `slider_data`.                     |
|         `value_changed(func)`         | Handle value click.                                      |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/misc/rate/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/misc/rate/src/main.py)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Rate
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Initialize `Rate` widget

```python

infos = ["oops", "disappointed", "normal", "good", "great"]
colors = ["#1414E4", "#2DE414", "#F7BA2A"]
rate = Rate(colors=colors, texts=infos, text_color="#E414D7", show_text=True, void_color="#17202A")
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter.

```python
card = Card(
    "Rate",
    content=Container([rate]),
)

layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=card)
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/120389559/225910001-8ff0fe26-401b-4646-b8de-e46e274f2520.gif" alt="layout" />
</p>
