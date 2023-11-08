# Message Box

## Introduction

**`MessageBox`** widget can be used for displaying alerts, notifications, or important information to users. Widget consists of a button and a Dialog window. When the button is clicked, the Dialog window opens and displays the message. The Dialog window can be closed by clicking the "OK" button or by clicking outside the Dialog window.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/widgets/text-elements/messagebox)

## Function signature

```python
message_box = MessageBox(
    title="Message Box",
    message="This widget can be used for displaying alerts, notifications, or important information to users.",
    button_text="Open MessageBox",
    type="info",
)
```

![default](https://github.com/supervisely-ecosystem/ui-widgets-demos/assets/48913536/d79bf71d-b72e-4020-8b81-f763df7d3d10)

## Parameters

|  Parameters   |                     Type                      |                  Description                   |
| :-----------: | :-------------------------------------------: | :--------------------------------------------: |
|    `title`    |                     `str`                     |            Title of the message box            |
|   `message`   |                     `str`                     | Text that will be displayed in the message box |
|    `type`     | `Literal["info", "warning", "error", "text"]` |                  Message type                  |
| `button_text` |                     `str`                     |     Text on the button to open message box     |
|  `widget_id`  |                     `str`                     |                ID of the widget                |

### title

Title of the message box. Will be displayed in the header.

**type:** `str`

**default value:** `str`

```python
message_box = MessageBox(title="Custom Title")
```

![title](https://github.com/supervisely-ecosystem/ui-widgets-demos/assets/48913536/34bbf30f-4d94-4e48-829e-5f86826377ce)

### message

Text that will be displayed in the message box.

**type:** `str`

**default value:** `str`

```python
message_box = MessageBox(
    title="Message Box",
    message="Lorem ipsum dolor sit amet ...",
    type="info",
)
```

![message](https://github.com/supervisely-ecosystem/ui-widgets-demos/assets/48913536/8e6ec736-9f8a-4616-b631-ae37cd94f034)

### type

Message type

**type:** `Literal["info", "warning", "error", "text"]`

**default value:** `"info"`

```python
message_box = MessageBox(
    title="Message Box",
    message="Lorem ipsum dolor sit amet ...",
    type="info",
)
```

![type](https://github.com/supervisely-ecosystem/ui-widgets-demos/assets/48913536/9f2d8fab-3328-4b76-ae13-6655875b1b90)

### button_text

Text on the button to open message box.

**type:** `str`

**default value:** `"Open MessageBox"`

```python
message_box = MessageBox(button_text="Click Me!")
```

![button_text](https://github.com/supervisely-ecosystem/ui-widgets-demos/assets/48913536/3cccf989-3303-40ca-b373-ad02b6aca2c1)

### widget_id

ID of the widget.

**type:** `str`

**default value:** `None`

## Methods and attributes

| Attributes and Methods | Description               |
| :--------------------: | ------------------------- |
|    `set_message()`     | Set message text and type |
|    `get_message()`     | Get current message text  |
|      `get_type()`      | Get current message type  |

## Mini App Example

You can find this example in our GitHub repository:

[supervisely-ecosystem/ui-widgets-demos/text-elements/007_message_box/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/text-elements/007_message_box/src/main.py)

### Import libraries

```python
import os
from dotenv import load_dotenv
import supervisely as sly
from supervisely.app.widgets import Card, Flexbox, MessageBox

```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Create MessageBox widgets for each available type of message: info, warning, error, text.

```python
message_box_info = MessageBox(
    title="Info",
    message="Lorem ipsum dolor sit amet ...",
    type="info",
    button_text="Info",
)

message_box_warning = MessageBox(
    title="Warning",
    message="Lorem ipsum dolor sit amet ...",
    type="warning",
    button_text="Warning",
)

message_box_error = MessageBox(
    title="Error",
    message="Lorem ipsum dolor sit amet ...",
    type="error",
    button_text="Error",
)

message_box_text = MessageBox(
    title="Text",
    message="Lorem ipsum dolor sit amet ...",
    type="text",
    button_text="Text",
)
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Flexbox` widget.

```python
card = Card(
    title="MessageBox",
    content=Flexbox(
        [message_box_info, message_box_warning, message_box_error, message_box_text],
        center_content=True,
    ),
)
layout = card
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=card)
```

![miniapp-min](https://github.com/supervisely-ecosystem/ui-widgets-demos/assets/48913536/d6839221-3dac-4b26-b811-ba853052cc9e)
