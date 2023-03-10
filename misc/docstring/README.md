# Docstring

## Introduction

In this tutorial you will learn how to use `Docstring` widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/docstring)

## Function signature

```python
Docstring(data="", widget_id=None)
```

![default](https://user-images.githubusercontent.com/120389559/224303776-85b03aec-bfdd-45e8-be9c-4cbc598fdfa0.png)

## Parameters

| Parameters  | Type  |   Description    |
| :---------: | :---: | :--------------: |
|   `data`    | `str` |  `HTML` content  |
| `widget_id` | `str` | Id of the widget |

### data

Determine input `HTML` content.

**type:** `str`

**default value:** `""`

```python
docstring = Docstring(data="Some content")
```

![data](https://user-images.githubusercontent.com/120389559/224304307-2e222fd3-0430-4b1b-abec-6e8996df64c5.png)

### widget_id

ID of the widget.

**type:** `str`

**default value:** `None`

## Methods and attributes

| Attributes and Methods  | Description              |
| :---------------------: | ------------------------ |
| `set_value(value: str)` | Set `Docstring` data.    |
|      `get_value()`      | Return `Docstring` data. |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/misc/docstring/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/misc/docstring/src/main.py)

### Import libraries

```python
import os, requests

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Docstring, Button
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
button_gmail_content = Button(text="Set gmail content")
button_google_content = Button(text="Set google content")
button_clean_content = Button(text="Clean content")
buttons_container = Container(
    widgets=[button_gmail_content, button_google_content, button_clean_content],
    direction="horizontal")
```

### Initialize `Docstring` widget

```python
url = "https://www.google.com/"
r = requests.get(url)
url_content = r.text

docstring = Docstring(data=url_content)
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card = Card(title="Docstring", content=Container([docstring, buttons_container]))
layout = Container(widgets=[card], direction="vertical")
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```

### Handle button clicks

```python
@button_gmail_content.click
def gmail_content():
    url = "https://www.gmail.com/"
    r = requests.get(url)
    url_content = r.text
    docstring.set_value(url_content)


@button_google_content.click
def google_content():
    url = "https://www.google.com/"
    r = requests.get(url)
    url_content = r.text
    docstring.set_value(url_content)


@button_clean_content.click
def clear():
    docstring.set_value("")
```

![layout](https://user-images.githubusercontent.com/120389559/224306026-114e4d01-ae4b-49b1-97ba-14fdffab089e.gif)
