# One of

## Introduction

This widget allows to display an element corresponding to selected item in a conditional type widget (e. g. `Select`, `RadioButton`, `Switch`). Clicking on it can be processed from python code. In this tutorial you will learn how to use **`OneOf`** widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/OneOf)

## Function signature

```python
one_of = OneOf(conditional_widget=Select(items=animals))
```

![default](https://user-images.githubusercontent.com/79905215/217235567-e6b0c581-8cac-4a36-9286-58ea331db051.png)

## Parameters

|     Parameters     |       Type        |                             Description                             |
| :----------------: | :---------------: | :-----------------------------------------------------------------: |
| conditional_widget | ConditionalWidget | conditional widget with preset items (e.g. `Select`, `RadioButton`, `Switch`) |
|     widget_id      |        str        |                          id of the widget                           |

### conditional_widget

Conditional widget with preset items.

**type:** `ConditionalWidget`

```python
one_of = OneOf(conditional_widget=Select(items=animals))
```

### widget_id

ID of the widget.

**type:** `int`

**default value:** `None`

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/017_one_of/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/017_one_of/src/main.py)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, OneOf, Select, Image
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Prepare conditional widget content

You can use `RadioGroup`, `Select` or `Switch` widgets to set in `conditional_widget` property.
In this tutorial we will use `Select` widget. 

Prepare images we will use in `Select.Items`

```python
cat_image = Image(
    url="https://user-images.githubusercontent.com/120389559/209821564-7917cbe5-fa8e-49dd-a1ca-519ee2b3a7ca.jpg"
)
dog_image = Image(
    url="https://user-images.githubusercontent.com/120389559/209821597-8670675b-5a18-480c-8fdc-1309e91086c7.jpg"
)
horse_image = Image(
    url="https://user-images.githubusercontent.com/120389559/209821602-ddb8196f-0ac5-4556-abae-178327ff734b.jpg"
)
sheep_image = Image(
    url="https://user-images.githubusercontent.com/120389559/209821609-c8396b3e-d7a3-4beb-b92b-539d31e91e90.jpg"
)
```

Prepare items for `Select` widget using `Select.Item`. [Learn more](https://github.com/supervisely-ecosystem/ui-widgets-demos/tree/master/009_select)

```python
animals = [
    Select.Item(value="cat", label="cat", content=cat_image),
    Select.Item(value="dog", label="dog", content=dog_image),
    Select.Item(value="horse", label="horse", content=horse_image),
    Select.Item(value="sheep", label="sheep", content=sheep_image),
]
```

Create `Select` widget.

```python
select_items = Select(items=animals)
```


### Initialize `OneOf` widget

```python
one_of = OneOf(conditional_widget=select_items)
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card = Card(
    title="One of",
    content=one_of,
)

layout = Container(widgets=[select_items, card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```
