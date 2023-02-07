# Select Dataset

## Introduction

This widget is a select dataset input, clicking on it can be processed from python code. In this tutorial you will learn how to use `SelectDataset` widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/SelectDataset)

## Function signature

```python
SelectDataset(default_id=None, project_id=None, multiselect=False, compact=False, show_label=True, size=None, disabled=False, widget_id=None)
```

![default](https://user-images.githubusercontent.com/79905215/216376305-1556627a-ef61-4df7-900c-ac2ffbb9c8d0.png)

## Parameters

| Parameters  |               Type                |                   Description                   |
| :---------: | :-------------------------------: | :---------------------------------------------: |
| default_id  |                int                |                   Dataset ID                    |
| project_id  |                int                |                   Project ID                    |
| multiselect |               bool                | Allow to select all datasets in current project |
|   compact   |               bool                |            Show only dataset select             |
| show_label  |               bool                |                   Show label                    |
|    size     | Literal["large", "small", "mini"] |        Selector size (large/small/mini)         |
|  disabled   |               bool                |             Disable dataset select              |
|  widget_id  |                int                |                Id of the widget                 |

### default_id

Determine Dataset will be selected by default.

**type:** `int`

**default value:** `None`

```python
select_project = SelectDataset(default_id=dataset_id)
```

![default_id](https://user-images.githubusercontent.com/79905215/216376305-1556627a-ef61-4df7-900c-ac2ffbb9c8d0.png)

### project_id

Determine project will be selected by default.

**type:** `int`

**default value:** `None`

```python
select_project = SelectDataset(project_id=project_id)
```

![project_id](https://user-images.githubusercontent.com/79905215/216376305-1556627a-ef61-4df7-900c-ac2ffbb9c8d0.png)

### multiselect

Allow to select all datasets in current project.

**type:** `bool`

**default value:** `false`

```python
select_dataset = SelectDataset(default_id=dataset_id, project_id=project_id, multiselect=True)
```

![multiselect](https://user-images.githubusercontent.com/79905215/216376305-1556627a-ef61-4df7-900c-ac2ffbb9c8d0.png)

### compact

Show only dataset select.

**type:** `bool`

**default value:** `false`

```python
select_dataset = SelectDataset(default_id=dataset_id, project_id=project_id, compact=True)
```

![compact](https://user-images.githubusercontent.com/79905215/216376305-1556627a-ef61-4df7-900c-ac2ffbb9c8d0.png)

### show_label

Determine show text `Dataset` on widget or not, work only if `compact` is True.

**type:** `bool`

**default value:** `True`

```python
select_dataset = SelectDataset(
    default_id=dataset_id, project_id=project_id, compact=True, show_label=False
)
```

![show_label](https://user-images.githubusercontent.com/79905215/216376305-1556627a-ef61-4df7-900c-ac2ffbb9c8d0.png)

### size

Size of input.

**type:** `Literal["large", "small", "mini"]`

**default value:** `None`

### disabled

Determine dataset select ability.

**type:** `bool`

**default value:** `false`

```python
select_dataset = SelectDataset(default_id=dataset_id, project_id=project_id, disabled=True)
```

![disabled](https://user-images.githubusercontent.com/79905215/216376305-1556627a-ef61-4df7-900c-ac2ffbb9c8d0.png)

### widget_id

ID of the widget.

**type:** `int`

**default value:** `None`

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/011_select_dataset/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/011_select_dataset/src/main.py)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, SelectDataset
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Prepare project_id and dataset_id

```python
project_id = int(os.environ["modal.state.slyProjectId"])
dataset_id = int(os.environ["modal.state.slyDatasetId"])
```

### Initialize `SelectDataset` widget

```python
select_dataset = SelectDataset(
    default_id=dataset_id,
    project_id=project_id,
)
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card = Card(
    title="Select Dataset",
    content=Container(widgets=[select_dataset]),
)

layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```
