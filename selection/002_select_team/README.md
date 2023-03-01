# Select Team

## Introduction

This widget is a select team input, clicking on it can be processed from python code. In this tutorial you will learn how to use **`SelectTeam`** widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/widgets/selection/selectworkspace)

## Function signature

```python
SelectTeam(
    default_id=None,
    show_label=True,
    size=None,
    widget_id=None,
)
```

![default](https://user-images.githubusercontent.com/120389559/218033566-7b4babed-9dfd-4bc6-ba14-19666afb2e1d.png)

## Parameters

|  Parameters  |                   Type                    |           Description            |
| :----------: | :---------------------------------------: | :------------------------------: |
| `default_id` |                   `int`                   |   Default supervisely team ID    |
| `show_label` |                  `bool`                   |            Show label            |
|    `size`    | `Literal["large", "small", "mini", None]` | Selector size (large/small/mini) |
| `widget_id`  |                   `str`                   |         ID of the widget         |

### default_id

Determine `Team` will be selected by default.

**type:** `int`

**default value:** `None`

```python
select_team = SelectTeam(default_id=team_id)
```

![default_id](https://user-images.githubusercontent.com/120389559/218033755-a0449ce0-141e-4769-b11a-311bd2be7dfb.png)

### show_label

Determine show text `Team` on widget or not.

**type:** `bool`

**default value:** `True`

```python
select_team = SelectTeam(default_id=team_id, show_label=False)
```

![show_label](https://user-images.githubusercontent.com/120389559/218034036-b9a1bd07-62f4-4787-a8f9-847d94ee3cf0.png)

### size

Size of input.

**type:** `Literal["large", "small", "mini", None]`

**default value:** `None`

```python
select_team = SelectTeam(default_id=team_id, show_label=False)
select_mini = SelectTeam(default_id=team_id, show_label=False, size="mini")
select_small = SelectTeam(default_id=team_id, show_label=False, size="small")
select_large = SelectTeam(default_id=team_id, show_label=False, size="large")
card = Card(
    title="Select Team",
    content=Container(widgets=[select_team, select_mini, select_small, select_large]),
)
```

![size](https://user-images.githubusercontent.com/120389559/218723907-e80e8122-f1be-493e-afb2-5bdce23725c2.png)

### widget_id

ID of the widget.

**type:** `str`

**default value:** `None`

## Methods and attributes

| Attributes and Methods | Description              |
| :--------------------: | ------------------------ |
|  `get_selected_id()`   | Return selected team id. |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/013_select_team/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/013_select_team/src/main.py)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, NotificationBox, SelectTeam
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Prepare `Team` ID

```python
team_id = sly.env.team_id()
```

### Initialize `SelectTeam` widget

```python
select_team = SelectTeam()
```

### Create button and notification box we will use in UI for demo

```python
ok_btn = Button("OK")

notification_box = NotificationBox()
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card = Card(
    title="Select Team",
    content=Container(widgets=[select_team, ok_btn, notification_box]),
)

layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```

### Add functions to get `team ID` from widget

```python
@ok_btn.click
def show_team_members():
    team_id = select_team.get_selected_id()
    team = api.team.get_info_by_id(team_id)
    notification_box.set(
        title=f"Team '{team.name}'",
        description=f"Your role in the team: {team.role}",
    )
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/79905215/222133799-90b573a4-d1fa-4c8e-a337-9665cd8ae458.gif" alt="select-team-app" width="600"/>
</p>
