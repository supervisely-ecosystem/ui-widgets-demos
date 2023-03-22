# Date and Time Picker

## Introduction

**`DateTimePicker`** is a widget in Supervisely that allows choise date and time on the UI.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/widgets/charts-and-plots/datetimepicker)

## Function signature

```python
DateTimePicker(
    value=None
    readonly=False,
    disabled=False,
    editable=True,
    clearable=True,
    size=None,
    placeholder="Select date and time",
    w_type="datetime",
    format="yyyy-MM-dd HH:mm:ss",
    widget_id=None,
)
```

![datetime_picker_default](link)

## Parameters

|  Parameters   |                                         Type                                         |            Description             |
| :-----------: | :----------------------------------------------------------------------------------: | :--------------------------------: |
|    `value`    |                         `Union[int, str, list, tuple, None]`                         | Default value in `DateTimePicker`  |
|  `readonly`   |                                        `bool`                                        |    Allows to set read only mode    |
|  `disabled`   |                                        `bool`                                        | Allows to disable `DateTimePicker` |
|  `editable`   |                                        `bool`                                        |        Allows to edit input        |
|  `clearable`  |                                        `bool`                                        |         Shows clear button         |
|    `size`     |                      `Literal["large", "small", "mini", None]`                       |        Size of input field         |
| `placeholder` |                                        `str`                                         |    `DateTimePicker` placeholder    |
|   `w_type`    | `Literal["year", "month", "date", "datetime", "week", "datetimerange", "daterange"]` |    `DateTimePicker` picker type    |
|   `format`    |                                        `str`                                         |     Datetime displaying format     |
|  `widget_id`  |                                        `str`                                         |          ID of the widget          |

### value

Determine `DateTimePicker` default value.

**type:** `Union[int, str, list, tuple, None]`

**default value:** `None`

```python
datetime_picker = DateTimePicker(value="2023-03-22 14:01:02")
```

![value](link)

### placeholder

Determine `DateTimePicker` placeholder.

**type:** `str`

**default value:** `"Select date and time"`

```python
datetime_picker = DateTimePicker(placeholder="Select")
```

![placeholder](link)

### size

Determine `DateTimePicker` size of input.

**type:** `Literal["large", "small", "mini", None]`

**default value:** `None`

```python
datetime_picker = DateTimePicker()
datetime_picker_mini = DateTimePicker(size="mini")
datetime_picker_small = DateTimePicker(size="small")
datetime_picker_large = DateTimePicker(size="large")
```

![size](link)

### w_type

Determine `DateTimePicker` picker type.

**type:** `Literal["year", "month", "date", "datetime", "week", "datetimerange", "daterange"]`

**default value:** `"datetime"`

```python
datetime_picker = DateTimePicker(w_type="datetimerange")
```

![type-datetimerange](link)

### format

Determine `DateTimePicker` displaying format.

**type:** `str`

**default value:** `"yyyy-MM-dd HH:mm:ss"`

```python
datetime_picker = DateTimePicker(format="yyyy-MM-dd HH:mm")
```

![format](link)

### readonly

Determine whether `DateTimePicker` is read only.

**type:** `bool`

**default value:** `False`

```python
datetime_picker = DateTimePicker(readonly=True)
```

![readonly](link)

### disabled

Determine whether `DateTimePicker` is disabled.

**type:** `bool`

**default value:** `False`

```python
datetime_picker = DateTimePicker(disabled=True)
```

![disabled](link)

### editable

Determine whether the input is editable.

**type:** `bool`

**default value:** `True`

### clearable

Determine whether to show clear button.

**type:** `bool`

**default value:** `True`

### widget_id

ID of the widget

**type:** `str`

**default value:** `None`

## Methods and attributes

|             Attributes and Methods             | Description                                          |
| :--------------------------------------------: | ---------------------------------------------------- |
|                 `get_value()`                  | Return `DateTimePicker` current value.               |
| `set_value(value: Union[int, str, datetime])`  | Set `DateTimePicker` vlue.                           |
| `set_range_values(values: Union[list, tuple])` | Set `DateTimePicker` range values.                   |
|                `@value_changed`                | Decorator function to handle `DateTimePicker` click. |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/misc/datetime_picker/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/misc/datetime_picker/src/main.py)

### Import libraries

```python
import os
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Text, DateTimePicker
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))
api = sly.Api()
```

### Initialize `DateTimePicker` and `Text` widgets

```python
datetime_picker = DateTimePicker()
text = Text()
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter.

```python
card = Card(
    "Date and Time Picker",
    content=Container([datetime_picker, text]),
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
@datetime_picker.value_changed
def show_time(res):
    info = f"Selected time: {res}"
    text.set(text=info, status="info")
```

<p align="center">
  <img src="link" alt="layout" />
</p>
