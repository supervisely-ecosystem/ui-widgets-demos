# Editor

## Introduction

**`Editor`** widget in Supervisely allows users to input and edit code with syntax highlighting. It provides a customizable text input area with options such as language selection, input height, and some styles. `Editor` widget is used for editing code snippets, as the syntax highlighting makes it easier to read and edit code for languages such as `python`, `json`, `html`, and `yaml`.

[Read this tutorial in developer portal.](https://developer.supervisely.com/app-development/widgets/text-elements/editor)

## Function signature

```python
Editor(
    initial_text='{ "value": 10 }',
    height_px=100,
    height_lines=None, # overwrites height_px if specified.
    language_mode='json',
    readonly=False,
    show_line_numbers=True,
    highlight_active_line=True,
    restore_default_button=True,
    widget_id=None,
    auto_format=False,
)
```

![editor](https://user-images.githubusercontent.com/79905215/223056987-58ea3680-037a-48d3-8db8-a16658f6b67b.png)

## Parameters

|        Parameters        |       Type       |                       Description                       |
| :----------------------: | :--------------: | :-----------------------------------------------------: |
|      `initial_text`      | `Optional[str]`  |                  Editor default value                   |
|       `height_px`        | `Optional[int]`  |            Specifies widget height in pixels            |
|      `height_lines`      | `Optional[int]`  |     Specifies the visible number of lines in widget     |
|     `language_mode`      | `Optional[int]`  |            Specifies language mode of editor            |
|        `readonly`        | `Optional[bool]` |    Specifies that a editor area should be read-only     |
|   `show_line_numbers`    | `Optional[bool]` |     Specifies displaying numbers of lines in editor     |
| `highlight_active_line`  | `Optional[bool]` | Specifies if visible highlighting active line in editor |
| `restore_default_button` | `Optional[bool]` |    Display button for settting editor default value     |
|       `widget_id`        | `Optional[str]`  |                    ID of the widget                     |
|      `auto_format`       | `Optional[bool]` |  Automatically format JSON content on initialization   |

### initial_text

Editor default value

**type:** `Optional[str]`

**default value:** `""`

```python
editor = Editor('{ "value": 10 }')
```

![editor](https://user-images.githubusercontent.com/79905215/223056987-58ea3680-037a-48d3-8db8-a16658f6b67b.png)

### height_px

Specifies widgets height in pixels.

**type:** `Optional[int]`

**default value:** `100`

```python
editor = Editor('{ "value": 10 }', height_px=200)
```

![height_px](https://user-images.githubusercontent.com/79905215/223057354-e9031a49-a94b-49f8-a5a6-cab84467fe9f.png)

### height_lines

Specifies the visible number of lines in widget.
If specified it overwrites `height_px`. If >= 1000, all lines will be displayed

**type:** `Optional[int]`

**default value:** `None`

```python
editor = Editor(
    """{
    "person1": {"first": "Nicole", "last": "Adelstein"},
    "person2": {"first": "Pleuni", "last": "Pennings"},
    "person3": {"first": "Rori", "last": "Rohlfs"}
}""",
    height_lines=10,
)
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/79905215/223059715-676fe9b2-0b4e-49b6-a0e9-764d6620323b.gif" alt="height_lines" />
</p>

### language_mode

Specifies language mode of editor.

**type:** `Optional[Literal['json', 'html', 'plain_text', 'yaml', 'python']]`

**default value:** `json`

```python
editor_json = Editor('{ "value": 10 }', language_mode="json")
editor_html = Editor("<div> </div>", language_mode="html")
editor_plain_text = Editor("plain_text example", language_mode="plain_text")
editor_yaml = Editor('ray: "a drop of golden sun"', language_mode="yaml")
editor_python = Editor("import supervisely as sly", language_mode="python")
```

![language_mode](https://user-images.githubusercontent.com/120389559/222470256-6ccc3b15-891a-44f1-aec0-75ed66af1e1f.png)

### readonly

Specifies that a editor area should be read-only.

**type:** `Optional[bool]`

**default value:** `False`

```python
editor = Editor('{ "value": 10 }', readonly=True)
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/79905215/223060673-7afba086-a7ea-4747-8e1d-0ec0149a51d6.gif" alt="readonly" />
</p>

### show_line_numbers

Specifies displaying numbers of lines in editor.

**type:** `Optional[bool]`

**default value:** `True`

```python
editor = Editor('{ "value": 10 }', show_line_numbers=False)
```

![show_line_nums](https://user-images.githubusercontent.com/79905215/223060889-935a72ca-60ae-409b-8082-9aad68921390.png)

### highlight_active_line

Specifies if visible highlighting active line in editor.

**type:** `Optional[bool]`

**default value:** `True`

```python
editor = Editor('{ "value": 10 }', highlight_active_line=False)
```

![highlight_active](https://user-images.githubusercontent.com/79905215/223061054-9f44cfaa-3b64-44dd-899e-f7dc52602e10.png)

### restore_default_button

Display button for settting editor default value.

**type:** `Optional[bool]`

**default value:** `True`

```python
editor = Editor('{ "value": 10 }', restore_default_button=False)
```

![restore_btn](https://user-images.githubusercontent.com/79905215/223061500-5ed58d85-0cc1-4d97-8ecb-5d4960cb5c13.png)

### widget_id

ID of the widget.

**type:** `Optional[str]`

**default value:** `None`

### auto_format

Automatically format JSON content on initialization.

**type:** `Optional[bool]`

**default value:** `False`

```python
editor = Editor('{ "value": 10 }', auto_format=True)
```

![auto_format](https://github.com/supervisely-ecosystem/ui-widgets-demos/assets/79905215/119750c5-8c94-4e1a-a29b-363b74eb2058)

## Methods and attributes

|                                                    Attributes and Methods                                                     | Description                           |
| :---------------------------------------------------------------------------------------------------------------------------: | ------------------------------------- |
|                                                          `readonly`                                                           | Get or set `readonly` property.       |
|                                                     `show_line_numbers()`                                                     | Display line numbers or code snippet. |
|                                                     `hide_line_numbers()`                                                     | Hide line numbers or code snippet.    |
|                                                         `get_text()`                                                          | Returns input value data.             |
| `set_text(text: Optional[str] = "", language_mode: Optional[Literal['json', 'html', 'plain_text', 'yaml', 'python']] = None)` | Set input value data.                 |

## Mini App Example

You can find this example in our GitHub repository:

[supervisely-ecosystem/ui-widgets-demos/text-elements/003_editor/src/main.py](<https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/text elements/003_editor/src/main.py>)

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
editor = Editor('{ "value": 10 }', height_px=100)
```

### Initialize widgets we will use in this demo

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

Prepare a layout for app using `Card` widget with the `content` parameter and place widgets that we've just created in the `Container` widget.

```python
btns_container = Container(
    [
        show_lines_button,
        hide_lines_button,
        readonly_true_button,
        readonly_false_button,
    ],
    direction="horizontal",
)

card_container = Container(
    [editor, btns_container, get_text_button, label],
    gap=5,
)

card = Card(title="Editor", content=card_container)
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=card)
```

Add functions to control widgets from python code

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

<p align="center">
  <img src="https://user-images.githubusercontent.com/79905215/223064271-da5039b7-56bc-4224-bbce-01a1640202e7.gif" alt="layout" />
</p>
