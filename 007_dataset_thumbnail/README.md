# Dataset thumbnail

## Introduction

In this tutorial you will learn how to use `DatasetThumbnail` widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/DatasetThumbnail)

## Function signature

```python
DatasetThumbnail(project_info=None, dataset_info=None, show_project_name=True, widget_id=None)
```

![default](https://user-images.githubusercontent.com/79905215/213988894-d4420e3e-5003-431b-8be1-01b1ddbf98df.png)

## Parameters

|    Parameters     |    Type     |                   Description                    |
| :---------------: | :---------: | :----------------------------------------------: |
|   project_info    | ProjectInfo | NamedTuple, containing information about project |
|   dataset_info    | DatasetInfo | NamedTuple, containing information about dataset |
| show_project_name |    bool     |        determines to display project name        |
|     widget_id     |     int     |                 id of the widget                 |

### project_info

NamedTuple, containing information about project.

**type:** `ProjectInfo`

**default value:** `None`

```python
project = api.project.get_info_by_id(project_id)
dataset_thumbnail = DatasetThumbnail(project_info=project)
```

### dataset_info

NamedTuple, containing information about dataset.

**type:** `DatasetInfo`

**default value:** `None`

```python
dataset = api.dataset.get_info_by_id(id=dataset_id)
dataset_thumbnail = DatasetThumbnail(dataset_info=dataset)
```

![dataset_info](https://user-images.githubusercontent.com/79905215/213988894-d4420e3e-5003-431b-8be1-01b1ddbf98df.png)

### show_project_name

Determines to display project name.

**type:** `bool`

**default value:** `True`

```python
project = api.project.get_info_by_id(project_id)
dataset = api.dataset.get_info_by_id(dataset_id)
dataset_thumbnail = DatasetThumbnail(project_info=project, dataset_info=dataset, show_project_name=False)
```

![show_project_name](https://user-images.githubusercontent.com/79905215/213988894-d4420e3e-5003-431b-8be1-01b1ddbf98df.png)

### widget_id

ID of the widget.

**type:** `int`

**default value:** `None`

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/007_dataset_thumbnail/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/007_dataset_thumbnail/src/main.py)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, DatasetThumbnail
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Initialize `ProjectThumbnail` widget

```python
# get project and dataset info from server
project_id = int(os.environ["modal.state.slyProjectId"])
project = api.project.get_info_by_id(project_id)
dataset_id = int(os.environ["modal.state.slyDatasetId"])
dataset = api.dataset.get_info_by_id(id=dataset_id)

dataset_thumbnail = DatasetThumbnail(project_info=project, dataset_info=dataset)
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
# create new cards
card = Card(
    title="Dataset Thumbnail",
    content=Container(widgets=[dataset_thumbnail]),
)
layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```
