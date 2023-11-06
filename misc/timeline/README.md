# Timeline

## Introduction

**`Timeline`** widget is used to display video timeline. It can be used to get current frame and display information about it.

[Read this tutorial in developer portal.](https://developer.supervisely.com/app-development/widgets/media/tagmetaview)

## Function signature

```python
timeline = Timeline(
    frames_count=31,
    intervals=[[0, 6], [6, 11], [12, 15], [16, 17], [18, 19], [20, 31]],
    colors=["#DB7093", "#93db70", "#7093db", "#70dbb8", "#db8370", "#db70c9"],
    height="30px",
)
```

![tagmeta-default](https://github.com/supervisely-ecosystem/ui-widgets-demos/assets/48913536/31589e86-d107-4d53-967e-43a48affcf05)

## Parameters

|   Parameters   |       Type        |                Description                |
| :------------: | :---------------: | :---------------------------------------: |
| `frames_count` |       `int`       |           Timeline frames count           |
|  `intervals`   | `List[List[int]]` |            Set frame intervals            |
|    `colors`    |    `List[str]`    | Set intervals colors in `hex` color codes |
|    `height`    |       `str`       |         Set widget height in `px`         |
|  `widget_id`   |       `str`       |             ID of the widget              |

### frames_count

Timeline frames count

**type:** `int`

```python
timeline = Timeline(
    frames_count=31,
    intervals=[[0, 6], [6, 11], [12, 15], [16, 17], [18, 19], [20, 31]],
    colors=["#DB7093", "#93db70", "#7093db", "#70dbb8", "#db8370", "#db70c9"],
)
```

![frames_count]()

### intervals

Set frame intervals. Each interval is a list of two integers: `[start_frame, end_frame]`. Intervals and colors lists must be the same length.

**type:** `List[List[int]]`

```python
timeline = Timeline(
    frames_count=31,
    intervals=[[0, 6], [6, 11], [12, 15], [16, 17], [18, 19], [20, 31]],
    colors=["#DB7093", "#93db70", "#7093db", "#70dbb8", "#db8370", "#db70c9"],
    height="30px",
)
```

![intervals]()

### colors

Set intervals colors in `hex` color codes. Intervals and colors lists must be the same length.

**type:** `List[str]`

```python
timeline = Timeline(
    frames_count=31,
    intervals=[[0, 6], [6, 11], [12, 15], [16, 17], [18, 19], [20, 31]],
    colors=["#DB7093", "#93db70", "#7093db", "#70dbb8", "#db8370", "#db70c9"],
    height="30px",
)
```

![colors]()

### height

Set widget height in `px`.

**type:** `str`

**default value:** `30px`

```python
timeline = Timeline(
    frames_count=31,
    intervals=[[0, 6], [6, 11], [12, 15], [16, 17], [18, 19], [20, 31]],
    colors=["#DB7093", "#93db70", "#7093db", "#70dbb8", "#db8370", "#db70c9"],
    height="60px",
)
```

### widget_id

ID of the widget.

**type:** `str`

**default value:** `None`

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/media/013_tag_meta_view/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/media/013_tag_meta_view/src/main.py)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Field, TagMetaView, ProjectThumbnail
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Initialize `Project ID` we will use

```python
project_id = sly.env.project_id()
```

### Get Project info and meta from server

```python
project_info = api.project.get_info_by_id(id=project_id)
project_meta = api.project.get_meta(id=project_id)
project_meta = sly.ProjectMeta.from_json(project_meta)
```

### Prepare `TagMeta` for each tag in project

Get TagMetas from project meta

```python
tag_metas = project_meta.tag_metas
```

### Initialize `TagMetaView` widget

In this tutorial we will create list of `TagMetaView` objects for each tag in project.

```python
tag_meta_view = [
    TagMetaView(
        tag_meta=tag_meta,
        show_type_text=True,
        limit_long_names=False,
    )
    for tag_meta in tag_metas
]
```

### Create app layout

Prepare a layout for app using `Card`, `Field` widgets with the `content` parameter and place widgets that we've just created in the `Container` widget.

```python
tag_metas_container = Container(widgets=tag_meta_view)
tag_metas_field = Field(
    content=tag_metas_container,
    title="Project tags:",
)

# create widget ProjectThumbnail
project_thumbnail = ProjectThumbnail(project_info)

card = Card(
    title="TagMetaView",
    content=Container(widgets=[project_thumbnail, tag_metas_field]),
)
layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```

![tagmetaview-app](https://github.com/supervisely-ecosystem/ui-widgets-demos/assets/48913536/98452051-08ea-4596-a515-483a632608bd)
