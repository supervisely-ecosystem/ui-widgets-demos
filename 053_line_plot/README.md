# Line Plot

## Introduction

In this tutorial you will learn how to use `LinePlot` widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/LinePlot)

## Function signature

```python
LinePlot(title, series=[], smoothing_weight=0, group_key=None, show_legend=True, decimals_in_float=2, xaxis_decimals_in_float=None, yaxis_interval=None, widget_id=None, yaxis_autorescale=True)
```

![default](https://user-images.githubusercontent.com/120389559/219958867-13bb604e-d890-475d-ab46-8b41063620ba.png)

## Parameters

|       Parameters        | Type |                         Description                          |
| :---------------------: | :--: | :----------------------------------------------------------: |
|          title          | str  |                       `LinePlot` title                       |
|         series          | list |                  List of input data series                   |
|    smoothing_weight     | int  |                          Smoothing                           |
|        group_key        | str  |                      Synced charts key                       |
|       show_legend       | bool |                  Show legend on `LinePlot`                   |
|    decimals_in_float    | int  | The number of fractions to display floating values in y-axis |
| xaxis_decimals_in_float | int  | The number of fractions to display floating values in x-axis |
|     yaxis_interval      | list |          Min and max values on y axis (e.g. [0, 1])          |
|        widget_id        | str  |                       Id of the widget                       |
|    yaxis_autorescale    | bool |                       Id of the widget                       |

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

![series](https://user-images.githubusercontent.com/120389559/220658262-3d4af3e6-70cd-4b02-9a75-18046d4bc401.png)

### smoothing_weight

Determine `LinePlot` smoothing.

**type:** `int`

**default value:** `0`

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

![show_legend](https://user-images.githubusercontent.com/120389559/220660068-1801f5ad-fc21-4ab5-88e4-6f30a5d0a0e4.png)

### decimals_in_float

The number of fractions to display floating values in y-axis.

**type:** `int`

**default value:** `2`

### xaxis_decimals_in_float

The number of fractions to display floating values in x-axis.

**type:** `int`

**default value:** `None`

```python
line_chart = LinePlot(
    title="Max vs Denis",
    series=[{"name": "Max", "data": s1}, {"name": "Denis", "data": s2}],
    xaxis_decimals_in_float=44,
)
```

![xaxis_decimals_in_float](https://user-images.githubusercontent.com/120389559/220661506-646cc687-bc27-445d-8f05-0b3a2b2efccf.png)

### yaxis_interval

Determine min and max values on y axis (e.g. [0, 1]).

**type:** `list`

**default value:** `None`

```python
line_chart = LinePlot(
    title="Max vs Denis",
    series=[{"name": "Max", "data": s1}, {"name": "Denis", "data": s2}],
    yaxis_interval=[0, 200],
)
```

![yaxis_interval](https://user-images.githubusercontent.com/120389559/220662241-f6e86fd9-0410-4e8f-bd18-859e5dfc6dc9.png)

### widget_id

ID of the widget.

**type:** `str`

**default value:** `None`

### yaxis_autorescale

Determine min and max values on y axis (e.g. [0, 1]).

**type:** `bool`

**default value:** `True`

```python
line_chart = LinePlot(
    title="Max vs Denis",
    series=[{"name": "Max", "data": s1}, {"name": "Denis", "data": s2}],
    yaxis_interval=[0, 200],
)
```

![yaxis_autorescale](https://user-images.githubusercontent.com/120389559/220662241-f6e86fd9-0410-4e8f-bd18-859e5dfc6dc9.png)

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
