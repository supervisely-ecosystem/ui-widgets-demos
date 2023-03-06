# Slider

## Introduction

In this tutorial you will learn how to use `Slider` widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/slider)

## Function signature

```python
Slider(
    value=0,
    min=0,
    max=100,
    step=1,
    show_input=False,
    show_input_controls=False,
    show_stops=False,
    show_tooltip=True,
    range=False,
    vertical=False,
    height=None,
    widget_id=None,
)
```

![default](https://user-images.githubusercontent.com/120389559/223120953-a9a1b137-26c4-441f-9f1b-81cc7afd6d9c.gif)

## Parameters

|      Parameters       |          Type           |                          Description                           |
| :-------------------: | :---------------------: | :------------------------------------------------------------: |
|        `value`        | `Union[int, List[int]]` |                      `Slider` start value                      |
|         `min`         |          `int`          |                         Minimum value                          |
|         `max`         |          `int`          |                         Maximum value                          |
|        `step`         |          `int`          |                           Step size                            |
|     `show_input`      |         `bool`          | Whether to display an input box, works when `range` is `False` |
| `show_input_controls` |         `bool`          | Whether to display control buttons when `show-input` is `True` |
|     `show_stops`      |         `bool`          |                 Whether to display breakpoints                 |
|    `show_tooltip`     |         `bool`          |                Whether to display tooltip value                |
|        `range`        |         `bool`          |                   Whether to select a range                    |
|      `vertical`       |         `bool`          |                         Vertical mode                          |
|       `height`        |          `int`          |           `Slider` height, required in vertical mode           |
|      `widget_id`      |          `str`          |                        Id of the widget                        |

### value

Determine `Slider` start value.

**type:** `Union[int, List[int]]`

**default value:** `0`

```python
slider = Slider(value=15)
```

![value](https://user-images.githubusercontent.com/120389559/223123599-84cf761f-c872-4eb3-9818-0c64d0f7ea02.gif)

### min

Determine `Slider` minimum value.

**type:** `int`

**default value:** `0`

### max

Determine `Slider` maximum value.

**type:** `int`

**default value:** `100`

```python
slider = Slider(min=30, max=50)
```

![min_max](https://user-images.githubusercontent.com/120389559/223124560-2779ca6a-c4af-4566-b0a8-ccdeae655333.gif)

### step

Determine step size.

**type:** `int`

**default value:** `1`

```python
slider = Slider(step=5)
```

![step](https://user-images.githubusercontent.com/120389559/223126223-757d4d9d-955b-4c4c-977a-db06c1f53678.gif)

### show_input

Whether to display an input box, works when `range` is false.

**type:** `bool`

**default value:** `false`

```python
slider = Slider(show_input=True)
```

![show_input](https://user-images.githubusercontent.com/120389559/223126910-d41427e0-e577-4f25-93b8-cff984d9bc35.gif)

### show_input_controls

Whether to display control buttons when `show-input` is true.

**type:** `bool`

**default value:** `false`

```python
slider = Slider(show_input=True, show_input_controls=True)
```

![show_input_controls](https://user-images.githubusercontent.com/120389559/223127700-8beb0cb4-547a-41d0-8825-560d55b3bdf2.gif)

### show_stops

Whether to display breakpoints.

**type:** `bool`

**default value:** `false`

```python
slider = Slider(show_stops=True, max=20, step=5)
```

![show_stops](https://user-images.githubusercontent.com/120389559/223128573-f0685e71-2722-491d-bdcd-bcecbe425688.gif)

### show_tooltip

Whether to display tooltip value.

**type:** `bool`

**default value:** `true`

```python
slider = Slider(show_tooltip=False)
```

![show_tooltip](https://user-images.githubusercontent.com/120389559/223129072-7508c91c-5d1a-49f0-a032-07744241e121.gif)

### range

Determine whether to select a range, equires value to be List[int, int].

**type:** `bool`

**default value:** `true`

```python
slider = Slider(value=[5, 20], range=True)
```

![range](https://user-images.githubusercontent.com/120389559/223129733-1f769ed5-bd73-4bb7-9d03-ee7f813e9aae.gif)

### vertical

Determine vertical mode.

**type:** `bool`

**default value:** `false`

### height

Determine `Slider` height, required in vertical mode.

**type:** `int`

**default value:** `None`

```python
slider = Slider(vertical=True, height=100)
```

![vertical](https://user-images.githubusercontent.com/120389559/223130649-d7a81b94-6645-4dc2-9568-95541e9d2228.gif)

### widget_id

ID of the widget.

**type:** `str`

**default value:** `None`

## Methods and attributes

|          Attributes and Methods           | Description                                |
| :---------------------------------------: | ------------------------------------------ |
| `set_value(value: Union[int, List[int]])` | Set `Slider` value.                        |
|               `get_value()`               | Return `Slider` value.                     |
|                `set_min()`                | Set `Slider` minimum.                      |
|                `get_min()`                | Return `Slider` minimum.                   |
|                `set_max()`                | Set `Slider` maximum.                      |
|                `get_max()`                | Return `Slider` maximum.                   |
|               `set_step()`                | Set `Slider` step.                         |
|               `get_step()`                | Return `Slider` step.                      |
|           `is_input_enabled()`            | Return `Slider` `showInput` value.         |
|              `show_input()`               | Set `showInput` value to `True`.           |
|              `hide_input()`               | Set `showInput` value to `False`.          |
|       `is_input_controls_enabled()`       | Return `Slider` `showInputControls` value. |
|          `show_input_controls()`          | Set `showInputControls` value to `True`.   |
|          `hide_input_controls()`          | Set `showInputControls` value to `False`.  |
|            `is_step_enabled()`            | Return `Slider` `showStops` value.         |
|              `show_steps()`               | Set `showStops` value to `True`.           |
|              `hide_steps()`               | ESet `showStops` value to `False`.         |
|          `is_tooltip_enabled()`           | Return `Slider` `showTooltip` value.       |
|             `show_tooltip()`              | Set `showTooltip` value to `True`.         |
|             `hide_tooltip()`              | Set `showTooltip` value to `False`.        |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/misc/slider/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/misc/slider/src/main.py)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Slider
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Initialize `Slider` widget

```python
slider = Slider(value=[10, 50], step=5, range=True, show_stops=True)
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card = Card(title="Slider", content=Container([slider]))
layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```

![layout](https://user-images.githubusercontent.com/120389559/223135395-7a883603-d8bf-40da-a5b1-1409f0f6e424.gif)
