# CompareImages

## Introduction

**`CompareImages`** is a simple widget that allows you to compare two images using `Image` or `LabelingImage` widgets. It can be useful for comparing images before and after processing, or for comparing images with different annotations (in this case, the `LabelingImage` widget should be used).

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/widgets/media/compareimages)

## Function signature

```python
CompareImages(
    left=None,
    right=None,
    widget_id=None,
)
```

![def]()

## Parameters

| Parameters  |               Type                |                   Description                   |
| :---------: | :-------------------------------: | :---------------------------------------------: |
|   `left`    | `Optional[Image or LabeledImage]` | Left widget (`Image` or `LabeledImage` widget)  |
|   `right`   | `Optional[Image or LabeledImage]` | Right widget (`Image` or `LabeledImage` widget) |
| `widget_id` |               `str`               |                ID of the widget                 |

### left

Left widget (`Image` or `LabeledImage` widget).

**type:** `Optional[Image or LabeledImage]`

**default value:** `None`

### right

Right widget (`Image` or `LabeledImage` widget).

**type:** `Optional[Image or LabeledImage]`

**default value:** `None`

```python
compare_images = CompareImages(left=Image(), right=Image())
```

![left_right]()

### widget_id

ID of the widget.

**type:** `str`

**default value:** `None`

## Methods and attributes

| Attributes and Methods | Description                    |
| :--------------------: | ------------------------------ |
|     `update_left`      | Update left widget parameters  |
|     `update_right`     | Update right widget parameters |
|    `clean_up_left`     | Clean up left widget           |
|    `clean_up_right`    | Clean up right widget          |
|       `clean_up`       | Clean up both widgets          |

## Usage examples

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/media/002_labeled_image/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/media/002_labeled_image/src/main.py)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, CompareImages, LabeledImage, Image
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Get project ID and dataset ID

```python
project_id = sly.env.project_id()
dataset_id = sly.env.dataset_id()
```

### Get images and annotations infos

```python
project_meta = sly.ProjectMeta.from_json(data=api.project.get_meta(id=project_id))
images_infos = api.image.get_list(dataset_id=dataset_id)
anns_infos = api.annotation.get_list(dataset_id=dataset_id)
```

### Collect image names, urls and annotations

```python
image_names = []
image_urls = []
image_anns = []
for idx in range(len(images_infos)):
    image_names.append(images_infos[idx].name)
    image_urls.append(images_infos[idx].full_storage_url)
    image_anns.append(
        sly.Annotation.from_json(data=anns_infos[idx].annotation, project_meta=project_meta)
    )
```

### Initialize `LabeledImage` or `Image` widgets and fill it with image data

```python
left_labeled_image = LabeledImage(view_height=300)
right_labeled_image = LabeledImage(view_height=300)
left_labeled_image.set(title=image_names[0], image_url=image_urls[0], ann=image_anns[0])
right_labeled_image.set(title=image_names[1], image_url=image_urls[1], ann=image_anns[1])
```

or

```python
left_image = Image(url=image_urls[2], width="100%")
right_image = Image(url=image_urls[3], width="100%")
```

### Initialize `CompareImages` widget

```python
compare_images = CompareImages(left=left_labeled_image, right=right_labeled_image)
```

or

```python
compare_images = CompareImages(left=left_image, right=right_image)
```

### Create buttons for updating images

```python
button_set_left = Button("set left image")
button_set_right = Button("set right image")
btn_clean = Button("clean")
btn_clean_left = Button("clean left")
btn_clean_right = Button("clean right")
buttons = Container(
    [button_set_left, button_set_right, btn_clean, btn_clean_left, btn_clean_right],
    direction="horizontal",
)
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card = Card(
    title="Compare Images",
    content=comapre_images,
)

layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```

### Create a callback functions for buttons

```python
@button_set_left.click
def add():
    compare_images.update_left(title=image_names[2], image_url=image_urls[2], ann=image_anns[2])
    # or compare_images.update_left(url=image_urls[2])


@button_set_right.click
def add():
    compare_images.update_right(title=image_names[4], image_url=image_urls[4], ann=image_anns[4])
    # or compare_images.update_right(url=image_urls[4])


@btn_clean.click
def add():
    compare_images.clean_up()


@btn_clean_left.click
def add():
    compare_images.clean_up_left()


@btn_clean_right.click
def add():
    compare_images.clean_up_right()
```

![app]()
