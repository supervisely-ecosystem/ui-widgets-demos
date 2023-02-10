# InputNumber

## Introduction

In this tutorial you will learn how to use `InputNumber` widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/inputnumber)

## Function signature

```python
InputNumber(value=1, min=None, max=None, step=1, size="small", controls=True, debounce=300, precision=0, widget_id=None)
```

![default](https://user-images.githubusercontent.com/120389559/217827984-b1b33d3e-2dfd-43de-9c2e-9558a5d15bbb.png)

## Parameters

| Parameters |    Type    |                Description                 |
| :--------: | :--------: | :----------------------------------------: |
|   value    | int, float |               binding value                |
|    min     | int, float |         the minimum allowed value          |
|    max     | int, float |         the maximum allowed value          |
|    step    | int, float |             incremental steps              |
|    size    |    str     |           size of the component            |
|  controls  |    bool    |   whether to enable the control buttons    |
|  debounce  |    int     | debounce delay when typing, in millisecond |
| precision  |    int     |                 precision                  |
| widget_id  |    int     |              id of the widget              |

### value

Binding value.

**type:** `int`, `float`

**default value:** `1`

```python
input_number = InputNumber(value=7)
```

![value](https://user-images.githubusercontent.com/120389559/217828155-7a8ef55a-defb-48f9-9d8e-ff0d592c0a87.png)

### min

Minimum allowed value.

**type:** `int`, `float`

**default value:** `None`

```python
input = InputNumber(min=5)
```

### max

Maximum allowed value.

**type:** `int`, `float`

**default value:** `None`

```python
input = InputNumber(max=500)
```

### step

Incremental steps.

**type:** `int`, `float`

**default value:** `1`

```python
input = InputNumber(step=3)
```

![step](https://user-images.githubusercontent.com/120389559/218094932-18d8e080-3bda-48e7-92f4-1fc8f65db643.gif)

### size

Size of the component.

**type:** `str`

**default value:** `small`

```python
input_small = InputNumber(size="small")
input_large = InputNumber(size="large")
```

![size](https://user-images.githubusercontent.com/120389559/218095519-b8293718-490f-4101-9781-3607bd607a4f.png)

### controls

Whether to enable the control buttons.

**type:** `bool`

**default value:** `true`

```python
input = InputNumber(controls=True)
```

### debounce

Debounce delay when typing, in millisecond.

**type:** `int`

**default value:** `300`

```python
input = InputNumber(debounce=500)
```

### precision

Precision.

**type:** `int`

**default value:** `0`

```python
input = InputNumber(precision=2)
```

### widget_id

ID of the widget.

**type:** `int`

**default value:** `None`

**Methods and attributes**

| Attributes and Methods | Description                                                |
| :--------------------: | ---------------------------------------------------------- |
|        `value`         | Get or set widgets `value` filed.                          |
|     `get_value()`      | Get input number value.                                    |
|         `min`          | Set min value value.                                       |
|         `max`          | Set max value value.                                       |
|    `value_changed`     | Decorator function is handled when input value is changed. |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/005_input_number/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/005_input_number/src/main.py)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, InputNumber
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Initialize `InputNumber` widget

```python
input_number = InputNumber()
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card = Card(
    title="Input Number",
    content=Container(widgets=[input_number]),
)

layout = Container(widgets=[card], direction="vertical")
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```
