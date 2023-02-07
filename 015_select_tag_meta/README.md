# Select Tag Meta

## Introduction

This widget is a select `TagMeta` input, clicking on it can be processed from python code. In this tutorial you will learn how to use `SelectTagMeta` widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/SelectTagMeta)

## Function signature

```python
SelectTagMeta(default=None, project_id=None, project_meta=None, allowed_types=None, multiselect=False, show_label=True, size=None, widget_id=None)
```

![default](https://user-images.githubusercontent.com/79905215/216376305-1556627a-ef61-4df7-900c-ac2ffbb9c8d0.png)

## Parameters

|  Parameters   |               Type                |                                        Description                                        |
| :-----------: | :-------------------------------: | :---------------------------------------------------------------------------------------: |
|    default    |                str                |                                         Tag name                                          |
|  project_id   |                int                |                  Determine `Project` from which `Tags` will be selected.                  |
| project_meta  |            ProjectMeta            |                Determine `ProjectMeta` from which `Tags` will be selected                 |
| allowed_types |             List[str]             | Determine `Tags` types witch will be available to select from all the `Tags` in `Project` |
|  multiselect  |         List[ProjectType]         |                             Allows to select multiple `Tags`                              |
|  show_label   |               bool                |                                        Show label                                         |
|     size      | Literal["large", "small", "mini"] |                             Selector size (large/small/mini)                              |
|   widget_id   |                int                |                                     Id of the widget                                      |

### default

Determine `Tag` will be selected by default.

**type:** `str`

**default value:** `None`

```python
select_tag_meta = SelectTagMeta(default="cat", project_id=project_id)
```

![default](https://user-images.githubusercontent.com/79905215/216376305-1556627a-ef61-4df7-900c-ac2ffbb9c8d0.png)

### project_id

Determine `Project` from which `Tags` will be selected.

**type:** `int`

**default value:** `None`

```python
select_tag_meta = SelectTagMeta(project_id=project_id)
```

![project_id](https://user-images.githubusercontent.com/79905215/216376305-1556627a-ef61-4df7-900c-ac2ffbb9c8d0.png)

### project_meta

Determine `ProjectMeta` from which `Tags` will be selected.

**type:** `ProjectMeta`

**default value:** `None`

```python
# Get ProjectMeta
meta_json = api.project.get_meta(project_id)
project_meta = sly.ProjectMeta.from_json(meta_json)
# Create widget
select_tag_meta = SelectTagMeta(project_meta=project_meta)
```

![project_meta](https://user-images.githubusercontent.com/79905215/216376305-1556627a-ef61-4df7-900c-ac2ffbb9c8d0.png)

### allowed_types

Determine `Tags` types witch will be available to select from all the `Tags` in `Project`.

**type:** `List[str]`

**default value:** `None`

```python
from supervisely.annotation.tag_meta import TagValueType
allowed_types = [TagValueType.ANY_STRING, TagValueType.NONE]
select_tag_meta = SelectTagMeta(project_id=project_id, allowed_types=allowed_types)
```

![allowed_types](https://user-images.githubusercontent.com/79905215/216376305-1556627a-ef61-4df7-900c-ac2ffbb9c8d0.png)

### multiselect

Allows to select multiple `Tags`.

**type:** `bool`

**default value:** `False`

```python
select_tag_meta = SelectTagMeta(project_id=project_id, multiselect=True)
```

![multiselect](https://user-images.githubusercontent.com/79905215/216376305-1556627a-ef61-4df7-900c-ac2ffbb9c8d0.png)

### show_label

Determine show text `Tag` on widget or not.

**type:** `bool`

**default value:** `True`

```python
select_tag_meta = SelectTagMeta(project_id=project_id, show_label=False)
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

[supervisely-ecosystem/ui-widgets-demos/015_select_tag_meta/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/015_select_tag_meta/src/main.py)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, SelectTagMeta
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Prepare project_id

```python
project_id = int(os.environ["modal.state.slyProjectId"])
```

### Initialize `SelectTagMeta` widget

```python
select_tag_meta = SelectTagMeta(default="cat", project_id=project_id)
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card = Card(
    title="Select TagMeta",
    content=select_tag_meta,
)

layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```
