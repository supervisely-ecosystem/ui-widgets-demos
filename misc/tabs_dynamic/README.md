# Tabs Dynamic

## Introduction

In this tutorial you will learn how to use `TabsDynamic` widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/tabsdynamic)

## Function signature

```python
TabsDynamic(filepath_or_raw_yaml, type="border-card", disabled=False, widget_id=None)
```

![default](https://user-images.githubusercontent.com/120389559/222417044-1ebf8551-8208-420b-9fb7-bb11f8328a06.gif)

## Parameters

|       Parameters       |               Type               |         Description         |
| :--------------------: | :------------------------------: | :-------------------------: |
| `filepath_or_raw_yaml` |              `str`               | Path to yaml file or string |
|         `type`         | `Literal["card", "border-card"]` |     Output format type      |
|       `disabled`       |              `bool`              |       Disable widget        |
|      `widget_id`       |              `str`               |      Id of the widget       |

### filepath_or_raw_yaml

Determine path to yaml input file or string.

**type:** `str`

```python
yaml_path = "misc/tabs_dynamic/src/yaml"
tabs_dynamic = TabsDynamic(yaml_path)
```

### type

Determine output format type.

**type:** `Literal["card", "border-card"]`

**default value:** `border-card`

```python
yaml_path = "misc/tabs_dynamic/src/yaml"
tabs_dynamic = TabsDynamic(yaml_path, type="card")
```

![type](https://user-images.githubusercontent.com/120389559/222423429-e08a2bf5-54c0-4bf7-8137-f393e2389bbc.gif)

### disabled

Disable widget.

**type:** `bool`

**default value:** `false`

```python
yaml_path = "misc/tabs_dynamic/src/yaml"
tabs_dynamic = TabsDynamic(yaml_path, disabled=True)
```

![disabled](https://user-images.githubusercontent.com/120389559/222424295-9210067b-3113-4ceb-8f71-8f49ed964a3c.gif)

### widget_id

ID of the widget.

**type:** `str`

**default value:** `None`

## Methods and attributes

| Attributes and Methods | Description         |
| :--------------------: | ------------------- |
|   `set_active_tab()`   | Set active tab.     |
|   `get_active_tab()`   | Return active tab.  |
|  `get_merged_yaml()`   | Return merged yaml. |
|      `disable()`       | Disable widget.     |
|       `enable()`       | Enable widget.      |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/misc/tabs_dynamic/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/misc/tabs_dynamic/src/main.py)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, TabsDynamic
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Initialize `TabsDynamic` widget

```python
yaml_path = "misc/tabs_dynamic/src/yaml"
tabs_dynamic = TabsDynamic(yaml_path)
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card = Card(title="TabsDynamic", content=Container([tabs_dynamic]))
layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```

![layout](https://user-images.githubusercontent.com/120389559/222425009-48e94882-6a1a-4cf5-9383-45bc98dc4bb9.png)
