# Model Info

## Introduction

In this tutorial you will learn how to use `ModelInfo` widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervisely.com/app-development/widgets/status-elements/modelinfo)

## Function signature

```python
ModelInfo(session_id=None, team_id=None, widget_id=None)
```

![default](https://user-images.githubusercontent.com/120389559/219638497-b20cda0e-ec0b-40dc-925d-21cadf9b19d6.png)

## Parameters

|  Parameters  | Type  |   Description    |
| :----------: | :---: | :--------------: |
| `session_id` | `int` |   `Session` ID   |
|  `team_id`   | `int` |    `Team` ID     |
| `widget_id`  | `str` | Id of the widget |

### session_id

Determines `Session` ID for which model data will be displayed.

**type:** `int`

**default value:** `None`

### team_id

Determines `Team` ID for which model data will be displayed.

**type:** `int`

**default value:** `None`

### widget_id

ID of the widget.

**type:** `str`

**default value:** `None`

## Methods and attributes

|      Attributes and Methods       | Description                                  |
| :-------------------------------: | -------------------------------------------- |
| `set_session_id(session_id: int)` | Set given `session_id` value in `ModelInfo`. |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/status-elements/007_model_info/src/main.py](<https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/status elements/007_model_info/src/main.py>)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, ModelInfo
```

### Initialize `session_id` we will use

```python
session_id = int(os.environ["context.sessionId"])
```

### Initialize `ModelInfo` widget and set `session_id`

```python
model_stats = ModelInfo()
model_stats.set_session_id(session_id=session_id)
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card = Card(
    title="Model Info",
    content=Container(widgets=[model_stats]),
)

layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```
