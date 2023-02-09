# Text

## Introduction

In this tutorial you will learn how to use `Text` widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/text)

## Function signature

```python
Text(text=None, status="text", widget_id=None)
```

![default](https://user-images.githubusercontent.com/120389559/217816296-b03edf40-8ac1-42f7-ac6e-d0c319bad783.png)

## Parameters

| Parameters |                          Type                          |       Description        |
| :--------: | :----------------------------------------------------: | :----------------------: |
|    text    |                          str                           | determine displayed text |
|   status   | Literal["text", "info", "success", "warning", "error"] |       text status        |
| widget_id  |                          str                           |     id of the widget     |

### text

Determine displayed text.

**type:** `str`

**default value:** `None`

```python
text = Text(text="My text")
```

### status

Text status.

**type:** `str`

**default value:** `text`

```python
text = Text(text="My text", status="text")
```

![text](https://user-images.githubusercontent.com/120389559/217818651-10a968df-60f7-45f2-a019-d1828bb6cf28.png)

```python
text_info = Text(text="My info text", status="info")
```

![info](https://user-images.githubusercontent.com/120389559/217818910-2f027556-adbf-47ea-8a9a-9042a315d813.png)

```python
text_success = Text(text="My success text", status="success")
```

![success](https://user-images.githubusercontent.com/120389559/217819084-42736f03-d71f-499b-95a2-af7eadbdaff7.png)

```python
text_warning = Text(text="My warning text", status="warning")
```

![warning](https://user-images.githubusercontent.com/120389559/217819327-4f843414-0ff9-4d81-a03e-6c795141e93a.png)

```python
text_error = Text(text="My error text", status="error")
```

![error](https://user-images.githubusercontent.com/120389559/217819527-b9762a5c-59a5-4d4e-a1f6-17ec65aef080.png)

### widget_id

ID of the widget.

**type:** `str`

**default value:** `None`

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/003_text/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/003_text/src/main.py)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, Text
```

### Init API client

Init API for communicating with Supervisely Instance. First, we load environment variables with credentials:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))
api = sly.Api()
```

### Initialize five `Button` widgets for each type of text message: text, info, success, warning, error

```python
button_show_text = Button(
    text="Text",
    button_type="primary",
    button_size="small",
    icon="zmdi zmdi-comment-text",
)
button_show_info = Button(
    text="Info", button_type="info", button_size="small", icon="zmdi zmdi-info-outline"
)
button_show_success = Button(
    text="Success", button_type="success", button_size="small", icon="zmdi zmdi-check"
)
button_show_warning = Button(
    text="Warning",
    button_type="warning",
    button_size="small",
    icon="zmdi zmdi-alert-circle-o",
)
button_show_error = Button(
    text="Error",
    button_type="danger",
    button_size="small",
    icon="zmdi zmdi-minus-circle-outline",
)
```

### Initialize `Container` widget

Create `Container` widget for all buttons.

```python
buttons_container = Container(
    widgets=[
        button_show_text,
        button_show_info,
        button_show_success,
        button_show_warning,
        button_show_error,
    ],
    direction="horizontal",
)
```

### Initialize `Text` widget with text and status

```python
text = Text(text="Lorem ipsum dolor sit amet... anim id est laborum.", status="text")
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place 2 widgets that we've just created in the `Container` widget. Place order in the `Container` is important, we want the message text to be displayed below the buttons.

```python
card = Card(
    title="Text",
    description="👉 Click on the button to change text highlighting",
    content=Container(widgets=[buttons_container, text]),
)
layout = Container(widgets=[card], direction="vertical")
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```

Our app layout is ready.

![layout](https://user-images.githubusercontent.com/120389559/217820070-ddb06396-ee61-42f9-96e0-3a92e99c268c.png)

### Start text status change with button click

Use the decorator as shown below to handle button click.
`Text` will be updating it status after pressing corresponding button.

```python
@button_show_text.click
def show_text():
    text.status = "text"
```

![text_click](https://user-images.githubusercontent.com/120389559/217820070-ddb06396-ee61-42f9-96e0-3a92e99c268c.png)

```python
@button_show_info.click
def show_info():
    text.status = "info"
```

![info_click](https://user-images.githubusercontent.com/120389559/217820638-d9770fc3-626f-4908-afaf-ba539c739e2e.png)

```python
@button_show_success.click
def show_success():
    text.status = "success"
```

![success_click](https://user-images.githubusercontent.com/120389559/217820791-854538ed-d388-4ab0-bfb4-d516ba0753ca.png)

```python
@button_show_warning.click
def show_warning():
    text.status = "warning"
```

![warning_click](https://user-images.githubusercontent.com/120389559/217820912-fe79f9b8-e003-4663-836f-50bc9e48b783.png)

```python
@button_show_error.click
def show_error():
    text.status = "error"
```

![error_click](https://user-images.githubusercontent.com/120389559/217821073-b896b175-dfa5-4b83-834f-ef30d0cd84ed.png)
