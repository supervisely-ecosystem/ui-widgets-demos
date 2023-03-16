# Timeline

## Introduction

**`Timeline`** widget in Supervisely is used to create a timeline with given list of data. Users can add intervals, making it useful for interactive data exploration and analysis.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/widgets/charts-and-plots/timeline)

## Function signature

```python
Timeline(
    pointer=0,
    frames_count=0,
    intervals=[],
    colors=[],
    height=30,
    pointer_color="",
    widget_id=None,
)
```

```python
intervals = [
    [1, 60],
    [100, 300],
    [320, 330],
    [340, 345],
    [400, 450],
    [500, 700],
    [800, 900],
]

colors = ["#99d162", "#00f0b0", "#e41436", "#14d7e4", "#99d162", "#ffff00", "#00ff00"]

timeline = Timeline(intervals=intervals, colors=colors)
```

![timeline_default](https://user-images.githubusercontent.com/120389559/225675990-836fb9a3-2976-465f-9863-d6c75243b36d.gif)

## Parameters

|   Parameters    |  Type  |         Description         |
| :-------------: | :----: | :-------------------------: |
|    `pointer`    | `int`  |    Current frame number     |
| `frames_count`  | `int`  |     Total frames count      |
|   `intervals`   | `list` |    `Timeline` intervals     |
|    `colors`     | `list` | `Timeline` intervals colors |
|    `height`     | `int`  |    `Timeline` bar height    |
| `pointer_color` | `int`  |  Pointer background color   |
|   `widget_id`   | `str`  |      ID of the widget       |

### pointer

Determine current `Timeline` frame number.

**type:** `int`

**default value:** `0`

```python
timeline = Timeline(pointer=220, intervals=intervals, colors=colors)
```

![pointer](https://user-images.githubusercontent.com/120389559/225677625-c35b9734-f1af-49b1-816f-d7e2e760e42b.png)

### selectable

Display collapse button.

**type:** `bool`

**default value:** `True`

```python
class_balance = ClassBalance(
    max_value=max_value,
    segments=segments,
    rows_data=rows_data,
    slider_data=slider_data,
    selectable=False,
    collapsable=True
)
```

![selectable](https://user-images.githubusercontent.com/120389559/224936812-ba9e1bce-8cb7-4729-9dc6-c52b27da6e04.png)

### collapsable

Display collapse button. The case `collapsable=True` has been shown above to show examples for changing the `max_height` parameter. So now an example will be shown for case `collapsable=False`.

**type:** `bool`

**default value:** `False`

```python
class_balance = ClassBalance(
    max_value=max_value,
    segments=segments,
    rows_data=rows_data,
    slider_data=slider_data,
    collapsable=False
)
```

![collapsable](https://user-images.githubusercontent.com/120389559/224938851-fdf5a506-b100-49f9-90d5-17252a6720b7.png)

### clickable_name

Allow to click on class name.

**type:** `bool`

**default value:** `False`

```python
class_balance = ClassBalance(
    max_value=max_value,
    segments=segments,
    rows_data=rows_data,
    slider_data=slider_data,
    clickable_name=True,
)
```

![clickable_name](https://user-images.githubusercontent.com/120389559/224949506-f85fa772-e2c8-4de5-9079-919adc9cbf2c.png)

### clickable_segment

Allow to click on class segments.

**type:** `bool`

**default value:** `False`

```python
class_balance = ClassBalance(
    max_value=max_value,
    segments=segments,
    rows_data=rows_data,
    slider_data=slider_data,
    clickable_segment=True,
)
```

## Methods and attributes

|                     Attributes and Methods                     | Description                                                    |
| :------------------------------------------------------------: | -------------------------------------------------------------- |
|                       `get_max_value()`                        | Return `ClassBalance` max value.                               |
|                  `set_max_value(value: int)`                   | Set `ClassBalance` max value.                                  |
|                  `set_max_height(value: int)`                  | Set `ClassBalance` max height.                                 |
|                       `get_max_height()`                       | Return `ClassBalance` max height.                              |
|                     `disable_selectable()`                     | Set `selectable` to `False`.                                   |
|                     `unable_selectable()`                      | Set `selectable` to `True`.                                    |
|                       `get_selectable()`                       | Return `ClassBalance` `selectable` value.                      |
|                    `disable_collapsable()`                     | Set `collapsable` to `False`.                                  |
|                     `unable_collapsable()`                     | Set `collapsable` to `True`.                                   |
|                      `get_collapsable()`                       | Return `ClassBalance` `collapsable` value.                     |
|                   `disable_clickable_name()`                   | Set `clickable_name` to `False`.                               |
|                   `unable_clickable_name()`                    | Set `clickable_name` to `True`.                                |
|                     `get_clickable_name()`                     | Return `ClassBalance` `clickable_name` value.                  |
|                 `disable_clickable_segment()`                  | Set `clickable_segment` to `False`.                            |
|                  `unable_clickable_segment()`                  | Set `clickable_segment` to `True`.                             |
|                   `get_clickable_segment()`                    | Return `ClassBalance` `clickable_segment` value.               |
|  `add_segments(segments: List[Dict] = [], send_changes=True)`  | Add new `segments` to now existing in `ClassBalance`.          |
|                        `get_segments()`                        | Return `ClassBalance` `segments`.                              |
|  `set_segments(segments: List[Dict] = [], send_changes=True)`  | Set new `segments` in `ClassBalance`.                          |
| `add_rows_data(rows_data: List[Dict] = [], send_changes=True)` | Add new `rows_data` to now existing in `ClassBalance`.         |
|                       `get_rows_data()`                        | Return `ClassBalance` `rows_data`.                             |
| `set_rows_data(rows_data: List[Dict] = [], send_changes=True)` | Set new `rows_data` in `ClassBalance`.                         |
|  `add_slider_data(slider_data: Dict = {}, send_changes=True)`  | Add new `slider_data` to now existing in `ClassBalance`.       |
|                      `get_slider_data()`                       | Return `ClassBalance` `slider_data`.                           |
|  `set_slider_data(slider_data: Dict = {}, send_changes=True)`  | Set new `slider_data` in `ClassBalance`.                       |
|                     `get_selected_rows()`                      | Return list of `ClassBalance` clicked rows.                    |
|                            `@click`                            | Decorator function to handle class name or rows segment click. |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/misc/class_balance/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/misc/class_balance/src/main.py)

### Import libraries

```python
import os

from dotenv import load_dotenv
import supervisely as sly
from supervisely.app.widgets import ClassBalance, Text, Card, Container
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Prepare series for class balance

```python
max_value = 1000
segments = [
    {"name": "Train", "key": "train", "color": "#1892f8"},
    {"name": "Val", "key": "val", "color": "#25e298"},
    {"name": "Test", "key": "test", "color": "#fcaf33"},
]

rows_data = [
    {
        "nameHtml": "<div>black-pawn</div>",
        "name": "black-pawn",
        "total": 1000,
        "disabled": False,
        "segments": {"train": 600, "val": 350, "test": 50},
    },
    {
        "name": "white-pawn",
        "total": 700,
        "disabled": False,
        "segments": {"train": 400, "val": 250, "test": 50},
    },
    {
        "name": "black-rook",
        "total": 450,
        "disabled": True,
        "segments": {"train": 300, "val": 150, "test": 0},
    },
    {
        "name": "white-rook",
        "total": 250,
        "disabled": False,
        "segments": {"train": 200, "val": 50, "test": 0},
    },
]

slider_data = {
    "black-pawn": [
        {
            "moreExamples": ["https://www.w3schools.com/howto/img_nature.jpg"],
            "preview": "https://www.w3schools.com/howto/img_nature.jpg",
        },
        {
            "moreExamples": ["https://www.quackit.com/pix/samples/18m.jpg"],
            "preview": "https://www.quackit.com/pix/samples/18m.jpg",
        },
    ],
    "white-pawn": [
        {
            "moreExamples": ["https://i.imgur.com/35pUPD2.jpg"],
            "preview": "https://i.imgur.com/35pUPD2.jpg",
        },
        {
            "moreExamples": ["https://i.imgur.com/fB2DBcM.jpeg"],
            "preview": "https://i.imgur.com/fB2DBcM.jpeg",
        },
    ],
    "black-rook": [
        {
            "moreExamples": ["https://i.imgur.com/OpSj3JE.jpg"],
            "preview": "https://i.imgur.com/OpSj3JE.jpg",
        },
        {
            "moreExamples": ["https://www.w3schools.com/howto/img_nature.jpg"],
            "preview": "https://www.w3schools.com/howto/img_nature.jpg",
        },
        {
            "moreExamples": ["https://www.quackit.com/pix/samples/18m.jpg"],
            "preview": "https://www.quackit.com/pix/samples/18m.jpg",
        },
    ],
    "white-rook": [
        {
            "moreExamples": ["https://i.imgur.com/35pUPD2.jpg"],
            "preview": "https://i.imgur.com/35pUPD2.jpg",
        },
        {
            "moreExamples": ["https://i.imgur.com/fB2DBcM.jpeg"],
            "preview": "https://i.imgur.com/fB2DBcM.jpeg",
        },
        {
            "moreExamples": ["https://i.imgur.com/OpSj3JE.jpg"],
            "preview": "https://i.imgur.com/OpSj3JE.jpg",
        },
    ],
}
```

### Initialize `ClassBalance` and `Text` widgets

```python
class_balance = ClassBalance(
    max_value=max_value,
    segments=segments,
    rows_data=rows_data,
    slider_data=slider_data,
    max_height=700,
    collapsable=True,
    clickable_name=True,
    clickable_segment=True,
)

text = Text()
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter.

```python
card = Card(
    title="Class Balance",
    content=Container([class_balance, text]))
layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=card)
```

### Add functions to control widgets from python code

```python
@class_balance.click
def show_item(res):
    if res.get("segmentValue") is not None and res.get("segmentName") is not None:
        info = (
            f"Class {res['name']} contain {res['segmentValue']} tags with name {res['segmentName']}"
        )
        if res["segmentName"] == "Val":
            status = "success"
        elif res["segmentName"] == "Test":
            status = "warning"
        else:
            status = "info"
    else:
        info = f"Class {res['name']}"
        status = "text"

    text.set(text=info, status=status)
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/120389559/224947329-e58c39ee-232b-4b77-8dc2-45692a97a9d6.gif" alt="layout" />
</p>
