# Object Class View

## Introduction

In this tutorial you will learn how to use **`ObjectClassView`** widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/object-class-view)

## Function signature

```python
obj_class_view = ObjectClassView(
    obj_class=sly.ObjClass("cat", sly.Bitmap, [255, 0, 0]),
    show_shape_text=True,
    show_shape_icon=True,
)
```

![objclass-default](https://user-images.githubusercontent.com/79905215/218079475-c5c5c032-8420-4850-b3fc-19dfc19c266a.png)

## Parameters

|   Parameters    |     Type     |         Description          |
| :-------------: | :----------: | :--------------------------: |
|    obj_class    | sly.ObjClass |   Supervisely object class   |
| show_shape_text |     bool     | If `True` display shape text |
| show_shape_icon |     bool     | If `True` display shape icon |
|    widget_id    |     str      |       ID of the widget       |

### obj_class

Description text of widget

**type:** `sly.ObjClass`

```python
obj_class = sly.ObjClass(name="cat", geometry_type=sly.Bitmap, color=[255, 0, 0])

obj_class_view = ObjectClassView(obj_class=obj_class)
```

### show_shape_text

Display object class text

**type:** `bool`

**default value:** `True`

```python
obj_class_view = ObjectClassView(obj_class=obj_class, show_shape_text=False)
```

![objclass-show-text](https://user-images.githubusercontent.com/79905215/218081019-0d0d2ebe-69a8-4e7d-b1ce-e647b005dd7b.png)

### show_shape_icon

Display object class icon

**type:** `bool`

**default value:** `False`

```python
obj_class_view = ObjectClassView(obj_class=obj_class, show_shape_icon=True)
```

![objclass-show-icon](https://user-images.githubusercontent.com/79905215/218080581-9344eb4a-3696-4c75-b9ff-8f1ec96722b7.png)

### widget_id

ID of the widget.

**type:** `str`

**default value:** `None`


## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/020_object_class_view/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/020_object_class_view/src/main.py)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, ObjectClassView
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Prepare `sly.ObjClass` object

```python
obj_class = sly.ObjClass(name="cat", geometry_type=sly.Bitmap, color=[255, 0, 0])
```

### Initialize `ObjectClassView` widget

```python
obj_class_view = ObjectClassView(
    obj_class=obj_class,
    show_shape_text=True,
    show_shape_icon=True,
)
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widgets that we've just created in the `Container` widget.

```python
card = Card(
    title="ObjClass View",
    content=obj_class_view,
)
layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```

![objclass-default](https://user-images.githubusercontent.com/79905215/218079475-c5c5c032-8420-4850-b3fc-19dfc19c266a.png)
