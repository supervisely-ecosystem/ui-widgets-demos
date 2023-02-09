# Notification Box

## Introduction

This widget allows to display notification message. In this tutorial you will learn how to use **`NotificationBox`** widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/notification-box)

## Function signature

```python
note_box = NotificationBox(
    title="Notification Box",
    description="Lorem ipsum dolor sit amet...",
)
```

![default](https://user-images.githubusercontent.com/79905215/217855739-8303283a-f541-4172-880b-8afd7d5d867c.png)

## Parameters

| Parameters  |                      Type                      |          Description           |
| :---------: | :--------------------------------------------: | :----------------------------: |
|    title    |                      str                       | Main title of notification box |
| description |                      str                       |        Description text        |
|  box_type   | Literal["success", "info", "warning", "error"] |     Notification box style     |
|  widget_id  |                      str                       |        ID of the widget        |

### title

Main title of notification box

**type:** `str`

**default value:** `None`

```python
note_box = NotificationBox(title="Notification Box")
```

![note-title](https://user-images.githubusercontent.com/79905215/217857459-677008e8-a300-45d0-a06d-44f7c1650aa0.png)

### description

Description text

**type:** `str`

**default value:** `None`

```python
note_box = NotificationBox(description="Lorem ipsum dolor sit amet...")
```

![note-desc](https://user-images.githubusercontent.com/79905215/217858292-929ad1e6-26e9-4433-8f37-f45b24684483.png)

### box_type

Parameter to change notification style

**type:** `Literal["success", "info", "warning", "error"]`

**default value:** `"info"`

```python
note_box = NotificationBox(
    title="Notification Box",
    box_type="success"
)
```

![note-success](https://user-images.githubusercontent.com/79905215/217859149-3b603ada-f2b6-45dc-8890-5f569cdb40c1.png)

### widget_id

ID of the widget.

**type:** `int`

**default value:** `None`

## Methods and attributes

|       Attributes and Methods        | Description                                |
| :---------------------------------: | ------------------------------------------ |
|               `title`               | Get notification box title property.       |
|         `title(value: str)`         | Set notification box title.                |
|            `description`            | Get notification box description property. |
|      `description(value: str)`      | Set notification box description.          |
| `set(title: str, description: str)` | Set `title` and `description` properties.  |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/018_notification_box/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/018_notification_box/src/main.py)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, NotificationBox
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Initialize `NotificationBox` widget

In this tutorial we will use 4 types of notification box.

```python
note_box_desc = "Lorem ipsum dolor sit amet... anim id est laborum."

# initialize widgets we will use in UI
note_box_success = NotificationBox(
    title="Box type: SUCCESS", description=note_box_desc, box_type="success"
)
note_box_info = NotificationBox(
    title="Box type: INFO", description=note_box_desc, box_type="info"
)
note_box_warning = NotificationBox(
    title="Box type: WARNING", description=note_box_desc, box_type="warning"
)
note_box_error = NotificationBox(
    title="Box type: ERROR", description=note_box_desc, box_type="error"
)
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widgets that we've just created in the `Container` widget.

```python
notification_container = Container(
    widgets=[note_box_success, note_box_info, note_box_warning, note_box_error]
)

card = Card(
    title="Notification Box",
    content=notification_container,
)
layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```


![default](https://user-images.githubusercontent.com/79905215/217855760-cd7ce373-1f1e-4cd8-8ab2-3b86414b104d.png)
