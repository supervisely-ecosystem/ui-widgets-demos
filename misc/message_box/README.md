# MessageBox

## Introduction

**`MessageBox`** is a widget in Supervisely that allows to show dialog window messages on the UI. It is used to display information, warnings, errors.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/widgets/message-box)

## Function signature

```python
MessageBox(
    title="",
    message="",
    type="info",
    widget_id=None,
)
```

![message_box_default]()

## Parameters

| Parameters  |                 Type                  |        Description         |
| :---------: | :-----------------------------------: | :------------------------: |
|   `title`   |                 `str`                 |  Title of the message box  |
|  `message`  |                 `str`                 | Message of the message box |
|   `type`    | `Literal["info", "warning", "error"]` |  Type of the message box   |
| `widget_id` |                 `str`                 |      ID of the widget      |

### title

Determine title of the message box.

**type:** `str`

**default value:** `""`

```python
message_box = MessageBox(title="My title")
```

![message_box_title]()

### message

Determine message of the message box.

**type:** `str`

**default value:** `""`

```python
message_box = MessageBox(message="My message")
```

![message_box_message]()

### type

Determine type of the message box.

**type:** `Literal["info", "warning", "error"]`

**default value:** `"info"`

```python
message_box = MessageBox(type="warning")
```

![message_box_type]()

### widget_id

Determine ID of the widget.

**type:** `str`

**default value:** `None`

## Methods and attributes

|                                      Attributes and Methods                                      | Description                         |
| :----------------------------------------------------------------------------------------------: | ----------------------------------- |
|                                          `get_title()`                                           | Get title of the message box        |
|                                     `set_title(title: str)`                                      | Set title of the message box        |
|                                         `get_message()`                                          | Get message of the message box      |
|                                   `set_message(message: str)`                                    | Set message of the message box      |
|                                           `get_type()`                                           | Get type of the message box         |
|                      `set_type(type: Literal["info", "warning", "error"])`                       | Set type of the message box         |
|                                           `get_data()`                                           | Get data of the message box         |
|                                   `set(data: Dict[str, Any])`                                    | Set data of the message box         |
| `open(title: str = None, message: str = None, type: Literal["info", "warning", "error"] = None)` | Open message box with optional data |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/misc/message_box/src/main.py]()

### Import libraries

```python
import os
import supervisely as sly
from supervisely.app.widgets import Button, Card, Container, Flexbox, Input, MessageBox
from dotenv import load_dotenv
```

### Load environment variables

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))
```

### Initialize `MessageBox` widget

```python
message_box = MessageBox(title="Message Box title", message="Message Box message")
```

### Create additional widgets

```python
button_open = Button("open message")
button_set = Button("set")
buttons = Flexbox([button_open, button_set])

title_input = Input(placeholder="Enter title")
message_input = Input(placeholder="Enter message")
type_input = Input(placeholder="Enter type")
inputs  = Container(widgets=[title_input, message_input, type_input])
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter.

```python
card = Card(
    "Compare Images",
    content=Container([message_box, inputs, buttons]),
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
@button_open.click
def on_click():
    message_box.open()


@button_set.click
def on_click():
    data = {}
    if title_input.get_value() != "":
        data["title"] = title_input.get_value()
    if message_input.get_value() != "":
        data["message"] = message_input.get_value()
    if type_input.get_value() != "":
        data["type"] = type_input.get_value()
    message_box.set(data)
```

<!-- <p align="center">
  <img src="https://user-images.githubusercontent.com/120389559/227779108-bbb467d3-2706-45ef-8d8e-db92359eadd7.gif" alt="layout" />
</p> -->
