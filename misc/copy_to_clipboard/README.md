# CopyToClipboard

## Introduction

In this tutorial you will learn how to use `CopyToClipboard` widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/сopyеoсlipboard)

## Function signature

```python
CopyToClipboard(content="", widget_id=None)
```

![default](https://user-images.githubusercontent.com/120389559/224316390-de355f21-bf5b-4dca-9619-43cc523562f9.png)

## Parameters

| Parameters  |                     Type                      |        Description        |
| :---------: | :-------------------------------------------: | :-----------------------: |
|  `content`  | `Optional[Editor or Text or TextArea or str]` | `CopyToClipboard` content |
| `widget_id` |                     `str`                     |     Id of the widget      |

### content

Determine input `CopyToClipboard` content.

**type:** `Optional[Editor or Text or TextArea or str]`

**default value:** `""`

```python
markdown = Markdown(md="Some content")
```

![md](https://user-images.githubusercontent.com/120389559/224316855-4dd7d72a-3818-44f5-bc74-7a83ac1a82ab.png)

### height

Determine `Widget` height.

**type:** `int`

**default value:** `300`

```python
markdown = Markdown(md="Some content", height=30)
```

![height](https://user-images.githubusercontent.com/120389559/224317474-e94ef7c0-39f2-42db-b7d6-5a105d84e11b.png)

### widget_id

ID of the widget.

**type:** `str`

**default value:** `None`

## Methods and attributes

| Attributes and Methods  | Description               |
| :---------------------: | ------------------------- |
| `set_value(value: str)` | Set `Markdown` data.      |
|      `get_value()`      | Return `Markdown` data.   |
|     `get_height()`      | Return `Markdown` height. |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/misc/markdown/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/misc/markdown/src/main.py)

### Import libraries

```python
import os, markdown

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Markdown, Button
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Initialize `Button` widgets, we will use

```python
button_readme = Button(text="Set md readme")
button_text = Button(text="Set md text")
button_clean = Button(text="Clean md")
buttons_container = Container(
    widgets=[button_readme, button_text, button_clean], direction="horizontal")
```

### Initialize `Markdown` widget

```python
md_path = os.path.join(os.getcwd(), "misc/markdown/README.md")
f = open(md_path, "r")
md = markdown.markdown(f.read())

markdown = Markdown(md=md)
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card = Card(title="Markdown", content=Container([markdown, buttons_container]))
layout = Container(widgets=[card], direction="vertical")
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```

### Handle button clicks

```python
@button_readme.click
def gmail_content():
    markdown.set_value(md)


@button_text.click
def google_content():
    markdown.set_value("some markdown text")


@button_clean.click
def clear():
    markdown.set_value("")
```

![layout](https://user-images.githubusercontent.com/120389559/224319059-a601a2a4-fc67-4551-bf22-df3b621f9260.gif)
