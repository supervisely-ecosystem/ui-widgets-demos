# Pagination

## Introduction

**`Pagination`** is a widget in Supervisely that allows to use pagination on the UI.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/widgets/charts-and-plots/pagination)

## Function signature

```python
Pagination(
    total,
    layout="prev, pager, next, jumper, ->, total",
    current_page=1,
    small=False,
    page_size=10,
    page_sizes=[10, 20, 30, 40, 50, 100],
    widget_id=None,
)
```

```python
pagination = Pagination(total=50)
```

![pagination_default](https://user-images.githubusercontent.com/120389559/227777410-1953c671-fd43-4778-903a-2c5de639325a.gif)

## Parameters

|   Parameters   |    Type     |                       Description                       |
| :------------: | :---------: | :-----------------------------------------------------: |
|    `total`     |    `int`    |              Total `Pagination` item count              |
|    `layout`    |    `str`    | Layout of `Pagination`, elements separated with a comma |
| `current_page` |    `int`    |                   Current page number                   |
|    `small`     |   `bool`    |             Whether to use small pagination             |
|  `page_size`   |    `int`    |                 Item count of each page                 |
|  `page_sizes`  | `List[int]` |             Options of item count per page              |
|  `widget_id`   |    `str`    |                    ID of the widget                     |

### total

Determine total `Pagination` item count.

**type:** `int`

### layout

Determine layout of `Pagination`, elements separated with a comma. Possible values: `sizes, prev, pager, next, jumper, ->, total, slot`.

**type:** `str`

**default value:** `"prev, pager, next, jumper, ->, total"`

```python
pagination = Pagination(total=50, layout="sizes, prev, pager, next, jumper, ->, total, slot")
```

![layout](https://user-images.githubusercontent.com/120389559/227777864-2368f10d-524f-4a18-8e21-63c4f52bb4cf.png)

### current_page

Determine current page number.

**type:** `int`

**default value:** `1`

```python
pagination = Pagination(total=50, current_page=3)
```

![current_page](https://user-images.githubusercontent.com/120389559/227777949-fdb7ebf3-1e90-44ca-b4ef-8e1a00f60b03.png)

### small

Determine whether to use small pagination.

**type:** `bool`

**default value:** `False`

```python
pagination = Pagination(total=50, small=True)
```

![small](https://user-images.githubusercontent.com/120389559/227778032-3bc9c752-34d9-450d-814b-8b46c55cf214.png)

### page_size

Determine item count of each page.

**type:** `int`

**default value:** `10`

```python
pagination = Pagination(total=50, page_size=5)
```

![page_size](https://user-images.githubusercontent.com/120389559/227778169-ca2179f7-7e84-4b82-ade5-45f790ec1adc.png)

### page_sizes

Determine options of item count per page.

**type:** `List[int]`

**default value:** `[10, 20, 30, 40, 50, 100]`

```python
pagination = Pagination(total=1000, page_sizes=[10, 20, 50], layout="prev, pager, next, sizes")
```

![page_sizes](https://user-images.githubusercontent.com/120389559/227778326-43b6ac36-9024-4646-8010-551617a4027a.gif)

## Methods and attributes

|       Attributes and Methods       | Description                                         |
| :--------------------------------: | --------------------------------------------------- |
|        `get_current_page()`        | Return `Pagination` current page.                   |
|         `get_page_size()`          | Set `Pagination` current page.                      |
|    `set_page_size(value: int)`     | Return `Pagination` page size.                      |
|   `set_current_size(value: int)`   | Set `Pagination` page size.                         |
|           `get_layout()`           | Return `Pagination` layout.                         |
|      `set_layout(value: str)`      | Set `Pagination` layout.                            |
|           `get_total()`            | Return `Pagination` total items count.              |
|      `set_total(value: int)`       | Set `Pagination` total items count.                 |
|    `unable_small_pagination()`     | Set `Pagination` `small` mode.                      |
|    `disable_small_pagination()`    | Disable `Pagination` `small` mode.                  |
|         `get_page_sizes()`         | Return `Pagination` page sizes data.                |
| `set_page_sizes(value: List[int])` | Set `Pagination` page sizes data.                   |
|         `@current_change`          | Decorator function to handle `current-page` change. |
|           `@size_change`           | Decorator function to handle `page-size` change.    |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/misc/pagination/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/misc/pagination/src/main.py)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Pagination, Text
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Initialize `Pagination` and `Text` widgets

```python
pagination = Pagination(
    total=1000, page_size=20, page_sizes=[10, 20, 50], layout="prev, pager, next, sizes, total"
)

text_page = Text()
text_size = Text()
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter.

```python
card = Card(
    "Pagination",
    content=Container([pagination, text_page, text_size]),
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
@pagination.current_change
def page_change(res):
    info = f"Current page number: {res}"
    text_page.set(text=info, status="info")


@pagination.size_change
def page_size_change(res):
    info = f"Current page size: {res}"
    text_size.set(text=info, status="success")
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/120389559/227779108-bbb467d3-2706-45ef-8d8e-db92359eadd7.gif" alt="layout" />
</p>
