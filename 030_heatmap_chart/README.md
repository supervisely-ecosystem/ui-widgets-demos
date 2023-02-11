# Heatmap Chart

## Introduction

This widget is a select `HeatmapChart` input, clicking on it can be processed from python code. In this tutorial you will learn how to use `HeatmapChart` widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/HeatmapChart)

## Function signature

```python
HeatmapChart(title, data_labels=True, xaxis_title=None, color_range="row", tooltip=None)
```

![default](https://user-images.githubusercontent.com/120389559/218247387-621e000a-56ef-4b0a-9900-1ef8cd0ebf38.gif)

## Parameters

| Parameters  |          Type           |                               Description                               |
| :---------: | :---------------------: | :---------------------------------------------------------------------: |
|    title    |           str           |                           HeatmapChart title                            |
| data_labels |          bool           | Determines whether the values ​​in the HeatmapChart cells are displayed |
| xaxis_title |           str           |                               X axe title                               |
| color_range | Literal["table", "row"] |            Determines the color distribution on HeatmapChart            |
|   tooltip   |           str           |        Determines the displayed value in the HeatmapChart cells         |

### title

Determines HeatmapChart title .

**type:** `str`

### data_labels

Determines whether the values ​​in the HeatmapChart cells are displayed.

**type:** `bool`

**default value:** `true`

```python
chart = HeatmapChart(
    title="Multiplication Table",
    xaxis_title="",
    data_labels='False'
    color_range="row",
    tooltip="Result multiplication of {x} * {series_name}",
)
```

![data_labels](https://user-images.githubusercontent.com/120389559/218247687-c27fcc47-16ab-40a5-a025-df8766dc5f42.gif)

### xaxis_title

Determines X axe title.

**type:** `str`

**default value:** `None`

```python
chart = HeatmapChart(
    title="Multiplication Table",
    xaxis_title="xaxis_title",
    color_range="row",
    tooltip="Result multiplication of {x} * {series_name}",
)
```

![xaxis_title](https://user-images.githubusercontent.com/120389559/218247762-ea5506e9-c029-41cf-b976-d9d80aee8b09.png)

### color_range

Determines the color distribution on HeatmapChart.

**type:** `Literal["table", "row"]`

**default value:** `row`

```python
chart = HeatmapChart(
    title="Multiplication Table",
    xaxis_title="xaxis_title",
    color_range="table",
    tooltip="Result multiplication of {x} * {series_name}",
)
```

![color_range](https://user-images.githubusercontent.com/120389559/218247863-836b4834-fe1d-499c-a324-9db938ef9f3c.png)

### tooltip

Determines the displayed value in the HeatmapChart cells.

**type:** `str`

**default value:** `None`

```python
chart = HeatmapChart(
    title="Multiplication Table",
    tooltip="Result multiplication of {x} * {series_name}",
)
```

![tooltip](https://user-images.githubusercontent.com/120389559/218247998-6d6503a6-d5b4-4565-a4de-7aa0e96d52e1.gif)

**Methods and attributes**

| Attributes and Methods | Description                       |
| :--------------------: | --------------------------------- |
|       `append()`       | Add item in GridGallery.          |
|      `clean_up()`      | Clean GridGallery from all items. |

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
