# CompareImages

## Introduction

**`CompareImages`** is a simple widget that allows you to compare two images using `Image`, `LabedledImage` or `ImageAnnotationPreview` widgets. It can be useful for comparing images before and after processing, or for comparing images with different annotations (in this case, the `ImageAnnotationPreview` or `LabedledImage` widget should be used).

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/widgets/compare-data/compareimages)

## Function signature

```python
CompareImages(
    left=None,
    right=None,
    widget_id=None,
)
```

![default](https://github.com/supervisely-ecosystem/ui-widgets-demos/assets/48913536/bb0929fd-3e4d-4244-8000-bfe2e95cf913)

## Parameters

| Parameters  |                          Type                           |   Description    |
| :---------: | :-----------------------------------------------------: | :--------------: |
|   `left`    | `Optional[Image, LabeledImage, ImageAnnotationPreview]` |    Left image    |
|   `right`   | `Optional[Image, LabeledImage, ImageAnnotationPreview]` |   Right image    |
| `widget_id` |                          `str`                          | ID of the widget |

### left

Widget with Image that will be displayed on the left side.

**type:** `Optional[Image, LabeledImage, ImageAnnotationPreview]`

**default value:** `None`

![left](https://github.com/supervisely-ecosystem/ui-widgets-demos/assets/48913536/05e76c51-f053-4f07-be6d-5fad6f18154c)

### right

Widget with Image that will be displayed on the right side.

**type:** `Optional[Image or LabeledImage]`

**default value:** `None`

```python
compare_images = CompareImages(left=Image(), right=Image())
```

![right](https://github.com/supervisely-ecosystem/ui-widgets-demos/assets/48913536/472a2db3-1fe9-42a4-9ac2-037c8ee96081)

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

In this example we will use only `ImageAnnotationPreview` widget for displaying images with annotations. Check out the mini app example in our Github repository to learn how to use it with `Image` and `LabeledImage` widgets.

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/compare-data/005_compare_images/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/compare-data/005_compare_images/src/main.py)

### Import libraries

```python
import os
from random import choice
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import (
    Button,
    Card,
    Container,
    CompareImages,
    ImageAnnotationPreview,
)
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

This app requires that you project have at least 2 images in it. If you don't have any projects, you can get one from [Supervisely Ecosystem](https://ecosystem.supervisely.com/projects).

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

### Collect image names, URLs and annotations

```python
image_names = []
image_preview_urls = []
image_anns = []
for idx in range(len(images_infos)):
    image_names.append(images_infos[idx].name)
    image_preview_urls.append(images_infos[idx].preview_url)
    image_anns.append(
        sly.Annotation.from_json(data=anns_infos[idx].annotation, project_meta=project_meta)
    )
```

### Initialize widgets and fill it with image data

```python
left_image_widget = ImageAnnotationPreview()
left_image_widget.set(
    image_url=image_preview_urls[0],
    ann=image_anns[0],
    project_meta=project_meta
)

right_image_widget = ImageAnnotationPreview()
right_image_widget.set(
    image_url=image_preview_urls[1],
    ann=image_anns[1],
    project_meta=project_meta,
)
```

### Initialize `CompareImages` widget

```python
compare_images = CompareImages(left=left_image_widget, right=right_image_widget)
```

### Create buttons for updating images

```python
button_set_left = Button("Set left image")
button_set_right = Button("Set right image")
btn_set_both = Button("Update left & right")
btn_clean_left = Button("Clean left")
btn_clean_right = Button("Clean right")
buttons = Container(
    [button_set_left, btn_clean_left, btn_set_both, btn_clean_right, button_set_right],
    direction="horizontal",
)
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card = Card(
    title="Compare Images",
    content=compare_images,
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
    random_idx = choice(range(len(image_names)))
    compare_images.update_left(
        image_url=image_preview_urls[random_idx],
        ann=image_anns[random_idx],
        project_meta=project_meta,
    )


@button_set_right.click
def add():
    random_idx = choice(range(len(image_names)))
    compare_images.update_right(
        image_url=image_preview_urls[random_idx],
        ann=image_anns[random_idx],
        project_meta=project_meta,
    )

@btn_set_both.click
def update_left_n_right():
    random_idx_l = choice(range(len(image_names)))
    random_idx_r = choice(range(len(image_names)))
    if random_idx_r == random_idx_l:
        random_idx_r = choice(range(len(image_names)))

    compare_images.update_left(
        image_url=image_preview_urls[random_idx_l],
        ann=image_anns[random_idx_l],
        project_meta=project_meta,
    )

    compare_images.update_right(
        image_url=image_preview_urls[random_idx_r],
        ann=image_anns[random_idx_r],
        project_meta=project_meta,
    )

@btn_clean_left.click
def add():
    compare_images.clean_up_left()


@btn_clean_right.click
def add():
    compare_images.clean_up_right()
```

![miniapp](https://github.com/supervisely-ecosystem/ui-widgets-demos/assets/48913536/4807b1c3-2785-40e5-9193-57d6fc2cd005)
