# Done Label

## Introduction

This widget display message with done label. In this tutorial you will learn how to use **`DoneLabel`** widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/done-label)

## Function signature

```python
done_label = DoneLabel(text="Task has been successfully finished")
```

![label-default](https://user-images.githubusercontent.com/79905215/218078545-53840478-4f2d-4b74-a4c7-2838efba93b9.png)

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

![label-text](https://user-images.githubusercontent.com/79905215/218078983-94449c90-3436-4da8-8107-cbdc29c416c0.png)

### widget_id

ID of the widget.

**type:** `str`

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


![label-default](https://user-images.githubusercontent.com/79905215/218078545-53840478-4f2d-4b74-a4c7-2838efba93b9.png)