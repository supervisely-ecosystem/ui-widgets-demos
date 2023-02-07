# Select Team

## Introduction

This widget is a select `Team` input, clicking on it can be processed from python code. In this tutorial you will learn how to use `SelectTeam` widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/SelectWorkspace)

## Function signature

```python
SelectTeam(default_id=None, show_label=True, size=None, widget_id=None)
```

![default](https://user-images.githubusercontent.com/79905215/216376305-1556627a-ef61-4df7-900c-ac2ffbb9c8d0.png)

## Parameters

| Parameters |               Type                |           Description            |
| :--------: | :-------------------------------: | :------------------------------: |
| default_id |                int                |             Team ID              |
| show_label |               bool                |            Show label            |
|    size    | Literal["large", "small", "mini"] | Selector size (large/small/mini) |
| widget_id  |                int                |         Id of the widget         |

### default_id

Determine `Team` will be selected by default.

**type:** `int`

**default value:** `None`

```python
select_team = SelectTeam(default_id=team_id)
```

![default_id](https://user-images.githubusercontent.com/79905215/216376305-1556627a-ef61-4df7-900c-ac2ffbb9c8d0.png)

### show_label

Determine show text `Team` on widget or not.

**type:** `bool`

**default value:** `True`

```python
select_team = SelectTeam(default_id=team_id, show_label=False)
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

[supervisely-ecosystem/ui-widgets-demos/013_select_team/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/013_select_team/src/main.py)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, SelectTeam
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Prepare team_id

```python
team_id = int(os.environ["modal.state.slyTeamId"])
```

### Initialize `SelectTeam` widget

```python
select_team = SelectTeam(
    default_id=team_id,
)
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card = Card(
    title="Select Team",
    content=Container(widgets=[select_team]),
)

layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```
