# Agent Selector

## Introduction

**`AgentSelector`** widget in Supervisely is a dropdown menu that allows users to select an agent from a list of available agents in within a given team. Clicking on it can be processed from python code. This widget is particularly useful when you are developing an app that can be able to launch another apps or deploy models.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/widgets/selection/agentselector)

## Function signature

```python
AgentSelector(
    team_id=team_id,
    any_status=False,
    show_public=False,
    has_gpu=False,
    only_running=False,
    compact=False,
    widget_id=None
)
```

![default](https://github.com/supervisely-ecosystem/ui-widgets-demos/assets/48913536/dd5bfcdb-c3bf-4f92-b18e-3677953bb2ac)

## Parameters

|   Parameters   |  Type  |                  Description                   |
| :------------: | :----: | :--------------------------------------------: |
|   `team_id`    | `int`  |      Team ID to list agents from the team      |
|  `any_status`  | `bool` |        Show all agents with any status         |
| `show_public`  | `bool` |               Show shared agents               |
|   `has_gpu`    | `bool` |              Show only GPU agents              |
| `only_running` | `bool` | Show agents only with "Running" network status |
|   `compact`    | `bool` |       If `True` selector will be compact       |
|  `widget_id`   | `str`  |                ID of the widget                |

### team_id

Team ID to list agents from the team. This parameter is required.

**type:** `int`

```python
agent_selector = AgentSelector(team_id=team_id)
```

### any_status

Show all agents with any status. If `False` only agents with "Running" status will be shown.

**type:** `bool`

**default value:** `False`

```python
agent_selector = AgentSelector(
    team_id=team_id,
    any_status=True,
)
```

### show_public

Show shared agents. If `False` shared agents will not be shown.

**type:** `bool`

**default value:** `False`

```python
agent_selector = AgentSelector(
    team_id=team_id,
    show_public=True,
)
```

![show-public](https://github.com/supervisely-ecosystem/ui-widgets-demos/assets/48913536/967740bf-b743-4429-8f0d-30c19593dff2)

### has_gpu

Show only agents with GPU.

**type:** `bool`

**default value:** `False`

```python
agent_selector = AgentSelector(
    team_id=team_id,
    has_gpu=True,
)
```

![needGPU](https://github.com/supervisely-ecosystem/ui-widgets-demos/assets/48913536/d83815df-a8e6-4577-9d42-443bdfdd14c9)

### only_running

Show agents only with "Running" network status. If `False` agents with any status will be shown.

**type:** `bool`

**default value:** `False`

```python
agent_selector = AgentSelector(
    team_id=team_id,
    only_running=True,
)
```

### compact

If `True` selector will be compact.

**type:** `bool`

**default value:** `False`

```python
agent_selector = AgentSelector(
    team_id=team_id,
    compact=True,
)
```

![compact](https://github.com/supervisely-ecosystem/ui-widgets-demos/assets/48913536/b7bf6219-f882-4907-b552-6784f6a69a37)

### widget_id

ID of the widget.

**type:** `str`

**default value:** `None`

## Methods and attributes

| Attributes and Methods | Description                                                |
| :--------------------: | ---------------------------------------------------------- |
|     `get_value()`      | Return selected agent id.                                  |
|    `@value_changed`    | Decorator function is handled when input value is changed. |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/selection/020_agent_selector/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/selection/020_agent_selector/src/main.py)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, AgentSelector, Text, Container
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Prepare `team_id`

```python
team_id = sly.env.team_id()
```

### Initialize `AgentSelector` widget

```python
agent_selector = AgentSelector(
    team_id=team_id,
    any_status=False,
    show_public=False,
    has_gpu=False,
    only_running=False,
    compact=False,
)
```

### Create preview widgets

Create a widget that will display the selected agent id.

```python
agent_id_preview = Text("", "text")
agent_name_preview = Text("", "text")
agent_preview_container = Container([agent_id_preview, agent_name_preview])
agent_preview_container.hide()
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
container = Container([agent_selector, agent_preview_container])
layout = Card(title="AgentSelector", content=container)
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```

![miniapp](https://github.com/supervisely-ecosystem/ui-widgets-demos/assets/48913536/da4d6c8d-bc64-41e5-b80f-3e9c8ecdb235)
