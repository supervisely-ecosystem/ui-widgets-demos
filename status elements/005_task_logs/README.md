# Task Logs

## Introduction

The **`TaskLogs`** widget in Supervisely is designed to display task logs for a given task ID.

> ℹ️ This widget will display logs passed by the session ID **only in production**. In development mode, the message _"You are currently in development mode. Task logs will be displayed only in production mode."_ will be displayed.

[Read this tutorial in the developer portal.](https://developer.supervise.ly/app-development/widgets/status-elements/tasklogs)

## Function signature

```python
TaskLogs(task_id=None, multiple=False, filterable=True, widget_id=None)
```

![default](https://github.com/supervisely-ecosystem/ui-widgets-demos/assets/79905215/76cb5208-bcb1-42b2-bbf5-033fb8b63d7c)

## Parameters

| Parameters  | Type  |           Description           |
| :---------: | :---: | :-----------------------------: |
|  `task_id`  | `int` | The task ID to display logs for |
| `widget_id` | `str` |        ID of the widget         |

### url

The task ID to display logs for.

**type:** `str`

**default value:** `None`

### widget_id

ID of the widget.

**type:** `str`

**default value:** `None`

## Methods and attributes

|   Attributes and Methods    | Description      |
| :-------------------------: | ---------------- |
|       `get_task_id()`       | Get the task ID. |
| `set_task_id(task_id: int)` | Set the task ID. |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/status-elements/005_task_logs/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/status-elements/005_task_logs/src/main.py)

### Import libraries

```python
import supervisely as sly
from supervisely.app.widgets import Card, Container, TaskLogs
```

> ℹ️ This widget will display logs passed by the session ID **only in production**. In development mode, the message _"You are currently in development mode. Task logs will be displayed only in production mode."_ will be displayed.

### Initialize `TaskLogs` widgets we will use in UI

```python
task_id = 36925

logs = TaskLogs()
logs.set_task_id(task_id)
```

or

```python
logs = TaskLogs(task_id)

```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card = Card(title="Logs", content=logs)
layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with `layout` parameter.

```python
app = sly.Application(layout=layout)
```

<p align="center">
    <video preload="none" playsinline="" autoplay="autoplay" muted="muted" loop="loop" width="1200">
        <source src=https://github.com/supervisely-ecosystem/ui-widgets-demos/assets/79905215/a59bde9e-4120-43e9-9219-5cb4d5d03843" type="video/webm"> 
        <source src="https://github.com/supervisely-ecosystem/ui-widgets-demos/assets/79905215/4ece99d2-89b9-44b9-8f32-5a05ff918417" type="video/mp4">
    </video>
</p>
