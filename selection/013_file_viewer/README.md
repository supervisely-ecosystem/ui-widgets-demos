# File Viewer

## Introduction

**`FileViewer`** widget in Supervisely is a useful tool for inspecting and easily navigating through files in specific directory in Team files.

[Read this tutorial in developer portal.](https://developer.supervisely.com/app-development/widgets/selection/fileviewer)

## Function signature

```python
FileViewer(
    files_list=files_list,
    selection_type=None,
    extended_selection=False,
    widget_id=None,
)
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/120389559/222391341-f8857a83-dffb-484e-859b-30794d0368f1.gif" alt="default" />
</p>

## Parameters

|      Parameters      |               Type                |                                                            Description                                                             |
| :------------------: | :-------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------: |
|     `files_list`     |           `List[dict]`            |                                             List of dicts with files and folders info                                              |
|   `selection_type`   | `Literal[None, "file", "folder"]` |                                                       Type of data to select                                                       |
| `extended_selection` |              `bool`               | If True method `get_selected_items()` returns an array of objects { path: '', type: 'file or folder' } instead of array with paths |
|     `widget_id`      |               `str`               |                                                          ID of the widget                                                          |

### files_list

List of files and folders info in `dict` format. See method `api.file.list()` for more information [here](https://supervisely.readthedocs.io/en/latest/sdk/supervisely.api.file_api.FileApi.html#supervisely.api.file_api.FileApi.list).

**type:** `List[dict]`

```python
files = api.file.list(team_id, path)
tree_items = []
for file in files:
    path = file["path"]
    tree_items.append({"path": path})


file_viewer = FileViewer(files_list=tree_items)
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/120389559/222391341-f8857a83-dffb-484e-859b-30794d0368f1.gif" alt="default" />
</p>

### selection_type

Type of data to select. If set to `'file'` - only files can be selected, if set to `'folder'` - only folders can be selected. If set to `None` - both files and folders can be selected.

**type:** `Literal[None, "file", "folder"]`

**default value:** `None`

```python
file_viewer = FileViewer(
    files_list=tree_items,
    selection_type="file",
)
```

### extended_selection

If `True` method `get_selected_items()` returns a `list` of `dict`s: `{path: '', type: 'file or folder'}`, instead of `list` with paths.

**type:** `bool`

**default value:** `False`

```python
file_viewer = FileViewer(
    files_list=tree_items,
    extended_selection=True,
)
```

### widget_id

ID of the widget.

**type:** `str`

**default value:** `None`

## Methods and attributes

|           Attributes and Methods           | Description                                             |
| :----------------------------------------: | ------------------------------------------------------- |
|                 `loading`                  | Get or set `loading` property.                          |
|           `get_selected_items()`           | Return selected items.                                  |
|            `get_current_path()`            | Return current path to files.                           |
| `update_file_tree(files_list: List[dict])` | Update files tree by given files list.                  |
|              `@path_changed`               | Decorator function is handled then input path changed.  |
|              `@value_changed`              | Decorator function is handled then input value changed. |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/selection/013_file_viewer/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/selection/013_file_viewer/src/main.py)

### Import libraries

```python
import os
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import FileViewer, Container, Card, Text
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Get Team ID from environment variables

```python
team_id = sly.env.team_id()
```

### Prepare file pathes

```python
path = "/"  # root of Team Files or specify your directory

files = api.file.list(team_id, path)
tree_items = []
for file in files:
    path = file["path"]
    tree_items.append({"path": path, "size": file["meta"]["size"]})
```

### Initialize `FileViewer` widget

```python
file_viewer = FileViewer(files_list=tree_items)
```

### Create `Text` widgets we will use

```python
selected_values = Text()
curr_path = Text()
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
layout = Card(
    content=Container(widgets=[curr_path, selected_values, file_viewer]),
    title="File Viewer",
)
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```

### Add function to control widgets from python code

```python
@file_viewer.path_changed
def refresh_tree(current_path):
    curr_path.set(
        text=f"Current path: {current_path}",
        status="text",
    )


@file_viewer.value_changed
def print_selected(selected_items):
    selected_values.set(
        text=f"Selected items: {', '.join(selected_items)}",
        status="text",
    )
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/120389559/222407891-9b5965c0-e99b-4f30-8ed7-b97d954cb422.gif" alt="layout" />
</p>
