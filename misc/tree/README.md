# Tree

## Introduction

**`Tree`** is a widget in Supervisely that allows choise items on the UI by tree structure.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/widgets/charts-and-plots/tree)

## Function signature

```python
Tree(
    data=[],
    label="label",
    children="children",
    disabled="disabled",
    node_key="id",
    show_checkbox=False,
    current_node_key=None,
    empty_text="Input data is void",
    accordion=False,
    widget_id=None,
)
```

Example of input data we will use.

```python
data = [
    {
        "id": 1,
        "label": "Level one 1",
        "children": [
            {
                "id": 4,
                "label": "Level two 1-1",
                "children": [
                    {"id": 9, "label": "Level three 1-1-1"},
                    {"id": 10, "label": "Level three 1-1-2"},
                ],
            }
        ],
    },
    {
        "id": 2,
        "label": "Level one 2",
        "children": [{"id": 5, "label": "Level two 2-1"}, {"id": 6, "label": "Level two 2-2"}],
    },
    {
        "id": 3,
        "label": "Level one 3",
        "children": [{"id": 7, "label": "Level two 3-1"}, {"id": 8, "label": "Level two 3-2"}],
    },
]


tree = Tree(data=data)
```

![tree_default](https://user-images.githubusercontent.com/120389559/226618896-1cbcd3c9-7070-4bb5-8cfa-e23b0c9ff930.gif)

## Parameters

|     Parameters     |            Type            |                                     Description                                      |
| :----------------: | :------------------------: | :----------------------------------------------------------------------------------: |
|       `data`       |        `List[Dict]`        |                                     `Tree` data                                      |
|      `label`       |           `str`            |             Specify which key of node object is used as the node's label             |
|     `children`     |           `str`            |               Specify which node object is used as the node's subtree                |
|     `disabled`     |           `str`            |      Specify which key of node object represents if node's checkbox is disabled      |
|     `node_key`     |           `str`            | Unique identity key name for nodes, its value should be unique across the whole tree |
|  `show_checkbox`   |           `bool`           |                              Whether node is selectable                              |
| `current_node_key` | `Optional[str, int, None]` |                                 Key of current node                                  |
|    `empty_text`    |           `str`            |                           Text displayed when data is void                           |
|    `accordion`     |           `bool`           |        Whether only one node among the same level can be expanded at one time        |
|    `widget_id`     |           `str`            |                                   ID of the widget                                   |

### data

Determine `Tree` data.

**type:** `List[Dict]`

**default value:** `[]`

### label

Specify which key of node object is used as the node's label.

**type:** `str`

**default value:** `"label"`

### children

Specify which node object is used as the node's subtree.

**type:** `str`

**default value:** `"children"`

### disabled

Specify which key of node object represents if node's checkbox is disabled.

**type:** `str`

**default value:** `"disabled"`

### node_key

Unique identity key name for nodes, its value should be unique across the whole tree.

**type:** `str`

**default value:** `"id"`

### show_checkbox

Determine whether node is selectable.

**type:** `bool`

**default value:** `False`

```python
tree = Tree(data=data, show_checkbox=True)
```

![show_checkbox](https://user-images.githubusercontent.com/120389559/226622217-cf287d2a-ee63-442b-84d7-b6e065180e45.gif)

### current_node_key

Determine key of current node.

**type:** `Optional[str, int, None]`

**default value:** `None`

### empty_text

Determine text displayed when data is void.

**type:** `str`

**default value:** `"Input data is void"`

```python
tree = Tree()
```

![empty_text](https://user-images.githubusercontent.com/120389559/226623761-8809a03e-c62d-47e6-bf64-ebb9bc1f6736.png)

### accordion

Determine whether only one node among the same level can be expanded at one time.

**type:** `bool`

**default value:** `False`

```python
time_picker = TimePicker(readonly=True)
```

![accordion](https://user-images.githubusercontent.com/120389559/226624472-631d4dfa-a7fa-4bf6-8d85-4ac8a9b87e60.gif)

## Methods and attributes

|    Attributes and Methods     | Description                                         |
| :---------------------------: | --------------------------------------------------- |
|     `get_current_node()`      | Return `Tree` current clicked node data.            |
|     `get_current_check()`     | Return `Tree` current clicked checkbox data.        |
|         `get_data()`          | Return `Tree` data.                                 |
| `set_data(value: List[Dict])` | Set `Tree` data.                                    |
| `add_data(value: List[Dict])` | Add `Tree` data to exist now.                       |
|    `set_label(value: str)`    | Set `Tree` label key name.                          |
|  `set_children(value: str)`   | Set `Tree` children key name.                       |
|      `unable_checkbox()`      | Set `show_checkbox` to `True`.                      |
|     `disable_checkbox()`      | Set `show_checkbox` to `False`.                     |
|         `@node_click`         | Decorator function to handle `Tree` node click.     |
|        `@check_change`        | Decorator function to handle `Tree` checkbox click. |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/misc/tree/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/misc/tree/src/main.py)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Text, Tree
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Initialize `Tree` and `Text` widgets

```python
data = [
    {
        "id": 1,
        "label": "Level one 1",
        "children": [
            {
                "id": 4,
                "label": "Level two 1-1",
                "children": [
                    {"id": 9, "label": "Level three 1-1-1"},
                    {"id": 10, "label": "Level three 1-1-2"},
                ],
            }
        ],
    },
    {
        "id": 2,
        "label": "Level one 2",
        "children": [{"id": 5, "label": "Level two 2-1"}, {"id": 6, "label": "Level two 2-2"}],
    },
    {
        "id": 3,
        "label": "Level one 3",
        "children": [{"id": 7, "label": "Level two 3-1"}, {"id": 8, "label": "Level two 3-2"}],
    },
]

tree = Tree(data=data, show_checkbox=True)

text = Text()
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter.

```python
card = Card(
    "Tree",
    content=Container([tree, text]),
)


layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=card)
```

### Add functions to control widgets from python code

```python
@tree.node_click
def show_time(res):
    info = f"Current node id={res['id']}, label text: {res['label']}"
    text.set(text=info, status="info")


@tree.check_change
def show_time(res):
    info = f"Current checkbox id={res['id']}"
    text.set(text=info, status="info")

```

<p align="center">
  <img src="https://user-images.githubusercontent.com/120389559/226628385-74c9d469-403b-40c6-8ad3-60c6feacc6cc.gif" alt="layout" />
</p>
