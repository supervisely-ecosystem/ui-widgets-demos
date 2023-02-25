# BindedInputNumber

## Introduction

In this tutorial you will learn how to use `BindedInputNumber` widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/BindedInputNumber)

## Function signature

```python
BindedInputNumber(width=256, height=256, min=1, max=10000, proportional=False, widget_id=None)
```

![default](https://user-images.githubusercontent.com/120389559/219939414-e601fd63-3cdb-420e-99c4-706b48710a41.png)

## Parameters

|   Parameters   |  Type  |                    Description                     |
| :------------: | :----: | :------------------------------------------------: |
|    `width`     | `int`  |                    Width value                     |
|    `height`    | `int`  |                    Weight value                    |
|     `min`      | `int`  |               Minimum allowed value                |
|     `max`      | `int`  |               Maximum allowed value                |
| `proportional` | `bool` | Synchronize changes in width and height parameters |
|  `widget_id`   | `str`  |                  Id of the widget                  |

### width

Determine width value.

**type:** `int`

**default value:** `256`

```python
binded_input_number = BindedInputNumber(width=15)
```

![width](https://user-images.githubusercontent.com/120389559/219939697-abd65ad3-b85d-410f-8424-15fd2e34bff8.png)

### height

Determine height value.

**type:** `int`

**default value:** `256`

```python
binded_input_number = BindedInputNumber(height=15)
```

![height](https://user-images.githubusercontent.com/120389559/219939756-0791330e-e047-49be-abba-a54957ebe322.png)

### min

Minimum allowed value.

**type:** `int`

**default value:** `1`

### max

Maximum allowed value.

**type:** `int`

**default value:** `10000`

```python
binded_input_number = BindedInputNumber(width=12, height=12, min=10, max=14)
```

![min_max](https://user-images.githubusercontent.com/120389559/221354865-018d95d0-c540-462c-888f-b9b1fc71a389.gif)

### proportional

Synchronize changes in width and height parameters.

**type:** `bool`

**default value:** `false`

```python
binded_input_number = BindedInputNumber(proportional=True)
```

![proportional](https://user-images.githubusercontent.com/120389559/221354956-e537a019-80ec-4964-b4b3-fbbf5052747b.gif)

### widget_id

ID of the widget.

**type:** `str`

**default value:** `None`

## Methods and attributes

|      Attributes and Methods      | Description                             |
| :------------------------------: | --------------------------------------- |
| `value(width: int, height: int)` | Set widgets `width` and `height` filed. |
|          `get_value()`           | Get input `width` and `height` values.  |
|   `proportional(value: bool)`    | Set `proportional` value.               |
|        `min(value: int)`         | Set `min` value.                        |
|        `max(value: int)`         | Set `max` value.                        |
|           `disable()`            | Disable widget.                         |
|            `enable()`            | Enable widget.                          |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/051_binded_input_number/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/051_binded_input_number/src/main.py)

### Import libraries

```python
import supervisely as sly
from supervisely.app.widgets import Container, BindedInputNumber, Card
```

### Initialize `BindedInputNumber` widget

```python
binded_input_number = BindedInputNumber()
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card = Card(
    title="Binded Input Number",
    content=Container(widgets=[binded_input_number]),
)

layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```

![layout](https://user-images.githubusercontent.com/120389559/219942364-cb93b2fb-ca7b-40e7-8d8f-591525092bf1.gif)
