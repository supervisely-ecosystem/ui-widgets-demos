# Input

## Introduction

In this tutorial you will learn how to use `Input` widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/input)

## Function signature

```python
Input(value="", minlength=0, maxlength=1000, placeholder="", size=None, readonly=False, widget_id=None)
```

![default](https://user-images.githubusercontent.com/79905215/213988894-d4420e3e-5003-431b-8be1-01b1ddbf98df.png)

## Parameters

| Parameters  |               Type                |           Description           |
| :---------: | :-------------------------------: | :-----------------------------: |
|    value    |                str                |          binding value          |
|  minlength  |                int                |    minimum input text length    |
|  maxlength  |               bool                |    maximum input text length    |
| placeholder |                int                |      placeholder of input       |
|    size     | Literal["mini", "small", "large"] |          size of input          |
|  readonly   |               bool                | same as readonlyin native input |
|  widget_id  |                int                |        id of the widget         |

### value

Binding value.

**type:** `str`

**default value:** ""

```python
input = Input(value="Start input value")
```

![value](https://user-images.githubusercontent.com/48913536/202438044-1b805dec-7e29-4969-867e-b9fc1d28cea4.gif)

### minlength

Minimum input text length.

**type:** `int`

**default value:** `0`

```python
input = Input(minlength=5)
```

### maxlength

Maximum input text length.

**type:** `int`

**default value:** `1000`

```python
input = Input(maxlength=500)
```

### placeholder

Placeholder of input.

**type:** `str`

**default value:** ""

```python
input = Input(placeholder="Please input")
```

![value](https://user-images.githubusercontent.com/48913536/202438044-1b805dec-7e29-4969-867e-b9fc1d28cea4.gif)

### size

Size of input.

**type:** `str`

**default value:** `None`

```python
input = Input()
```

![value](https://user-images.githubusercontent.com/48913536/202438044-1b805dec-7e29-4969-867e-b9fc1d28cea4.gif)

```python
input = Input(input="mini")
```

![value](https://user-images.githubusercontent.com/48913536/202438044-1b805dec-7e29-4969-867e-b9fc1d28cea4.gif)

```python
input = Input(input="small")
```

![value](https://user-images.githubusercontent.com/48913536/202438044-1b805dec-7e29-4969-867e-b9fc1d28cea4.gif)

```python
input = Input(input="large")
```

![value](https://user-images.githubusercontent.com/48913536/202438044-1b805dec-7e29-4969-867e-b9fc1d28cea4.gif)

### readonly

Same as readonlyin native input.

**type:** `bool`

**default value:** `false`

```python
input = Input(readonly=True)
```

![value](https://user-images.githubusercontent.com/48913536/202438044-1b805dec-7e29-4969-867e-b9fc1d28cea4.gif)

### widget_id

ID of the widget.

**type:** `int`

**default value:** `None`

**Methods and attributes**

| Attributes and Methods  | Description                                                |
| :---------------------: | ---------------------------------------------------------- |
|     `is_readonly()`     | Return `True` if input is readonly, else `False`.          |
| `set_value(value: str)` | Set input value.                                           |
|      `get_value()`      | Get input value.                                           |
|   `enable_readonly()`   | Enable input`s readonly property.                          |
|  `disable_readonly()`   | Disable input`s readonly property.                         |
|     `value_changed`     | Decorator function is handled when input value is changed. |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/002_progress_bar/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/004_input/src/main.py)

### Import libraries

```python
import os
from random import choice

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, Input
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Initialize `Input` widget

```python
input_text = Input(placeholder="Please input")
```

### Create buttons to control Input widget values.

```python
button_random_planet = Button(text="Random planet name")
button_clean_input = Button(text="Clean input")
button_set_readonly = Button(text="Set readonly")

buttons_container = Container(
    widgets=[
        button_random_planet,
        button_clean_input,
        button_set_readonly,
    ],
    direction="horizontal",
)
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
# create new cards
card = Card(
    title="Input",
    content=Container(widgets=[input_text, buttons_container]),
)

layout = Container(widgets=[card], direction="vertical")
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```

### Add functions to control widget from python code

```python
@button_random_planet.click
def random_planet():
    input_text.set_value(
        choice(
            [
                "Mercury",
                "Venus",
                "Earth",
                "Mars",
                "Jupiter",
                "Saturn",
                "Uranus",
                "Neptune",
            ]
        )
    )


@button_clean_input.click
def random_word():
    input_text.set_value("")


@button_set_readonly.click
def set_readonly():
    if input_text.is_readonly():
        input_text.disable_readonly()
        print("Readonly: Disabled")
    else:
        input_text.enable_readonly()
        print("Readonly: Enabled")
```
