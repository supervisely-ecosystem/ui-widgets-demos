# Checkbox

## Introduction

This widget is a checkbox type input, clicking on it can be processed from python code. In this tutorial you will learn how to use `Checkbox` widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/checkbox)

## Function signature

```python
checkbox = Checkbox(content="Enable")
```

![default](https://user-images.githubusercontent.com/79905215/213662318-4cd628b0-b123-4ac4-8c1f-4f92fe01ab2a.png)

## Parameters

| Parameters |        Type        |         Description         |
| :--------: | :----------------: | :-------------------------: |
|  content   | Union[Widget, str] | content of string or widget |
|  checked   |        bool        |  whether Select is checked  |
| widget_id  |        str         |      id of the widget       |

### content

Сontent of checkbox input string.

**type:** `Union[Widget, str]`

```python
checkbox = Checkbox(content="Enable")
```

### checked

Whether Select is checked.

**type:** `bool`

**default value:** `False`

```python
checkbox = Checkbox(content="Enable", checked=True)
```
![checkbox-checked](https://user-images.githubusercontent.com/79905215/217864130-e7c5bd4b-8f11-43bb-8b18-289dec5b3dbf.png)

### widget_id

ID of the widget.

**type:** `int`

**default value:** `None`

## Methods and attributes

| Attributes and Methods | Description                                                   |
| :--------------------: | ------------------------------------------------------------- |
|     `is_checked()`     | Return `True` if checkbox is checked, else `False`.           |
|       `check()`        | Enable `checked` property.                                    |
|      `uncheck()`       | Disable `checked` property.                                   |
|    `@value_changed`    | Decorator function is handled when checkbox value is changed. |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/016_checkbox/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/016_checkbox/src/main.py)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Checkbox, Container
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Initialize `Checkbox` widget

```python
checkbox = Checkbox(
    content="Enable",
    checked=False,
)
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
# create new cards
card = Card(
    title="Checkbox",
    content=checkbox,
)

layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```

### Add functions to control widget from python code

```python
@checkbox.value_changed
def show_message(value):
    print(f"Checkbox value has been changed: value={value}")

```
