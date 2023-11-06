# Image Annotation Preview

## Introduction

**`ImageAnnotationPreview`** is a widget for displaying image annotation.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/imageannotationpreview)

## Function signature

```python
image_preview = ImageAnnotationPreview(
    annotations_opacity = 0.5,
    enable_zoom = False,
    line_width = 1,
)
```

![image-annotation-preview-default]()

## Parameters

|      Parameters       |  Type   |                  Description                  |
| :-------------------: | :-----: | :-------------------------------------------: |
| `annotations_opacity` | `float` |           Opacity of the annotation           |
|     `enable_zoom`     | `bool`  |        If `True` allows to zoom image         |
|     `line_width`      |  `int`  | Width of the annotation border (contour) line |
|      `widget_id`      |  `str`  |               ID of the widget                |

### annotations_opacity

Annotation opacity. Value must be between 0 and 1. Set to 0 to hide annotations.

**type:** `float`

**default value:** `0.5`

```python
image_preview = ImageAnnotationPreview(
    annotations_opacity = 1,
)
```

![annotation-opacity]()

### enable_zoom

If `True` allows to zoom image.

**type:** `bool`

**default value:** `False`

```python
image_preview = ImageAnnotationPreview(
    enable_zoom = True,
)
```

![enable-zoom]()

### line_width

Width of the annotation border (contour) line. Set to 0 to hide line.

**type:** `int`

**default value:** `1`

```python
image_preview = ImageAnnotationPreview(
    line_width = 0,
)
```

![line-width]()

### widget_id

ID of the widget.

**type:** `str`

**default value:** `None`

## Methods and attributes

| Attributes and Methods | Description                                     |
| :--------------------: | ----------------------------------------------- |
|        `set()`         | Set image and annotation to widget.             |
|      `clean_up()`      | Clean up widget from image.                     |
|      `is_empty()`      | Return bool value, whether image is set or not. |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/media/015_image_annotation_preview/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/media/015_image_annotation_preview/src/main.py)

### Import libraries

```python
import os
from random import choice
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, ImageAnnotationPreview
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Initialize `Project ID`

```python
project_id = sly.env.project_id()
```

### Get Project ID and meta

```python
project_id = sly.env.project_id()
project_meta_json = api.project.get_meta(project_id)
project_meta = sly.ProjectMeta.from_json(project_meta_json)
```

### Get images from dataset

```python
dataset = api.dataset.get_list(project_id)[0]
images = api.image.get_list(dataset.id)
image = images[0]
```

### Get annotation for image

```python
ann_json = api.annotation.download(image.id).annotation
ann = sly.Annotation.from_json(ann_json, project_meta)
```

### Initialize ImageAnnotationPreview widget and set image with annotation and project meta

```python
image_preview = ImageAnnotationPreview(
    annotations_opacity=0.5,
    enable_zoom=False,
    line_width=1,
)
image_preview.set(image_url=image.preview_url, ann=ann, project_meta=project_meta)
```

### Add button widget to show random image, we will use it later

```python
random_button = Button("Random image")
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widgets that we've just created in the `Container` widget.

```python
card = Card(title="ImageAnnotationPreview", content=Container([image_preview, random_button]))
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```

![miniapp]()

### Add button click event to update preview

```python
@random_button.click
def set_random_image():
    random_image = choice(images)
    random_ann_json = api.annotation.download(random_image.id).annotation
    random_ann = sly.Annotation.from_json(random_ann_json, project_meta)
    image_preview.set(image_url=random_image.preview_url, ann=random_ann, project_meta=project_meta)
```
