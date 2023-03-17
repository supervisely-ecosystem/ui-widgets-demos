# Timeline

## Introduction

**`Timeline`** widget in Supervisely is used to create a timeline with given list of data intervals and there colors. Users can add intervals, making it useful for interactive data exploration and analysis.

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

### frames_count

Determine total frames count.

**type:** `int`

**default value:** `0`

```python
timeline = Timeline(frames_count=1500, intervals=intervals, colors=colors)
```

![frames_count](https://user-images.githubusercontent.com/120389559/225843044-d80af279-878c-4540-89f0-f1c308983def.gif)

### intervals

Determine `Timeline` intervals.

**type:** `List`

**default value:** `[]`

### colors

Determine `Timeline` intervals colors.

**type:** `List`

**default value:** `[]`

### height

Determine `Timeline` bar height.

**type:** `int`

**default value:** `30`

```python
timeline = Timeline(height=300, intervals=intervals, colors=colors)
```

![height](https://user-images.githubusercontent.com/120389559/225843707-e0322f85-8ed7-4109-a04e-a026eb4f0554.png)

### pointer_color

Determine pointer background color.

**type:** `str`

**default value:** `""`

```python
pointer_color = "#ffffff"
timeline = Timeline(pointer_color=pointer_color, intervals=intervals, colors=colors)
```

![pointer_color](https://user-images.githubusercontent.com/120389559/225844384-0ad0a3e4-83c0-409d-8817-75bd678f03c0.gif)

### widget_id

ID of the widget.

**type:** `str`

**default value:** `None`

## Methods and attributes

|                  Attributes and Methods                  | Description                                             |
| :------------------------------------------------------: | ------------------------------------------------------- |
|                `set_pointer(value: int)`                 | Set `Timeline` pointer value.                           |
|                     `get_pointer()`                      | Return `Timeline` pointer value.                        |
|              `set_frames_count(value: int)`              | Set `Timeline` frames count.                            |
|                   `get_frames_count()`                   | Return `Timeline` frames count value.                   |
| `add_intervals(intervals: List = [], colors: List = [])` | Add new intervals to existing ones in `Timeline`.       |
| `set_intervals(intervals: List = [], colors: List = [])` | Set new intervals in `Timeline`.                        |
|                    `get_intervals()`                     | Return `Timeline` intervals.                            |
|                      `get_colors()`                      | Return `Timeline` colors.                               |
|                 `set_height(value: int)`                 | Set `Timeline` height.                                  |
|                      `get_height()`                      | Return `Timeline` height.                               |
|             `set_pointer_color(value: str)`              | Set `Timeline` poiner color.                            |
|                  `get_pointer_color()`                   | Return `Timeline` poiner color.                         |
|                  `get_select_segment()`                  | Return `Timeline` current selected segments.            |
|                         `@click`                         | Decorator function to handle selected segment by click. |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/misc/timeline/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/misc/timeline/src/main.py)

### Import libraries

```python
import os

from dotenv import load_dotenv
import supervisely as sly
from supervisely.app.widgets import Card, Container, Timeline, Text
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Prepare intervals and there colors for timeline

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
```

### Initialize `Timeline` and `Text` widgets

```python
timeline = Timeline(intervals=intervals, colors=colors)

text = Text()
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter.

```python
card = Card(
    title="Timeline",
    content=Container([timeline, text]),
)
layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=card)
```

### Add functions to control widgets from python code

```python
@timeline.click
def show_item(res):
    info = f"Current clicked interval: from {res[0]} to {res[1]}"
    text.set(text=info, status="info")
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/120389559/225847401-c7aa255c-e32c-40c3-b5ed-4c4e0942e5f8.gif" alt="layout" />
</p>
