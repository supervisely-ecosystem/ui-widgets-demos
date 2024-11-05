# Project Selector

## Introduction

**`ProjectSelector`** widget in Supervisely is a dropdown menu that allows users to select a team, workspace, project and datasets from a list of available items.
Clicking on it can be processed from python code. This widget is particularly useful when working with multiple teams, workspaces, projects or datasets in Supervisely and allows to easily select items in applications. It can be customized by disabling team or dataset selection.
Overall, the ProjectSelector widget is a valuable tool for improving the efficiency and usability of Supervisely apps. 

[Read this tutorial in developer portal.](https://developer.supervisely.com/app-development/widgets/selection/projectselector)

## Function signature

```python
ProjectSelector(
    team_id=None,
    workspace_id=None,
    project_id=None,
    team_is_selectable=True,
    datasets_is_selectable=True,
    widget_id=None,
)
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/120389559/221404961-9a9bc6a8-feae-4295-b0a2-5d70c295341e.gif" alt="default" />
</p>

## Parameters

|        Parameters        |  Type  |        Description        |
| :----------------------: | :----: | :-----------------------: |
|        `team_id`         | `int`  |          Team ID          |
|      `workspace_id`      | `int`  |       Workspace ID        |
|       `project_id`       | `int`  |        Project ID         |
|   `team_is_selectable`   | `bool` |   Enable Team selection   |
| `datasets_is_selectable` | `bool` | Enable Datasets selection |
|       `widget_id`        | `str`  |     ID of the widget      |

### team_id

Determine `Team` ID.

**type:** `int`

**default value:** `None`

```python
team_id = sly.env.team_id()
project_selector = ProjectSelector(team_id=team_id)
```

![team_id](https://user-images.githubusercontent.com/120389559/221402069-74b16fff-0774-49fc-a793-9096c94243d9.gif)

### workspace_id

Determine `Workspace` ID.

**type:** `int`

**default value:** `None`

```python
workspace_id = sly.env.workspace_id()
project_selector = ProjectSelector(workspace_id=workspace_id)
```

![workspace_id](https://user-images.githubusercontent.com/120389559/221405175-40fd0a4c-0239-4a9d-abb1-7aa07d5bc0a4.png)

### project_id

Determine `Project` ID.

**type:** `int`

**default value:** `None`

```python
workspace_id = sly.env.workspace_id()
project_id = sly.env.project_id()
project_selector = ProjectSelector(
    workspace_id=workspace_id,
    project_id=project_id,
)
```

![project_id](https://user-images.githubusercontent.com/120389559/221405281-80300e90-db52-4879-935b-d4cb1ba04d7c.png)

### team_is_selectable

Determine ability to select `Team`.

**type:** `bool`

**default value:** `True`

```python
team_id = sly.env.team_id()
project_selector = ProjectSelector(
    team_id=team_id,
    team_is_selectable=False,
)
```

![team_is_selectable](https://user-images.githubusercontent.com/120389559/221405405-8cefe66c-1526-4289-936d-637314b39cec.png)

### datasets_is_selectable

Determine ability to select `Datasets`.

**type:** `bool`

**default value:** `True`

```python
team_id = sly.env.team_id()
project_selector = ProjectSelector(
    team_id=team_id,
    datasets_is_selectable=False,
)
```

![datasets_is_selectable](https://user-images.githubusercontent.com/120389559/221405467-d014d7c8-0dc9-4eeb-81e0-dd646e98bd5f.png)

### widget_id

ID of the widget.

**type:** `str`

**default value:** `None`

## Methods and attributes

|          Attributes and Methods          | Description                                     |
| :--------------------------------------: | ----------------------------------------------- |
|   `get_selected_team_id(state: dict)`    | Return selected `Team` ID.                      |
| `get_selected_workspace_id(state: dict)` | Return selected `Workspace` ID.                 |
|  `get_selected_project_id(state: dict)`  | Return selected `Project` ID.                   |
|   `get_selected_datasets(state: dict)`   | Return list of selected `Dataset` IDs.          |
|         `disabled(value: bool)`          | Set widget `disabled` attribute to given value. |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/legacy/001_project_selector/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/legacy/001_project_selector/src/main.py)

### Import libraries

```python
import os
import supervisely as sly
from supervisely.app.widgets import Card, Container, ProjectSelector
from dotenv import load_dotenv
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Prepare `team_id`, `workspace_id`, `project_id` we will use

```python
team_id = sly.env.team_id()
workspace_id = sly.env.workspace_id()
project_id = sly.env.project_id()
```

### Initialize `ProjectSelector` widget

```python
project_selector = ProjectSelector(
    team_id=team_id,
    workspace_id=workspace_id,
    project_id=project_id,
)
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card = Card(
    title="Project Selector",
    content=project_selector,
)
layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/120389559/221405858-cf9abe31-118b-4e67-a424-d8f5e012bf5f.gif" alt="layout" />
</p>
