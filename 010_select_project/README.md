# Select Project

## Introduction

This widget is a select project input, clicking on it can be processed from python code. In this tutorial you will learn how to use `SelectProject` widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/SelectProject)

## Function signature

```python
SelectProject(default_id=None, workspace_id=None, compact=False, allowed_types=[], show_label=True, size=None, widget_id=None)
```

![default](https://user-images.githubusercontent.com/79905215/216376305-1556627a-ef61-4df7-900c-ac2ffbb9c8d0.png)

## Parameters

|  Parameters   |               Type                |                       Description                       |
| :-----------: | :-------------------------------: | :-----------------------------------------------------: |
|  default_id   |                int                |                       Project ID                        |
| workspace_id  |                int                |                      Workspace ID                       |
|    compact    |               bool                |             Check Workspace ID is not None              |
| allowed_types |         List[ProjectType]         | List of project types witch will be available to select |
|  show_label   |               bool                |                       Show label                        |
|     size      | Literal["large", "small", "mini"] |            Selector size (large/small/mini)             |
|   widget_id   |                int                |                    Id of the widget                     |

### default_id

Determine `Project` will be selected by default.

**type:** `int`

**default value:** `None`

```python
select_project = SelectProject(default_id=project_id)
```

![default_id](https://user-images.githubusercontent.com/79905215/216376305-1556627a-ef61-4df7-900c-ac2ffbb9c8d0.png)

### workspace_id

Determine `Workspace` will be selected by default.

**type:** `int`

**default value:** `None`

```python
select_project = SelectProject(workspace_id=workspace_id)
```

![workspace_id](https://user-images.githubusercontent.com/79905215/216376305-1556627a-ef61-4df7-900c-ac2ffbb9c8d0.png)

### compact

Show only `Project` select.

**type:** `bool`

**default value:** `false`

```python
select_project = SelectProject(default_id=project_id, workspace_id=workspace_id, compact=True)
```

![compact](https://user-images.githubusercontent.com/79905215/216376305-1556627a-ef61-4df7-900c-ac2ffbb9c8d0.png)

### allowed_types

List of project types witch will be available to select.

**type:** `List[ProjectType]`

**default value:** `[]`

### show_label

Determine show text `Project` on widget or not, work only if `compact` is True.

**type:** `bool`

**default value:** `True`

```python
select_project = SelectProject(
    default_id=project_id, workspace_id=workspace_id, compact=True, show_label=False
)
```

![show_label](https://user-images.githubusercontent.com/79905215/216376305-1556627a-ef61-4df7-900c-ac2ffbb9c8d0.png)

### size

Size of input.

**type:** `Literal["large", "small", "mini"]`

**default value:** `None`

### widget_id

ID of the widget.

**type:** `int`

**default value:** `None`

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/010_select_project/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/010_select_project/src/main.py)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, SelectProject
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Prepare project_id and workspace_id

```python
workspace_id = int(os.environ["modal.state.slyWorkspaceId"])
project_id = int(os.environ["modal.state.slyProjectId"])
```

### Initialize `SelectProject` widget

```python
select_project = SelectProject(
    default_id=project_id,
    workspace_id=workspace_id,
)
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card = Card(
    title="Select Project",
    content=Container(widgets=[select_project]),
)

layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```
