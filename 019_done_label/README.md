# Done Label

## Introduction

This widget display message with done label. In this tutorial you will learn how to use **`DoneLabel`** widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/done-label)

## Function signature

```python
done_label = DoneLabel(text="Task has been successfully finished")
```

![default-done-label](https://user-images.githubusercontent.com/79905215/217868944-f67172f9-7845-4f94-93ed-4184555f548e.png)

## Parameters

| Parameters  |                      Type                      |          Description           |
| :---------: | :--------------------------------------------: | :----------------------------: |
|    text    |                      str                       | Description text of widget |
|  widget_id  |                      str                       |        ID of the widget        |

### text

Description text of widget

**type:** `str`

**default value:** `None`

```python
done_label = DoneLabel(text="Some text")
```

![label-text](https://user-images.githubusercontent.com/79905215/217869730-2ace7121-8bfa-442e-ae84-d0ef6a1b8088.png)

### widget_id

ID of the widget.

**type:** `int`

**default value:** `None`

## Methods and attributes

|       Attributes and Methods        | Description                                |
| :---------------------------------: | ------------------------------------------ |
|               `text`               | Get `text` property.       |
|         `text(value: str)`         | Set `text` property.                |


## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/019_done_label/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/019_done_label/src/main.py)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, DoneLabel
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Initialize `DoneLabel` widget


```python
done_label = DoneLabel(
    text="Task has been successfully finished",
)
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widgets that we've just created in the `Container` widget.

```python
card = Card(
    title="Done Label",
    content=done_label,
)
layout = Container(widgets=[done_label])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```


![done-label](https://user-images.githubusercontent.com/79905215/217868616-b2dcc497-a424-4126-b4aa-0e03c4e09e23.png)