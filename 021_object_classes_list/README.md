# Object Classes List

## Introduction

In this tutorial you will learn how to use **`ObjectClassesList`** widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/object-classes-list)

## Function signature

```python
obj_classes_list = ObjectClassesList(
    object_classes=project_meta.obj_classes
)
```

![objclass-list-default](https://user-images.githubusercontent.com/79905215/218096273-0a52cc67-0ba8-4886-95a0-660e61d6a4eb.png)

## Parameters

|    Parameters    |                    Type                     |          Description          |
| :--------------: | :-----------------------------------------: | :---------------------------: |
| `object_classes` | `Union[ObjClassCollection, List[ObjClass]]` | collection or list of classes |
|   `selectable`   |                   `bool`                    |   Enable classes selection    |
|    `columns`     |                    `int`                    |       Number of columns       |
|    widget_id     |                     str                     |       id of the widget        |

### object_classes

ObjClassCollection object or list of ObjClass objects.

**type:** `Union[ObjClassCollection, List[ObjClass]]`

```python
obj_classes_list = ObjectClassesList(
    object_classes=project_meta.obj_classes
)
```

### selectable

Enable classes selection.

**type:** `Union[ObjClassCollection, List[ObjClass]]`

**default** `False`

```python
obj_classes_list = ObjectClassesList(
    object_classes=project_meta.obj_classes,
    selectable=True
)
```

![objclass-list](https://user-images.githubusercontent.com/79905215/218092421-a4c996bb-9679-428b-899d-4bb29d570112.png)

### columns

Number of columns.

**type:** `Union[ObjClassCollection, List[ObjClass]]`

```python
obj_classes_list = ObjectClassesList(
    object_classes=project_meta.obj_classes,
    columns=2
)
```

![objclass-list-columns](https://user-images.githubusercontent.com/79905215/218098608-4c22b892-24a0-4b93-8da4-812e0c08d333.png)

### widget_id

ID of the widget.

**type:** `str`

**default value:** `None`

## Methods and attributes

|  Attributes and Methods  | Description                               |
| :----------------------: | ----------------------------------------- |
| `get_selected_classes()` | Return list of selected classes. |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/021_object_classes_list/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/021_object_classes_list/src/main.py)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, ObjectClassesList
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Get Project ID from environment variables

```python
project_id = int(os.environ["modal.state.slyProjectId"])
```

### Get Project meta

```python
project_meta = sly.ProjectMeta.from_json(api.project.get_meta(project_id))
```

### Initialize `ObjectClassesList` widget

```python
obj_classes_list = ObjectClassesList(object_classes=project_meta.obj_classes)
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card = Card(
    title="Object Classes List",
    content=Container(widgets=[obj_classes_list]),
)
layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```

![objclass-list-default](https://user-images.githubusercontent.com/79905215/218096273-0a52cc67-0ba8-4886-95a0-660e61d6a4eb.png)
