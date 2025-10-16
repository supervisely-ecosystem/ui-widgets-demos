# EcosystemModelSelector

## Introduction

The **`EcosystemModelSelector`** widget in Supervisely is a user interface element that enables users to browse and select from available ecosystem models. It displays models in a filterable table format with information about framework, task type, parameters, and metrics. The widget includes dropdown filters for frameworks and task types, allowing users to quickly find the models they need. Additionally, it includes event handlers that activate when a user selects a model from the table.

## Function signature

```python
EcosystemModelSelector(
    frameworks = None,
    task_types = None,
    models = None,
    api = None,
    widget_id = None,
)
```

![default](https://github.com/user-attachments/assets/4a971741-3cc8-4844-b116-6abd40c751e2)

## Parameters

| Parameters   |          Type          |                                        Description                                         |
| :----------- | :--------------------: | :----------------------------------------------------------------------------------------: |
| `frameworks` | `Optional[List[str]]`  | List of frameworks to filter by. If None, all frameworks will be shown. Default is `None`. |
| `task_types` | `Optional[List[str]]`  | List of task types to filter by. If None, all task types will be shown. Default is `None`. |
| `models`     | `Optional[List[Dict]]` |  List of models to display. If None, models will be fetched from API. Default is `None`.   |
| `api`        |    `Optional[Api]`     |   Supervisely API instance. If None, a new instance will be created. Default is `None`.    |
| `widget_id`  |         `str`          |                               An optional ID for the widget.                               |

### frameworks

Filter models by specific frameworks.
If provided, only models from the specified frameworks will be displayed initially.

**type:** `Optional[List[str]]`

**default value:** `None`

Show only PyTorch and TensorFlow models:

```python
widget = EcosystemModelSelector(frameworks=["pytorch", "tensorflow"])
```

### task_types

Filter models by specific task types.
If provided, only models from the specified task types will be displayed initially.

**type:** `Optional[List[str]]`

**default value:** `None`

Show only object detection models:

```python
widget = EcosystemModelSelector(task_types=["object detection"])
```

### models

Provide a custom list of models to display.
If not provided, models will be fetched from the Supervisely ecosystem API.

**type:** `Optional[List[Dict]]`

**default value:** `None`

Use custom model list:

```python
custom_models = [
    {
        "name": "YOLOv8n",
        "framework": "pytorch",
        "task": "object detection",
        "paramsM": 3.2,
        "evaluation": {"metrics": {"mAP": 37.3}}
    }
]
widget = EcosystemModelSelector(models=custom_models)
```

### api

Supervisely API instance for fetching models.
If not provided, a new API instance will be created.

**type:** `Optional[Api]`

**default value:** `None`

### widget_id

An optional ID for the widget.

**type:** `str`

**default value:** `None`

Initialize the widget with an ID:

```python
widget = EcosystemModelSelector(widget_id="ecosystem_model_selector")
```

## Methods and attributes

|                       Methods and Attributes                       |                    Description                     |
| :----------------------------------------------------------------: | :------------------------------------------------: |
|                          `get_selected()`                          |           Get currently selected model.            |
|                        `select(index: int)`                        |         Select a model by its table index.         |
| `select_framework_and_model_name(framework: str, model_name: str)` |       Select a model by framework and name.        |
|                         `refresh_table()`                          | Refresh the table with current models and filters. |
|               `set(frameworks, task_types, models)`                |   Update the widget with new filters and models.   |

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Text
from ecosystem_model_selector import EcosystemModelSelector
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))
api = sly.Api()
```

### Initialize the `EcosystemModelSelector` widget

Let's initialize the `EcosystemModelSelector` widget:

```python
model_selector = EcosystemModelSelector(api=api)
```

### Create an event handler for the `EcosystemModelSelector` widget

Now, let's create an event handler for the EcosystemModelSelector widget, when a model is selected from the table.

```python
selection_changed_info = Text(status="info")
selection_changed_info.hide()


@model_selector.table.value_changed
def model_selected(selected_row):
    if selected_row:
        try:
            selected_model = model_selector.get_selected()
            text = f"Selected model: {selected_model['name']} ({selected_model['framework']})"
            selection_changed_info.text = text
            selection_changed_info.show()
        except Exception as e:
            selection_changed_info.text = f"Error getting selected model: {str(e)}"
            selection_changed_info.show()
    else:
        selection_changed_info.hide()
```

### Create app layout

Prepare a layout for the app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card = Card(
    title="EcosystemModelSelector",
    content=Container(widgets=[selection_changed_info, model_selector]),
)

layout = Container(widgets=[card])
```

### Create an app using the layout

Create an app object with the layout parameter.

```python
app = sly.Application(layout=layout)
```
