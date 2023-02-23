# Grid Gallery

## Introduction

In this tutorial you will learn how to use `GridGallery` widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/gridgallery)

## Function signature

```python
GridGallery(
    columns_number,
    annotations_opacity=0.5,
    show_opacity_slider=True,
    enable_zoom=False,
    esize_on_zoom=False,
    sync_views=False,
    fill_rectangle=True,
    border_width=3,
    widget_id=None,
)
```

![default](https://user-images.githubusercontent.com/120389559/218119199-81c0a7f8-d1c1-4d8f-976d-43f6bdc86851.gif)

## Parameters

|      Parameters       |  Type   |                        Description                         |
| :-------------------: | :-----: | :--------------------------------------------------------: |
|   `columns_number`    |  `int`  |       Determines number of columns on `GridGallery`        |
| `annotations_opacity` | `float` |                      Figures opacity                       |
| `show_opacity_slider` | `bool`  | Determines the presence of opacity slider on `GridGallery` |
|     `enable_zoom`     | `bool`  |                Enable zoom on `GridGallery`                |
|   `resize_on_zoom`    | `bool`  |                 Resize card to fit figure                  |
|     `sync_views`      | `bool`  |               Sync pan & zoom between views                |
|      `widget_id`      |  `str`  |                      Id of the widget                      |

### columns_number

Determines number of columns on `GridGallery`.

**type:** `int`

**default value:** `1`

```python
grid_gallery = GridGallery(columns_number=4)
```

![columns](https://user-images.githubusercontent.com/120389559/218127708-13c6f79e-fd51-4ea8-9f7e-a6a6889f71d5.png)

### annotations_opacity

Figures opacity.

**type:** `float`

**default value:** `0.5`

```python
grid_gallery = GridGallery(columns_number=3, annotations_opacity=1)
```

![annotations_opacity](https://user-images.githubusercontent.com/120389559/218128278-925a8f65-5505-43ec-a3a0-1eb34bc6dc2d.png)

### show_opacity_slider

Determines the presence of opacity slider on `GridGallery`.

**type:** `bool`

**default value:** `true`

```python
grid_gallery = GridGallery(columns_number=3, show_opacity_slider=False)
```

![show_opacity_slider](https://user-images.githubusercontent.com/120389559/218129356-d3dc9c92-3d00-4e5f-a361-1a5b0c97a120.png)

### enable_zoom

Enable zoom on `GridGallery`.

**type:** `bool`

**default value:** `false`

```python
grid_gallery = GridGallery(columns_number=3, enable_zoom=True)
```

![enable_zoom](https://user-images.githubusercontent.com/120389559/218130261-31160ede-13c4-4a08-8998-3949678ed943.gif)

### resize_on_zoom

Resize card to fit figure.

**type:** `bool`

**default value:** `false`

### sync_views

Sync pan & zoom between views.

**type:** `bool`

**default value:** `false`

```python
grid_gallery = GridGallery(columns_number=3, enable_zoom=True, sync_views=True)
```

![sync_views](https://user-images.githubusercontent.com/120389559/218132098-3b799735-2494-4eb5-9489-fae636e9d2c5.gif)

### widget_id

ID of the widget.

**type:** `str`

**default value:** `None`

## Methods and attributes

|                                                                       Attributes and Methods                                                                        | Description                         |
| :-----------------------------------------------------------------------------------------------------------------------------------------------------------------: | ----------------------------------- |
|                                                               `get_column_index(incoming_value: int)`                                                               | Return column index by given value. |
| `append(image_url: str, annotation: Annotation = None, title: str = "", column_index: int = None, zoom_to: int = None, zoom_factor: float = 1.2, title_url = None)` | Add item in `GridGallery`.          |
|                                                                            `clean_up()`                                                                             | Clean `GridGallery` from all items. |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/029_grid_gallery/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/029_grid_gallery/src/main.py)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, GridGallery
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Initialize `Project` ID and `Dataset` ID we will use in UI

```python
project_id = int(os.environ["modal.state.slyProjectId"])
dataset_id = int(os.environ["modal.state.slyDatasetId"])
project_meta = sly.ProjectMeta.from_json(data=api.project.get_meta(id=project_id))
```

### Initialize `GridGallery` widget

```python
grid_gallery = GridGallery(columns_number=3, enable_zoom=False, sync_views=True)
```

### Fill `GridGallery` with data

```python
grid_gallery = GridGallery(columns_number=3, enable_zoom=False, sync_views=True)

images_infos = api.image.get_list(dataset_id=dataset_id)[: grid_gallery.columns_number]
anns_infos = api.annotation.get_list(dataset_id=dataset_id)[
: grid_gallery.columns_number
]
for idx, (image_info, ann_info) in enumerate(zip(images_infos, anns_infos)):
image_name = image_info.name
image_url = image_info.full_storage_url
image_ann = sly.Annotation.from_json(
data=ann_info.annotation, project_meta=project_meta
)

    grid_gallery.append(
        title=image_name, image_url=image_url, annotation=image_ann, column_index=idx
    )
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card = Card(
    title="Grid Gallery",
    content=grid_gallery,
)

layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```
