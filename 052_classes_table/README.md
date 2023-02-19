# Classes Table

## Introduction

In this tutorial you will learn how to use `ClassesTable` widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/ClassesTable)

## Function signature

```python
ClassesTable(project_meta=None, project_id=None, project_fs=None, allowed_types=None, selectable=True, disabled=False, widget_id=None)
```

![project_id](https://user-images.githubusercontent.com/120389559/219954018-a0d76d1e-d617-4729-9f8f-62ad688031ad.png)

## Parameters

|  Parameters   |       Type       |                                Description                                 |
| :-----------: | :--------------: | :------------------------------------------------------------------------: |
| project_meta  |  `ProjectMeta`   |                            Input `ProjectMeta`                             |
|  project_id   |       int        |                              Input project ID                              |
|  project_fs   |    `Project`     |                              Input `Project`                               |
| allowed_types | List[`Geometry`] | `Geometry` types witch will not be display from all types in given project |
|  selectable   |       bool       |                    Whether the component is selectable                     |
|   disabled    |       bool       |                     Whether the component is disabled                      |
|   widget_id   |       str        |                              Id of the widget                              |

### project_meta

Determine input `ProjectMeta`.

**type:** `ProjectMeta`

**default value:** `None`

```python
meta_json = api.project.get_meta(id=project_id)
meta = sly.ProjectMeta.from_json(data=meta_json)
classes_table = ClassesTable(project_meta=meta)
```

![project_meta](https://user-images.githubusercontent.com/120389559/219953958-f31b1c04-4a2e-4be4-8f48-039b71ebb2f9.png)

### project_id

Determine input project ID.

**type:** `int`

**default value:** `None`

```python
classes_table = ClassesTable(project_id=project_id)
```

![project_id](https://user-images.githubusercontent.com/120389559/219954018-a0d76d1e-d617-4729-9f8f-62ad688031ad.png)

### project_fs

Determine input `Project`, upload it from local host.

**type:** `Project`

**default value:** `None`

```python
project_path = "/home/admin/work/supervisely/projects/lemons_annotated"
project = sly.Project(project_path, sly.OpenMode.READ)
classes_table = ClassesTable(project_fs=project)
```

![project](https://user-images.githubusercontent.com/120389559/219954018-a0d76d1e-d617-4729-9f8f-62ad688031ad.png)

### allowed_types

Determine `Geometry` types witch will not be display from all types in given project.

**type:** `List[Geometry]`

**default value:** `None`

```python
classes_table = ClassesTable(project_id=project_id, allowed_types=[sly.Bitmap])
```

![allowed_types](https://user-images.githubusercontent.com/120389559/219954233-dd463cec-b385-4386-b951-3b017df55f3e.png)

### selectable

Determine whether the component is selectable.

**type:** `bool`

**default value:** `True`

```python
classes_table = ClassesTable(project_id=project_id, selectable=False)
```

![selectable](https://user-images.githubusercontent.com/120389559/219954378-3ddb4098-93c7-49fe-9a8d-dc49515d60a6.png)

### disabled

Determine whether the component is disabled.

**type:** `bool`

**default value:** `False`

```python
classes_table = ClassesTable(project_id=project_id, disabled=True)
```

![disabled](https://user-images.githubusercontent.com/120389559/219955255-6b2a7075-8e58-4934-9ab4-b3dbb4c11ce8.gif)

### widget_id

ID of the widget.

**type:** `str`

**default value:** `None`

## Methods and attributes

|  Attributes and Methods  | Description                                                  |
| :----------------------: | ------------------------------------------------------------ |
|      `read_meta()`       | Read given `ProjectMeta`.                                    |
|     `read_project()`     | Read given `Project`.                                        |
| `read_project_from_id()` | Read given `Project` by ID.                                  |
| `get_selected_classes()` | Return list of selected classes.                             |
|   `clear_selection()`    | Clear selected data.                                         |
|    `value_changed()`     | Decorator function is handled when input value is changed.   |
|       `loading()`        | Decorator function is handled when input value is uplouding. |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/052_classes_table/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/052_classes_table/src/main.py)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, ClassesTable
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Initialize `ClassesTable` widget

```python
project_id = int(os.environ["modal.state.slyProjectId"])
classes_table = ClassesTable(project_id=project_id)
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card = Card(
    title="Classes Table",
    content=classes_table,
)

layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```

![layout](https://user-images.githubusercontent.com/120389559/219955799-4f8abe96-8995-4c2a-bf19-61be6cd119d3.gif)
