# Image Region Selector

## Introduction

**`ImageRegionSelector`** widget in Supervisely is designed to display an image with mask and bounding box and provides additional features such as the ability to change bounding box boundaries and add two types of points positive and negative.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/widgets/media/imageregionselector)

![ImageRegionSelector](https://user-images.githubusercontent.com/61844772/229194885-741fa3c3-a538-4f4f-82fd-a4227584ecb8.png)

## Function signature

```python
ImageRegionSelector(
    image_info: ImageInfo = None,
    mask: Bitmap = None,
    mask_opacity: int = 50,
    bbox: List[int] = None,
    widget_id: str = None,
    disabled: bool = False,
    widget_width: str = "100%",
    widget_height: str = "100%",
)
```


## Parameters

|     Parameters      |    Type     |                      Description                          |
| :-----------------: | :---------: | :-------------------------------------------------------: |
|    `image_info`     | `ImageInfo` |            `ImageInfo` of the displayedimage              |
|       `mask`        |  `Bitmap`   |               `Bitmap` mask to be isplayed                |
|   `mask_opacity`    |    `int`    |                     Mask opacity in %                     |
|       `bbox`        |   `List`    | Bounding box left-top and right-bottom points coordinates |
|     `widget_id`     |    `str`    |                      ID of the widget                     |
|     `disabled`      |   `bool`    |                       Disable widget                      |
|   `widget_width`    |    `str`    |                       Widget width                        |
|   `widget_height`   |    `str`    |                       Widget height                       |

### image_info

ImageInfo of the displayed image.

**type:** `ImageInfo`

**default value:** `None`

```python
image_region_selector = ImageRegionSelector(image_info=image)
image_region_selector.set_image(image_info=image)
```

### mask

Bitmap mask to be displayed.

**type:** `Bitmap`

**default value:** `None`

```python
image_region_selector = ImageRegionSelector(mask=mask)
image_region_selector.set_mask(mask=mask)
```

### mask_opacity

Mask opacity in %.

**type:** `int`

**default value:** `50`

```python
image_region_selector = ImageRegionSelector(mask_opacity=50)
```

### bbox

Bounding box left-top and right-bottom points coordinates.

**type:** `List[List[int]]`

**default value:** `None`

```python
image_region_selector = ImageRegionSelector(bbox=[[0, 0], [100, 100]])
image_region_selector.set_bbox(bbox=[[0, 0], [100, 100]])
```

### widget_id

ID of the widget.

**type:** `str`

**default value:** `None`

### disabled

Disable widget.

**type:** `bool`

**default value:** `False`

### widget_width

Widget width.

**type:** `str`

**default value:** `100%`

```python
image_region_selector = ImageRegionSelector(widget_width="100px")
```

### widget_height

Widget height.

**type:** `str`

**default value:** `100%`

```python
image_region_selector = ImageRegionSelector(widget_height="100px")
```


## Methods and attributes

|    Attributes and Methods     |                    Description                     |
| :--------------------------:  | :------------------------------------------------: |
|      `get_image_info()`       | Get current Image Info.                            |
|       `image_update()`        | Update Image.                                      |
|         `set_image()`         | Update Image.                                      |
|         `set_bbox()`          | Set Bounding box.                                  |
|         `get_bbox()`          | Get current bouning box.                           |
|         `set_mask()`          | Set Mask.                                          |
|         `get_mask()`          | Get current mask.                                  |
|       `bbox_changed()`        | Register a callback for bbox change                |
|  `positive_points_changed()`  | Register a callback for positive points placement. |
|  `negative_points_changed()`  | Register a callback for positive points placement. |
|       `get_bbox_size()`       | Get bounding box size.                             |
|     `add_bbox_padding()`      | Enlarge bbox by percent.                           |
|         `is_empty()`          | Check `ImageRegionSelector` is empty.              |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/media/006_image_region_selector/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/media/006_image_region_selector/src/main.py)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, ImageRegionSelector
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Get project ID and meta

```python
project_id = int(os.environ["modal.state.slyProjectId"])
project = api.project.get_info_by_id(project_id)
meta_json = api.project.get_meta(id=project_id)
meta = sly.ProjectMeta.from_json(data=meta_json)
```

### Get image ID and annotations

```python
image_id = int(os.environ["modal.state.slyImageId"])
image = api.image.get_info_by_id(id=image_id)
ann_json = api.annotation.download_json(image_id=image_id)
ann = sly.Annotation.from_json(data=ann_json, project_meta=meta)
```

### Initialize `ImageRegionSelector` widget and fill it with image data

```python
image_region_selector = ImageRegionSelector()
image_region_selector.set_image(image_info=image)
```

### Set mask
```python
mask = ann.labels[0].geometry.convert(sly.Bitmap)[0]
image_region_selector.set_mask(mask)
```

### Set bbox
```python
bbox = ann.labels[0].geometry.to_bbox()
bbox = [[bbox.left, bbox.top], [bbox.right, bbox.bottom]]
image_region_selector.set_bbox(bbox)
```

### Set bbox change callback

Each time when user changes bounding box, the callback will be called with new bbox coordinates.

```python
@image_region_selector.bbox_changed
def bbox_changed(bbox):
    print("bbox changed", bbox)
```

### Set positive points change callback

Each time when user changes positive points, the callback will be called with new positive points coordinates.

```python
@image_region_selector.positive_points_changed
def positive_points_changed(points):
    print("positive points changed", points)
```

### Set negative points change callback

Each time when user changes negative points, the callback will be called with new negative points coordinates.

```python
@image_region_selector.negative_points_changed
def negative_points_changed(points):
    print("negative points changed", points)
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card = Card(
    title="Image Region Selector",
    content=image_region_selector,
)

layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```
