# Editor

## Introduction

In this tutorial you will learn how to use `Editor` widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/editor)

## Function signature

```python
Editor(
    initial_text="",
    height_px=100,
    height_lines=None,
    language_mode="json",
    readonly=False,
    show_line_numbers=True,
    highlight_active_line=True,
    restore_default_button=True,
    widget_id=None,
)
```

![default](https://user-images.githubusercontent.com/120389559/222461320-3164d65c-c2e4-40b8-a65e-6b3f083b30d3.gif)

## Parameters

|        Parameters        |                           Type                            |         Description          |
| :----------------------: | :-------------------------------------------------------: | :--------------------------: |
|      `initial_text`      |                           `str`                           |          Start text          |
|       `height_px`        |                           `int`                           |        Editor height         |
|      `height_lines`      |                           `int`                           | Editor height by lines count |
|     `language_mode`      | `Literal["json", "html", "plain_text", "yaml", "python"]` |     Editor language mode     |
|        `readonly`        |                          `bool`                           |        Read only mode        |
|   `show_line_numbers`    |                          `bool`                           |      Show line numbers       |
| `highlight_active_line`  |                          `bool`                           |    Highlight active line     |
| `restore_default_button` |                          `bool`                           |     Show default button      |
|       `widget_id`        |                           `str`                           |       Id of the widget       |

### initial_text

Determine start `Editor` text.

**type:** `str`

**default value:** `""`

```python
editor = Editor('{ "value": 10 }')
```

![initial_text](https://user-images.githubusercontent.com/120389559/222464999-d3bcd1e3-3a38-46b4-9d4d-815622d60047.png)

### height_px

Determine `Editor` height.

**type:** `int`

**default value:** `100`

```python
editor = Editor(height_px=300)
```

![height_px](https://user-images.githubusercontent.com/120389559/222465710-6be3c197-ad1b-41c2-afe0-ee01077f6048.png)

### height_lines

Determine `Editor` height by lines count.

**type:** `int`

**default value:** `None`

```python
editor = Editor(height_lines=5)
```

![height_lines](https://user-images.githubusercontent.com/120389559/222467049-a130d328-dfc8-4a11-bb04-8008bac277bf.gif)

### language_mode

Determine `Editor` language mode.

**type:** `Literal["json", "html", "plain_text", "yaml", "python"]`

**default value:** `json`

```python
editor_json = Editor('{ "value": 10 }', language_mode="json")
editor_html = Editor("<div> </div>", language_mode="html")
editor_plain_text = Editor("plain_text example", language_mode="plain_text")
editor_yaml = Editor('ray: "a drop of golden sun"', language_mode="yaml")
editor_python = Editor("import supervisely as sly", language_mode="python")

card = Card(content=Container([editor_json, editor_html, editor_plain_text, editor_yaml, editor_python]))
```

![language_mode](https://user-images.githubusercontent.com/120389559/222470256-6ccc3b15-891a-44f1-aec0-75ed66af1e1f.png)

### readonly

Determine readonly mode.

**type:** `bool`

**default value:** `false`

```python
editor = Editor('{ "value": 10 }', readonly=True)
```

![readonly](https://user-images.githubusercontent.com/120389559/222471583-eb4ebf25-d886-468d-9363-6ce6e29cc130.gif)

### show_line_numbers

Determine show_line_numbers or not.

**type:** `bool`

**default value:** `true`

```python
editor = Editor('{ "value": 10 }', show_line_numbers=False)
```

![show_line_numbers](https://user-images.githubusercontent.com/120389559/222472845-15472c19-d73f-4064-8c17-7fd9cfde62c2.png)

### highlight_active_line

Determine highlight active line or not.

**type:** `bool`

**default value:** `true`

```python
editor = Editor('{ "value": 10 }', highlight_active_line=False)
```

![highlight_active_line](https://user-images.githubusercontent.com/120389559/222473727-7e5a252c-1dcd-4d65-8df9-ac525c766986.png)

### restore_default_button

Determine highlight active line or not.

**type:** `bool`

**default value:** `true`

```python
editor = Editor('{ "value": 10 }', restore_default_button=False)
```

![restore_default_button](https://user-images.githubusercontent.com/120389559/222474457-c8ee9c8b-6fa2-4a56-8366-ac72e1f72737.png)

### widget_id

ID of the widget.

**type:** `str`

**default value:** `None`

## Methods and attributes

| Attributes and Methods  | Description                     |
| :---------------------: | ------------------------------- |
|      `get_text()`       | Return `Editor` text.           |
|  `show_line_numbers()`  | Show line numbers.              |
|  `hide_line_numbers()`  | Hide line numbers.              |
| `readonly(value: bool)` | Set `Editor` in readonly state. |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/misc/editor/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/misc/editor/src/main.py)

### Import libraries

```python
import os
from dotenv import load_dotenv
import supervisely as sly
from supervisely.app.widgets import Container, Editor, Text, Card, Button
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Initialize `Editor` widget

```python
editor = Editor('{ "value": 10 }')
```

### Initialize `Button` and `Text` widgets we will use

```python
show_lines_button = Button("Show line numbers", button_type="success")
hide_lines_button = Button("Hide line numbers", button_type="danger")
readonly_true_button = Button("Set readonly=True", button_type="success")
readonly_false_button = Button("Set readonly=False", button_type="danger")
get_text_button = Button("Get Text")
label = Text("")
label.hide()
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card = Card(
    title="Editor",
    content=Container(
        [
            editor,
            Container(
                [show_lines_button, hide_lines_button, readonly_true_button, readonly_false_button],
                direction="horizontal",
            ),
            get_text_button,
            label,
        ],
        gap=5,
    ),
)
layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```

### Add function to control widgets from python code

```python
@show_lines_button.click
def show_lines():
    editor.show_line_numbers()


@hide_lines_button.click
def hide_lines():
    editor.hide_line_numbers()


@readonly_true_button.click
def readonly_true():
    editor.readonly = True


@readonly_false_button.click
def readonly_false():
    editor.readonly = False


@get_text_button.click
def get_text():
    label.show()
    label.text = editor.get_text()
```

![layout](https://user-images.githubusercontent.com/120389559/222476978-093d15ad-4099-4ce0-85bc-c5f7d42913e3.gif)
