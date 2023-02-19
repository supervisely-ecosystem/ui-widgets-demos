# ElementButton

## Introduction

In this tutorial you will learn how to use `LinePlot` widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/LinePlot)

## Function signature

```python
LinePlot(title, series=[], smoothing_weight=0, group_key=None, show_legend=True, decimals_in_float=2, xaxis_decimals_in_float=None, yaxis_interval=None, widget_id=None, yaxis_autorescale=True)
```

![default](https://user-images.githubusercontent.com/120389559/219958867-13bb604e-d890-475d-ab46-8b41063620ba.png)

## Parameters

|       Parameters        | Type |             Description             |
| :---------------------: | :--: | :---------------------------------: |
|          title          | str  |          `LinePlot` title           |
|         series          | list |      List of input data series      |
|    smoothing_weight     | int  |              Smoothing              |
|        group_key        | str  |          Synced charts key          |
|       show_legend       | bool |      Show legend on `LinePlot`      |
|    decimals_in_float    | int  | Whether the component is selectable |
| xaxis_decimals_in_float | int  |  Whether the component is disabled  |
|     yaxis_interval      | list |          Id of the widget           |
|        widget_id        | str  |          Id of the widget           |
|    yaxis_autorescale    | bool |          Id of the widget           |

### title

Determine `LinePlot` title .

**type:** `str`

```python
line_chart = LinePlot(title="Max vs Denis")
```

![title](https://user-images.githubusercontent.com/120389559/219959818-7f392fac-7d2e-4bfc-b54e-850dd8f3d75f.png)

### series

Determine list of input data series.

**type:** `list`

**default value:** `[]`

```python
line_chart = LinePlot(
    title="Max vs Denis",
    series=[{"name": "Max", "data": s1}, {"name": "Denis", "data": s2}],
)
```

![series](https://user-images.githubusercontent.com/120389559/219959947-59a77142-1208-4bac-b371-0fa54e93afd2.png)

### smoothing_weight

Determine `LinePlot` smoothing.

**type:** `int`

**default value:** `0`

```python
line_chart = LinePlot(
    title="Max vs Denis",
    series=[{"name": "Max", "data": s1}, {"name": "Denis", "data": s2}],
    smoothing_weight=3,
)
```

![smoothing_weight](https://user-images.githubusercontent.com/120389559/219960053-5c90d279-c6a6-4390-8c2e-eef016b661d3.png)

### group_key

Synced `LinePlot` key.

**type:** `str`

**default value:** `None`

### show_legend

Determine showing legend on `LinePlot`.

**type:** `bool`

**default value:** `True`

```python
line_chart = LinePlot(
    title="Max vs Denis",
    series=[{"name": "Max", "data": s1}, {"name": "Denis", "data": s2}],
    show_legend=False,
)
```

![show_legend](https://user-images.githubusercontent.com/120389559/219960471-ba7f3745-25c6-4b76-bdec-5583f516be10.png)

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
