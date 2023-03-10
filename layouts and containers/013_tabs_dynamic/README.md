# Tabs Dynamic

## Introduction

**`TabsDynamic`** is a versatile widget in Supervisely that allows users to display and edit YAML files within their info, such as NN model settings. The widget can divide the YAML file into separate tabs, making it easier to navigate and manage complex data structures. Additionally, users can edit the YAML directly within the widget and obtain a merged YAML file with their changes. `TabsDynamic` also enables users to get or set the active tab from code.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/widgets/layouts-and-containers/tabsdynamic)

## Function signature

```python
TabsDynamic(
    filepath_or_raw_yaml,
    type="border-card",
    disabled=False,
    widget_id=None,
)
```

![default](https://user-images.githubusercontent.com/120389559/222425009-48e94882-6a1a-4cf5-9383-45bc98dc4bb9.png)

## Parameters

|       Parameters       |               Type               |          Description           |
| :--------------------: | :------------------------------: | :----------------------------: |
| `filepath_or_raw_yaml` |              `str`               |  Path to yaml file or string   |
|         `type`         | `Literal["card", "border-card"]` | Determine style of widget tabs |
|       `disabled`       |              `bool`              |         Disable widget         |
|      `widget_id`       |              `str`               |        ID of the widget        |

### filepath_or_raw_yaml

Determine path to yaml input file or string.

**type:** `str`

```python
yaml_path = "layouts and containers/013_tabs_dynamic/yaml/file_1.yaml"
tabs_dynamic = TabsDynamic(yaml_path)
```

![default](https://user-images.githubusercontent.com/120389559/222425009-48e94882-6a1a-4cf5-9383-45bc98dc4bb9.png)

### type

Determine style of widget tabs.

**type:** `Literal["card", "border-card"]`

**default value:** `border-card`

```python
yaml_path = "layouts and containers/013_tabs_dynamic/yaml/file_1.yaml"
tabs_dynamic = TabsDynamic(yaml_path, type="card")
```

![card](https://user-images.githubusercontent.com/79905215/224246883-68b34954-1327-49bb-b65f-50ad4ca626b3.png)

```python
yaml_path = "layouts and containers/013_tabs_dynamic/yaml/file_1.yaml"
tabs_dynamic = TabsDynamic(yaml_path, type="border-card")
```

![border](https://user-images.githubusercontent.com/79905215/224246903-45ca7f8f-2655-4a35-885a-5874416084ad.png)

### disabled

Disable widget.

**type:** `bool`

**default value:** `false`

```python
yaml_path = "layouts and containers/013_tabs_dynamic/yaml/file_1.yaml"
tabs_dynamic = TabsDynamic(yaml_path, disabled=True)
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/120389559/222424295-9210067b-3113-4ceb-8f71-8f49ed964a3c.gif" alt="disabled" />
</p>

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

[supervisely-ecosystem/ui-widgets-demos/layouts-and-containers/tabs_dynamic/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/layouts-and-containers/tabs_dynamic/src/main.py)

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
yaml_path = "layouts and containers/013_tabs_dynamic/yaml/file_1.yaml"
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

<p align="center">
  <img src="https://user-images.githubusercontent.com/120389559/222417044-1ebf8551-8208-420b-9fb7-bb11f8328a06.gif" alt="layout" />
</p>
