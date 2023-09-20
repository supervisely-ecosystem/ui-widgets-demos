# ImageSlider

## Introduction

**`ImageSlider`** widget in Supervisely is a simple widget that displays images using Slider and is convenient to use when there is no need to add extra functions for displaying annotations or adjusting their settings, but only to display the images passed to it by a list of URLs or local paths.

[Read this tutorial in the developer portal.](https://developer.supervise.ly/app-development/widgets/controls/imageslider)

## Function signature

```python
ImageSlider(
    data: List[str],
    height=200,
    selectable=False,
    preview_idx=0,
    preview_url=None,
    widget_id=None,
)
```

![default](https://user-images.githubusercontent.com/120389559/224553705-a6e109d5-f8cf-4243-b3f7-fb096bc2876e.png)

## Parameters

|  Parameters   |    Type     |                        Description                        |
| :-----------: | :---------: | :-------------------------------------------------------: |
|    `data`     | `List[str]` |        List of image URLs for the `Slider` widget         |
|   `height`    |    `int`    |               Height of the `Slider` widget               |
| `selectable`  |   `bool`    | Determines whether image selection is enabled or disabled |
| `preview_idx` |    `int`    |     Index of the initially selected image in `Slider`     |
| `preview_url` |    `str`    |      URL of the initially selected image in `Slider`      |
|  `widget_id`  |    `str`    |                     ID of the widget                      |

### data

List of image URLs for the `Slider` widget.

**type:** `List[str]`

```python
image_urls = [
    "https://www.w3schools.com/howto/img_nature.jpg",
    "https://www.quackit.com/pix/samples/18m.jpg",
    "https://i.imgur.com/35pUPD2.jpg",
    "https://i.imgur.com/fB2DBcM.jpeg",
    "https://i.imgur.com/OpSj3JE.jpg",
]

image_slider = ImageSlider(data=image_urls)
```

![default](https://user-images.githubusercontent.com/120389559/224553705-a6e109d5-f8cf-4243-b3f7-fb096bc2876e.png)

### height

Height of the `Slider` widget.

**type:** `int`

**default value:** `200`

```python
image_slider = ImageSlider(data=image_urls, height=100)
```

![height](https://user-images.githubusercontent.com/120389559/224554054-e5ce7521-283c-4a17-aa97-3432e2bb03df.png)

### selectable

Determines whether image selection is enabled or disabled.

**type:** `bool`

**default value:** `False`

```python
image_slider = ImageSlider(data=image_urls, selectable=True)
```

![selectable](https://user-images.githubusercontent.com/120389559/224554387-5cb72289-a185-4a98-86b3-bfc8793b4c48.gif)

### preview_idx

Index of the initially selected image in `Slider`. Use only if `selectable` is `True`.

**type:** `int`

**default value:** `0`

```python
image_slider = ImageSlider(data=image_urls, selectable=True, preview_idx=4)
```

![preview_idx](https://user-images.githubusercontent.com/120389559/224554540-e6b08895-a51f-490b-8af1-e604b46903a4.png)

### preview_url

URL of the initially selected image in `Slider`. Use only if `selectable` is `True`.

**type:** `str`

**default value:** `None`

```python
image_slider = ImageSlider(
    data=image_urls, selectable=True, preview_url="https://i.imgur.com/35pUPD2.jpg"
)
```

![preview_url](https://user-images.githubusercontent.com/120389559/224554736-5f71c249-9dbb-41b2-9cb2-d04bfe0e5abe.png)

### widget_id

ID of the widget.

**type:** `str`

**default value:** `None`

|    Attributes and Methods     | Description                                                                     |
| :---------------------------: | ------------------------------------------------------------------------------- |
|      `get_preview_url()`      | Get URL of the selected image in the slider.                                    |
| `set_preview_url(value: str)` | Sets URL of the image to be displayed as the preview image in the slider.       |
|      `get_preview_idx()`      | Retrieves the index of the currently selected image in the slider.              |
| `set_preview_idx(value: int)` | Sets the index of the image to be displayed as the preview image in the slider. |
|        `is_selectable`        | Returns a boolean indicating whether image selection is enabled or disabled.    |
|     `enable_selection()`      | Enables image selection.                                                        |
|     `disable_selection()`     | Disables image selection.                                                       |
|      `get_data_length()`      | Retrieves the length of the image URL list.                                     |

## Mini App Example

You can find this example in our GitHub repository:

[supervisely-ecosystem/ui-widgets-demos/misc/image_slider/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/misc/image_slider/src/main.py)

```python
import os

from dotenv import load_dotenv
import supervisely as sly
from supervisely.app.widgets import Card, Container, Text, ImageSlider, Button
```

### Init API client

Init API for communicating with Supervisely Instance. First, we load environment variables with credentials:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))
api = sly.Api()
```

### Initialize `ImageSlider` widget

```python
image_urls = [
    "https://www.w3schools.com/howto/img_nature.jpg",
    "https://www.quackit.com/pix/samples/18m.jpg",
    "https://i.imgur.com/35pUPD2.jpg",
    "https://i.imgur.com/fB2DBcM.jpeg",
    "https://i.imgur.com/OpSj3JE.jpg",
]


image_slider = ImageSlider(data=image_urls, selectable=True, height=250)
```

### Initialize `Text` and `Button` widgets, we will use

```python
image_url = Text()
image_index = Text()

button_url = Button(text="Get image url")
button_index = Button(text="Get image index")

buttons_container = Container(
    widgets=[button_url, button_index],
    direction="vertical",
)
```

### Create app layout

Prepare a layout for the app using `Card` widget with the `content` parameter and place widgets that we've just created in the `Container` widget. Place order in the `Container` is important, we want buttons to be displayed above the `Text` widget.

```python
card = Card(
    title="Image Slider",
    content=Container([image_slider, image_url, image_index, buttons_container]),
)

layout = Container(widgets=[card])
```

### Create an app using the layout

Create an app object with the layout parameter.

```python
app = sly.Application(layout=layout)
```

Our app layout is ready. It's time to handle button clicks.

### Add functions to control widgets from python code

```python
@button_url.click
def get_url():
    image_url.set(text=f"Image URL: {image_slider.get_preview_url()}", status="info")


@button_index.click
def get_index():
    image_index.set(text=f"Image index on slider: {image_slider.get_preview_idx()}", status="info")
```

![layout](https://user-images.githubusercontent.com/120389559/224554987-8fe055ae-0ccf-4994-ac4b-8fec064f0a4a.gif)
