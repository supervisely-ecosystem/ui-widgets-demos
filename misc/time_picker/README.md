# Time Picker

## Introduction

**`TimePicker`** is a widget in Supervisely that allows choise time on the UI.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/widgets/charts-and-plots/timepicker)

## Function signature

```python
TimePicker(
    start="09:00",
    step="00:15",
    end="22:30",
    placeholder=None,
    size=None,
    readonly=False,
    disabled=False,
    editable=True,
    clearable=True,
    widget_id=None,
)
```

![time_picker_default](https://user-images.githubusercontent.com/120389559/226362544-665389df-e819-4bc2-908c-8b1b6effaf84.gif)

## Parameters

|  Parameters   |                   Type                    |            Description            |
| :-----------: | :---------------------------------------: | :-------------------------------: |
|    `start`    |                   `str`                   |            Start time             |
|    `step`     |                   `str`                   |             Time step             |
|     `end`     |                   `str`                   |             End time              |
| `placeholder` |                   `str`                   |     `TimePicker` placeholder      |
|    `size`     | `Literal["large", "small", "mini", None]` |           Size of input           |
|  `readonly`   |                  `bool`                   | Whether `TimePicker` is read only |
|  `disabled`   |                  `bool`                   | Whether `TimePicker` is disabled  |
|  `editable`   |                  `bool`                   |   Whether the input is editable   |
|  `clearable`  |                  `bool`                   |   Whether to show clear button    |
|  `widget_id`  |                   `str`                   |         ID of the widget          |

### start

Determine `TimePicker` start time.

**type:** `str`

**default value:** `"09:00"`

### step

Determine `TimePicker` time step.

**type:** `str`

**default value:** `"00:15"`

### end

Determine `TimePicker` end time.

**type:** `str`

**default value:** `"22:30"`

```python
time_picker = TimePicker(start="06:30", step="00:30", end="15:00")
```

![start_step_end](https://user-images.githubusercontent.com/120389559/226361267-a46da0f4-38d3-46fc-adaa-bef14d33e58f.gif)

### placeholder

Determine `TimePicker` placeholder.

**type:** `str`

**default value:** `None`

```python
time_picker = TimePicker(placeholder="Select time")
```

![placeholder](https://user-images.githubusercontent.com/120389559/226362933-1da5a4c1-d9a6-4ba3-85d2-831afb42e074.png)

### size

Determine `TimePicker` size of input.

**type:** `Literal["large", "small", "mini", None]`

**default value:** `None`

```python
text = Text()
time_picker = TimePicker()
time_picker_mini = TimePicker(size="mini")
time_picker_small = TimePicker(size="small")
time_picker_large = TimePicker(size="large")
```

![size](https://user-images.githubusercontent.com/120389559/226363690-95e2def4-9154-44ef-8469-f0b4132e76e1.png)

### readonly

Determine whether `TimePicker` is read only.

**type:** `bool`

**default value:** `False`

```python
time_picker = TimePicker(readonly=True)
```

![readonly](https://user-images.githubusercontent.com/120389559/226364643-d1f00154-accb-461f-a26a-971fa3a103e2.gif)

### disabled

Determine whether `TimePicker` is disabled.

**type:** `bool`

**default value:** `False`

```python
time_picker = TimePicker(disabled=True)
```

![disabled](https://user-images.githubusercontent.com/120389559/226365042-fb81b483-3a63-4e25-9cc3-d1c326631342.png)

### editable

Determine whether the input is editable.

**type:** `bool`

**default value:** `True`

### clearable

Determine whether to show clear button.

**type:** `bool`

**default value:** `True`

## Methods and attributes

| Attributes and Methods  | Description                                      |
| :---------------------: | ------------------------------------------------ |
|      `get_value()`      | Return `TimePicker` current value.               |
| `get_picker_options()`  | Return `TimePicker` options(start, step, end).   |
| `set_start(value: str)` | Set `TimePicker` start time.                     |
|  `set_end(value: str)`  | Set `TimePicker` time step.                      |
| `set_step(value: str)`  | Set `TimePicker` end time.                       |
|    `@value_changed`     | Decorator function to handle `TimePicker` click. |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/misc/time_picker/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/misc/time_picker/src/main.py)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Text, TimePicker
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Initialize `TimePicker` and `Text` widgets

```python
time_picker = TimePicker()

text = Text()
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter.

```python
card = Card(
    "Time Picker",
    content=Container([time_picker, text]),
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
@time_picker.value_changed
def show_time(res):
    info = f"Selected time: {res}"
    text.set(text=info, status="info")
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/120389559/226366974-06d6fde5-11cc-4cdf-b743-93bf378b67fa.gif" alt="layout" />
</p>