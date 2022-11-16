<div align="center" markdown>
    <img src="https://user-images.githubusercontent.com/48913536/184925928-c035b6bd-6716-4080-9fac-d01967b01126.png"/>  
</div>

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/progress-bar)

## Introduction

In this tutorial you will learn how to use `Button` widget in Supervisely app.

## Function signature

```python
Button(text="Button", button_type="primary", button_size=None,
plain=False, show_loading=True, icon=None, icon_gap=5, widget_id=None)
```

![default](https://user-images.githubusercontent.com/48913536/202175644-0dc9c62a-544c-4460-8efa-f9af66e0b14f.png)

## Parameters

|  Parameters  |                                Type                                |                         Description                         |
| :----------: | :----------------------------------------------------------------: | :---------------------------------------------------------: |
|     text     |                                str                                 |         determine text that displayed on the button         |
| button_type  | Literal["primary", "info", "warning", "danger", "success", "text"] |                         button type                         |
| button_size  |                 Literal["mini", "small", "large"]                  |                         button size                         |
|    plain     |                                bool                                |         determine whether button is a plain button          |
| show_loading |                                bool                                |             determine whether button is loading             |
|     icon     |                                str                                 | button icon, accepts an icon name of Element icon component |
|   icon_gap   |                                int                                 |              gap between icon and button text               |
|  widget_id   |                                int                                 |                      id of the widget                       |

### text

Determine text that will be displayed on the button.
type: `str`
default value: `Button`

```python
button = Button(text="My text on the button")
```

![text](https://user-images.githubusercontent.com/48913536/202176057-d21bf18b-f6df-44ee-82a4-c87f5077dddb.png)

### button_type

Button type.
type: `Literal["primary", "info", "warning", "danger", "success", "text"]`
default value: `"primary"`

```python
button_primary = Button(text="primary", button_type="primary")
button_info = Button(text="info", button_type="info")
button_warning = Button(text="warning", button_type="warning")
button_danger = Button(text="danger", button_type="danger")
button_success = Button(text="success", button_type="success")
button_text = Button(text="text", button_type="text")
```

![type_primary](https://user-images.githubusercontent.com/48913536/202175723-19150a5c-3d62-474c-af7d-9802fffa6fc0.png)
![type_info](https://user-images.githubusercontent.com/48913536/202175740-14b07018-b823-4a5c-88fe-78018fb4283c.png)
![type_warning](https://user-images.githubusercontent.com/48913536/202175771-5f44ef74-4ffe-4865-8566-d332557b8e19.png)
![type_danger](https://user-images.githubusercontent.com/48913536/202175770-e96ef326-4c46-4f73-8e0e-c0788d8b0143.png)
![type_success](https://user-images.githubusercontent.com/48913536/202175768-b3934b08-b553-4f81-a209-4aa66b452c6f.png)
![type_text](https://user-images.githubusercontent.com/48913536/202175763-8140ff85-0bdb-41e0-9ad2-dbf5e0e5ea67.png)

### button_size

Button size.
type: `Literal["mini", "small", "large"]`
default value: `None`

```python
button_mini = Button(text="mini", button_size="mini")
button_small = Button(text="small", button_size="small")
button_default = Button(text="default")
button_large = Button(text="large", button_size="large")
```

![size_mini](https://user-images.githubusercontent.com/48913536/202175806-908797f7-f17a-49e1-bb52-935b5a1789f1.png)
![size_small](https://user-images.githubusercontent.com/48913536/202175804-bb9711af-d372-4e81-ae1d-2d905d2dcaa0.png)
![size_default](https://user-images.githubusercontent.com/48913536/202175802-f7083c9c-1e1c-43ac-b0aa-fc1e398b01ec.png)
![size_large](https://user-images.githubusercontent.com/48913536/202175800-ae6d2b9d-6b1c-45a9-b5ca-5b4a055f67e1.png)

### plain

Determine whether button is a plain button.
type: `bool`
default value: `False`

```python
button_plain = Button(plain=True)
```

![plain](https://user-images.githubusercontent.com/48913536/202175892-c7fb1d5f-5e69-4369-9d92-df58077d2840.png)

### show_loading

Determine whether button is loading.
type: `bool`
default value: `False`

```python
button = Button(show_loading=True)
```

![loading](https://user-images.githubusercontent.com/48913536/202175896-9a999d2b-aeca-4512-9291-7308bba26e9b.gif)

### icon

Button icon, accepts an icon name of Element icon component.
type: `str`
default value: `None`

```python
button_icon = Button(text="icon", icon="zmdi zmdi-play")
```

![icon](https://user-images.githubusercontent.com/48913536/202175834-eee3ec21-99b9-46e9-89c2-7a067f5d3362.png)

### icon_gap

Gap between icon and button text.
type: `int`
default value: `5`

```python
button_icon_gap_5 = Button(text="icon gap 5", icon="zmdi zmdi-play", icon_gap=5)
button_icon_gap_50 = Button(text="icon gap 50", icon="zmdi zmdi-play", icon_gap=50)
```

![icon_gap_5](https://user-images.githubusercontent.com/48913536/202175845-39f72731-e625-4793-b3aa-e232189d36ae.png)
![icon_gap_50](https://user-images.githubusercontent.com/48913536/202175842-14192061-4f6b-429c-8d5a-3af8997e85b0.png)

### widget_id

ID of the widget.

### Mini App Example

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

### Initialize `Button` and `Text` widgets

```python
button_add = Button(text="Add", icon="zmdi zmdi-plus-1")
button_subtract = Button(text="Subtract", icon="zmdi zmdi-neg-1")
text_num = Text(text="0", status="text")
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place 3 widgets that we've just created in the `Container` widget. Place order in the `Container` is important, we want buttons to be displayed above `Text` widget.

```python
card = Card(
    "Button",
    description="👉 Click on the button to add or subtract 1",
    content=Container([button_add, button_subtract, text_num]),
)
layout = Container(widgets=[card], direction="vertical")
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```

Our app layout is ready. It's time to handle button clicks.

### Handle button clicks

Use the decorator as shown below to handle button click.
We have 2 buttons, one for adding and another one for subtracting

```python
@button_add.click
def add():
    text_num.text = str(int(text_num.text) + 1)

@button_subtract.click
def subtract():
    text_num.text = str(int(text_num.text) - 1)
```
