# CopyToClipboard

## Introduction

`CopyToClipboard` widget allows you to wrap your widget with copy button.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/сopyеoсlipboard)

## Function signature

```python
CopyToClipboard(
    content="", 
    widget_id=None
)
```

![default](https://user-images.githubusercontent.com/120389559/224316390-de355f21-bf5b-4dca-9619-43cc523562f9.png)

## Parameters

| Parameters  |                     Type                      |        Description        |
| :---------: | :-------------------------------------------: | :-----------------------: |
|  `content`  | `Union[Editor, Text, TextArea, Input, str]`   | `CopyToClipboard` content |
| `widget_id` |                     `str`                     |     Id of the widget      |

### content

Determine input `CopyToClipboard` content.

**type:** `Union[Editor, Text, TextArea, Input, str]`

**default value:** `""`

```python
copy_to_clipboard = CopyToClipboard(content="Some Text")
```

![content](https://user-images.githubusercontent.com/120389559/224316855-4dd7d72a-3818-44f5-bc74-7a83ac1a82ab.png)

### widget_id

ID of the widget.

**type:** `str`

**default value:** `None`

## Methods and attributes

| Attributes and Methods  | Description               |
| :---------------------: | ------------------------- |
|    `get_json_data()`    | Get data in dict format.  |
|    `get_json_state()`   | Get state in dict format. |
|     `get_content()`     | Return wrapped content.   |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/misc/copy_to_clipboard/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/misc/copy_to_clipboard/src/main.py)s

### Import libraries

```python
import os, markdown

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import (
    Card,
    Container,
    CopyToClipboard,
    Button,
    Editor,
    Text,
    TextArea,
    Input,
)
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Initialize different inputs

```python
editor = Editor('{ "value": 10 }', show_line_numbers=True)
text = Text(text="Text", status="success")
text_area = TextArea(value="TextArea")
input = Input(value="Input", size="large")
string = "Only string"

copytoclipboard1 = CopyToClipboard(content=editor)
copytoclipboard2 = CopyToClipboard(content=input)
copytoclipboard3 = CopyToClipboard(content=text)
copytoclipboard4 = CopyToClipboard(content=text_area)
copytoclipboard5 = CopyToClipboard(content=string)
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card = Card(
    title="Copy To Clipboard",
    content=Container(
        [
            copytoclipboard1,
            copytoclipboard2,
            copytoclipboard3,
            copytoclipboard4,
            copytoclipboard5,
        ]
    ),
)
layout = Container(widgets=[card], direction="vertical")
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```

![layout](https://user-images.githubusercontent.com/120389559/224319059-a601a2a4-fc67-4551-bf22-df3b621f9260.gif)
