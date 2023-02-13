# Labeled Image

## Introduction

This widget is a select `LabeledImage` input, clicking on it can be processed from python code. In this tutorial you will learn how to use `LabeledImage` widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/LabeledImage)

## Function signature

```python
LabeledImage(annotations_opacity=0.5, show_opacity_slider=True, enable_zoom=False, esize_on_zoom=False, fill_rectangle=True, border_width=3, widget_id=None)
```

![default](https://user-images.githubusercontent.com/120389559/218493332-ef9ed5d9-d42e-4044-8948-e3208c00d88f.gif)

## Parameters

|     Parameters      | Type  |                        Description                        |
| :-----------------: | :---: | :-------------------------------------------------------: |
| annotations_opacity | float |                      Figures opacity                      |
| show_opacity_slider | bool  | Determines the presence of opacity slider on LabeledImage |
|     enable_zoom     | bool  |                Enable zoom on GridGallery                 |
|    esize_on_zoom    | bool  |                 Resize card to fit figure                 |
|   fill_rectangle    | bool  |                       Fill rectange                       |
|    border_width     |  int  |                       Border width                        |
|      widget_id      |  str  |                     Id of the widget                      |

### annotations_opacity

Figures opacity.

**type:** `float`

**default value:** `0.5`

```python
labeled_image = LabeledImage(annotations_opacity=1)
labeled_image.set(title=image.name, image_url=image.preview_url, ann=ann)
```

![annotations_opacity](https://user-images.githubusercontent.com/120389559/218493802-4ab354e1-fcf2-4eea-8184-eadf6b1a176a.png)

### show_opacity_slider

Determines the presence of opacity slider on LabeledImage.

**type:** `bool`

**default value:** `true`

```python
labeled_image = LabeledImage(show_opacity_slider=False)
labeled_image.set(title=image.name, image_url=image.preview_url, ann=ann)
```

![show_opacity_slider](https://user-images.githubusercontent.com/120389559/218494420-81b0019f-6249-477b-842d-fc776112d57b.png)

### enable_zoom

Enable zoom on LabeledImage.

**type:** `bool`

**default value:** `false`

```python
labeled_image = LabeledImage(enable_zoom=True)
labeled_image.set(title=image.name, image_url=image.preview_url, ann=ann)
```

![enable_zoom](https://user-images.githubusercontent.com/120389559/218495132-3042ef1e-e400-4b4c-b4ca-eb4950b5b6cb.gif)

### resize_on_zoom

Resize card to fit figure.

**type:** `bool`

**default value:** `false`

ID of the widget.

**type:** `str`

**default value:** `None`

**Methods and attributes**

| Attributes and Methods | Description                   |
| :--------------------: | ----------------------------- |
|        `set()`         | Set item in LabeledImage.     |
|      `clean_up()`      | Clean LabeledImage from item. |
|      `is_empty()`      | Check LabeledImage is empty.  |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/039_labeled_image/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/039_labeled_image/src/main.py)

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

### Initialize project_id and dataset_id we will use in UI

```python
project_id = int(os.environ["modal.state.slyProjectId"])
dataset_id = int(os.environ["modal.state.slyDatasetId"])
project_meta = sly.ProjectMeta.from_json(data=api.project.get_meta(id=project_id))
```

### Initialize `GridGallery` widget

```python
grid_gallery = GridGallery(columns_number=3, enable_zoom=False, sync_views=True)
```

### Fill GridGallery with data

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
