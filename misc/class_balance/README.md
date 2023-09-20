# Class Balance

## Introduction

**`ClassBalance`** is a widget in Supervisely that allows for displaying input data classes balance on the UI. For example, you can display the distribution of tags to different classes in the project, or set your data according to the required format.
It also provides functionality for data streaming and dynamic updates, allowing the class balance to display real-time data. Additionally, users can control the widget through Python code by detecting events such as clicking on a class name or segment data.

[Read this tutorial in the developer portal.](https://developer.supervise.ly/app-development/widgets/charts-and-plots/classbalance)

## Function signature

```python
ClassBalance(
    max_height=300,
    selectable=True,
    collapsable=False,
    clickable_name=False,
    clickable_segment=False,
    max_value=None,
    segments=[],
    rows_data=[],
    slider_data={},
    widget_id=None,
)
```

Example of input data we will use. If `max_value` is None, the maximum `total` form `rows_data` will be taken as `max_value`.

```python
max_value = 1000
segments = [
    {"name": "Train", "key": "train", "color": "#1892f8"},
    {"name": "Val", "key": "val", "color": "#25e298"},
    {"name": "Test", "key": "test", "color": "#fcaf33"},
]

rows_data = [
    {
        "nameHtml": "<div>black-pawn</div>",
        "name": "black-pawn",
        "total": 1000,
        "disabled": False,
        "segments": {"train": 600, "val": 350, "test": 50},
    },
    {
        "name": "white-pawn",
        "total": 700,
        "disabled": False,
        "segments": {"train": 400, "val": 250, "test": 50},
    },
    {
        "name": "black-rook",
        "total": 450,
        "disabled": True,
        "segments": {"train": 300, "val": 150, "test": 0},
    },
    {
        "name": "white-rook",
        "total": 250,
        "disabled": False,
        "segments": {"train": 200, "val": 50, "test": 0},
    },
]

slider_data = {
    "black-pawn": [
        {
            "moreExamples": ["https://www.w3schools.com/howto/img_nature.jpg"],
            "preview": "https://www.w3schools.com/howto/img_nature.jpg",
        },
        {
            "moreExamples": ["https://www.quackit.com/pix/samples/18m.jpg"],
            "preview": "https://www.quackit.com/pix/samples/18m.jpg",
        },
    ],
    "white-pawn": [
        {
            "moreExamples": ["https://i.imgur.com/35pUPD2.jpg"],
            "preview": "https://i.imgur.com/35pUPD2.jpg",
        },
        {
            "moreExamples": ["https://i.imgur.com/fB2DBcM.jpeg"],
            "preview": "https://i.imgur.com/fB2DBcM.jpeg",
        },
    ],
    "black-rook": [
        {
            "moreExamples": ["https://i.imgur.com/OpSj3JE.jpg"],
            "preview": "https://i.imgur.com/OpSj3JE.jpg",
        },
        {
            "moreExamples": ["https://www.w3schools.com/howto/img_nature.jpg"],
            "preview": "https://www.w3schools.com/howto/img_nature.jpg",
        },
        {
            "moreExamples": ["https://www.quackit.com/pix/samples/18m.jpg"],
            "preview": "https://www.quackit.com/pix/samples/18m.jpg",
        },
    ],
    "white-rook": [
        {
            "moreExamples": ["https://i.imgur.com/35pUPD2.jpg"],
            "preview": "https://i.imgur.com/35pUPD2.jpg",
        },
        {
            "moreExamples": ["https://i.imgur.com/fB2DBcM.jpeg"],
            "preview": "https://i.imgur.com/fB2DBcM.jpeg",
        },
        {
            "moreExamples": ["https://i.imgur.com/OpSj3JE.jpg"],
            "preview": "https://i.imgur.com/OpSj3JE.jpg",
        },
    ],
}
```

![classbalance](https://user-images.githubusercontent.com/120389559/224935446-9dbda308-feda-4297-92dd-a1111f241af1.gif)

## Parameters

|     Parameters      |     Type     |                    Description                     |
| :-----------------: | :----------: | :------------------------------------------------: |
|    `max_height`     |    `int`     | Specifies the maximum height of the `ClassBalance` |
|    `selectable`     |    `bool`    |         Determines if rows can be selected         |
|    `collapsable`    |    `bool`    |  Determines whether a rows data can be collapsed   |
|  `clickable_name`   |    `bool`    |           Allows clicking on class names           |
| `clickable_segment` |    `bool`    |         Allows clicking on class segments          |
|     `max_value`     |    `int`     |        The maximum value of the input data         |
|     `segments`      | `List[Dict]` |           List of segments in the widget           |
|     `rows_data`     | `List[Dict]` |          List of rows data in the widget           |
|    `slider_data`    |    `Dict`    |    Dict containing `ClassBalance` slider images    |
|     `widget_id`     |    `str`     |                  ID of the widget                  |

### max_height

Specifies the maximum height of the `ClassBalance`.

**type:** `int`

**default value:** `300`

```python
class_balance = ClassBalance(
    max_value=max_value,
    segments=segments,
    rows_data=rows_data,
    slider_data=slider_data,
    max_height=600,
    collapsable=True
)
```

![max_height](https://user-images.githubusercontent.com/120389559/224936111-6b2d5840-f3b4-4ecc-816f-c40683e30bd0.gif)

### selectable

Determines whether a collapse button is displayed.

**type:** `bool`

**default value:** `True`

```python
class_balance = ClassBalance(
    max_value=max_value,
    segments=segments,
    rows_data=rows_data,
    slider_data=slider_data,
    selectable=False,
    collapsable=True
)
```

![selectable](https://user-images.githubusercontent.com/120389559/224936812-ba9e1bce-8cb7-4729-9dc6-c52b27da6e04.png)

### collapsable

Display the collapse button. The case `collapsable=True` has been shown above to show examples for changing the `max_height` parameter. So now an example will be shown for case `collapsable=False`.

**type:** `bool`

**default value:** `False`

```python
class_balance = ClassBalance(
    max_value=max_value,
    segments=segments,
    rows_data=rows_data,
    slider_data=slider_data,
    collapsable=False
)
```

![collapsable](https://user-images.githubusercontent.com/120389559/224938851-fdf5a506-b100-49f9-90d5-17252a6720b7.png)

### clickable_name

Allows clicking on class names.

**type:** `bool`

**default value:** `False`

```python
class_balance = ClassBalance(
    max_value=max_value,
    segments=segments,
    rows_data=rows_data,
    slider_data=slider_data,
    clickable_name=True,
)
```

![clickable_name](https://user-images.githubusercontent.com/120389559/224949506-f85fa772-e2c8-4de5-9079-919adc9cbf2c.png)

### clickable_segment

Allow clicking on class segments.

**type:** `bool`

**default value:** `False`

```python
class_balance = ClassBalance(
    max_value=max_value,
    segments=segments,
    rows_data=rows_data,
    slider_data=slider_data,
    clickable_segment=True,
)
```

## Methods and attributes

|                     Attributes and Methods                     | Description                                                   |
| :------------------------------------------------------------: | ------------------------------------------------------------- |
|                       `get_max_value()`                        | Returns the maximum value of `ClassBalance`                   |
|                  `set_max_value(value: int)`                   | Sets the maximum height of `ClassBalance`                     |
|                  `set_max_height(value: int)`                  | Sets the maximum height of `ClassBalance`                     |
|                       `get_max_height()`                       | Return `ClassBalance` max height.                             |
|                     `disable_selectable()`                     | Disables row selection in `ClassBalance`                      |
|                     `enable_selectable()`                      | Enables row selection in `ClassBalance`                       |
|                       `get_selectable()`                       | Returns the value of `selectable` in `ClassBalance`           |
|                    `disable_collapsable()`                     | Disables collapse button in `ClassBalance` rows               |
|                     `enable_collapsable()`                     | Enables collapse button in `ClassBalance` rows                |
|                      `get_collapsable()`                       | Returns the value of `collapsable` in `ClassBalance`          |
|                   `disable_clickable_name()`                   | Set `clickable_name` to `False`                               |
|                   `enable_clickable_name()`                    | Set `clickable_name` to `True`                                |
|                     `get_clickable_name()`                     | Return `ClassBalance` `clickable_name` value                  |
|                 `disable_clickable_segment()`                  | Set `clickable_segment` to `False`                            |
|                  `enable_clickable_segment()`                  | Set `clickable_segment` to `True`                             |
|                   `get_clickable_segment()`                    | Return `ClassBalance` `clickable_segment` value               |
|  `add_segments(segments: List[Dict] = [], send_changes=True)`  | Add new `segments` to now existing in `ClassBalance`          |
|                        `get_segments()`                        | Return `ClassBalance` `segments`                              |
|  `set_segments(segments: List[Dict] = [], send_changes=True)`  | Set new `segments` in `ClassBalance`                          |
| `add_rows_data(rows_data: List[Dict] = [], send_changes=True)` | Add new `rows_data` to now existing in `ClassBalance`         |
|                       `get_rows_data()`                        | Return `ClassBalance` `rows_data`                             |
| `set_rows_data(rows_data: List[Dict] = [], send_changes=True)` | Set new `rows_data` in `ClassBalance`                         |
|  `add_slider_data(slider_data: Dict = {}, send_changes=True)`  | Add new `slider_data` to now existing in `ClassBalance`       |
|                      `get_slider_data()`                       | Return `ClassBalance` `slider_data`                           |
|  `set_slider_data(slider_data: Dict = {}, send_changes=True)`  | Set new `slider_data` in `ClassBalance`                       |
|                     `get_selected_rows()`                      | Return list of `ClassBalance` clicked rows                    |
|                            `@click`                            | Decorator function to handle class name or rows segment click |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/misc/class_balance/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/misc/class_balance/src/main.py)

### Import libraries

```python
import os

from dotenv import load_dotenv
import supervisely as sly
from supervisely.app.widgets import ClassBalance, Text, Card, Container
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Example 1. A simple example of using `ClassBalance` widget.

**Prepare series for class balance**

```python
max_value = 1000
segments = [
    {"name": "Train", "key": "train", "color": "#1892f8"},
    {"name": "Val", "key": "val", "color": "#25e298"},
    {"name": "Test", "key": "test", "color": "#fcaf33"},
]

rows_data = [
    {
        "nameHtml": "<div>black-pawn</div>",
        "name": "black-pawn",
        "total": 1000,
        "disabled": False,
        "segments": {"train": 600, "val": 350, "test": 50},
    },
    {
        "name": "white-pawn",
        "total": 700,
        "disabled": False,
        "segments": {"train": 400, "val": 250, "test": 50},
    },
    {
        "name": "black-rook",
        "total": 450,
        "disabled": True,
        "segments": {"train": 300, "val": 150, "test": 0},
    },
    {
        "name": "white-rook",
        "total": 250,
        "disabled": False,
        "segments": {"train": 200, "val": 50, "test": 0},
    },
]

slider_data = {
    "black-pawn": [
        {
            "moreExamples": ["https://www.w3schools.com/howto/img_nature.jpg"],
            "preview": "https://www.w3schools.com/howto/img_nature.jpg",
        },
        {
            "moreExamples": ["https://www.quackit.com/pix/samples/18m.jpg"],
            "preview": "https://www.quackit.com/pix/samples/18m.jpg",
        },
    ],
    "white-pawn": [
        {
            "moreExamples": ["https://i.imgur.com/35pUPD2.jpg"],
            "preview": "https://i.imgur.com/35pUPD2.jpg",
        },
        {
            "moreExamples": ["https://i.imgur.com/fB2DBcM.jpeg"],
            "preview": "https://i.imgur.com/fB2DBcM.jpeg",
        },
    ],
    "black-rook": [
        {
            "moreExamples": ["https://i.imgur.com/OpSj3JE.jpg"],
            "preview": "https://i.imgur.com/OpSj3JE.jpg",
        },
        {
            "moreExamples": ["https://www.w3schools.com/howto/img_nature.jpg"],
            "preview": "https://www.w3schools.com/howto/img_nature.jpg",
        },
        {
            "moreExamples": ["https://www.quackit.com/pix/samples/18m.jpg"],
            "preview": "https://www.quackit.com/pix/samples/18m.jpg",
        },
    ],
    "white-rook": [
        {
            "moreExamples": ["https://i.imgur.com/35pUPD2.jpg"],
            "preview": "https://i.imgur.com/35pUPD2.jpg",
        },
        {
            "moreExamples": ["https://i.imgur.com/fB2DBcM.jpeg"],
            "preview": "https://i.imgur.com/fB2DBcM.jpeg",
        },
        {
            "moreExamples": ["https://i.imgur.com/OpSj3JE.jpg"],
            "preview": "https://i.imgur.com/OpSj3JE.jpg",
        },
    ],
}

new_data = {
    "segment": {"name": "Extra", "key": "extra", "color": "#611268"},
    "row_data": {
        "name": "extra-row",
        "total": 280,
        "disabled": False,
        "segments": {"train": 200, "val": 50, "test": 0, "extra": 30},
    },
    "slider_data": {
        "extra-row": [
            {
                "moreExamples": ["https://i.imgur.com/OpSj3JE.jpg"],
                "preview": "https://i.imgur.com/OpSj3JE.jpg",
            }
        ],
    },
}
```

**Initialize `ClassBalance`**

```python
class_balance_1 = ClassBalance(
    max_value=max_value,
    segments=segments,
    rows_data=rows_data,
    slider_data=slider_data,
    max_height=700,
    collapsable=True,
    clickable_name=True,
    clickable_segment=True,
)
```

**Create additional widgets**

```python
add_segment_btn = Button("Add segment")
add_row_btn = Button("Add row data")
add_slider_data_btn = Button("Add slider data")

buttons = Flexbox([add_segment_btn, add_row_btn, add_slider_data_btn], "horizontal")
text = Text()

card_1 = Card(
    title="Class Balance",
    content=Container([class_balance_1, buttons, text]),
)
```

**Add functions to control widgets from python code**

```python
@class_balance_1.click
def show_item(res):
    if res.get("segmentValue") is not None and res.get("segmentName") is not None:
        info = (
            f"Class {res['name']} contain {res['segmentValue']} tags with name {res['segmentName']}"
        )
        if res["segmentName"] == "Val":
            status = "success"
        elif res["segmentName"] == "Test":
            status = "warning"
        else:
            status = "info"
    else:
        info = f"Class {res['name']}"
        status = "text"

    text.set(text=info, status=status)


@add_segment_btn.click
def add_segment():
    new_segment = new_data["segment"]
    class_balance_1.add_segments([new_segment])


@add_row_btn.click
def add_row():
    row_data = new_data["row_data"]
    class_balance_1.add_rows_data([row_data])


@add_slider_data_btn.click
def add_slider_data():
    slider_data = new_data["slider_data"]
    class_balance_1.add_slider_data(slider_data)
```

### Example 2. Advanced using `ClassBalance` widget.

👍 In this example, we will iterate through sample dataset images from the Supervisely platform and crop them based on object classes to set in the image slider. Finally, we will calculate and collect statistics for each class and display the class balance information.

**Get variables from the environment**

```python
data_dir = sly.app.get_data_dir()
team_id = sly.env.team_id()
project_id = sly.env.project_id()
```

**Get `ProjectMeta` and `DatasetInfo`s from the server**

```python
project_meta = sly.ProjectMeta.from_json(api.project.get_meta(project_id))
datasets = api.dataset.get_list(project_id)
```

**Calculate and collect series for the `ClassBalance` widget**

```python
max_value = 0
rows_data = []
slider_data = defaultdict(list)

PADDINGS = {"top": "20px", "left": "20px", "bottom": "20px", "right": "20px"}
SAMPLE_RATE = 0.1 # ⬅️ change it
objclass_stats = defaultdict(lambda: defaultdict(lambda: 0))
crop_id = 0
for ds in datasets:
    sample_cnt = max(int(SAMPLE_RATE * ds.items_count), 1)
    image_infos = api.image.get_list(ds.id)
    random.shuffle(image_infos)
    image_infos = image_infos[:sample_cnt]
    image_ids = [image_info.id for image_info in image_infos]
    imame_nps = api.image.download_nps(ds.id, image_ids)
    anns_json = api.annotation.download_json_batch(ds.id, image_ids)
    anns = [sly.Annotation.from_json(json, project_meta) for json in anns_json]

    # collect infos and cropped images for image sliders
    for image_info, img, ann in zip(image_infos, imame_nps, anns):
        for objclass in project_meta.obj_classes:

            # crop current image to separated images which contain current class instance
            crops = sly.aug.instance_crop(img, ann, objclass.name, False, PADDINGS)
            objclass_stats[objclass.name]["total"] += len(crops)
            max_value = max(max_value, objclass_stats[objclass.name]["total"])

            for crop_img, crop_ann in crops:

                # draw annotations on image and upload result crop image to Team Files
                crop_ann.draw_pretty(crop_img)
                path = os.path.join(data_dir, f"{crop_id}-{image_info.name}")
                crop_id += 1
                sly.image.write(path, crop_img)
                file_info = api.file.upload(team_id, path, path)

                # collect cropped image url
                slider_data[objclass.name].append({"preview": file_info.full_storage_url})

        # count number of objects with each tag
        for label in ann.labels:
            for tag in label.tags:
                objclass_stats[label.obj_class.name][tag.name.lower()] += 1

# prepare rows data
for obj_class in project_meta.obj_classes:
    data = {}
    data["name"] = obj_class.name
    data["nameHtml"] = f"<div>{obj_class.name}</div>"
    data["total"] = objclass_stats[obj_class.name]["total"]
    data["disabled"] = False
    data["segments"] = {
        "train": objclass_stats[obj_class.name]["train"],
        "val": objclass_stats[obj_class.name]["val"],
        "test": objclass_stats[obj_class.name]["test"],
    }
    rows_data.append(data)
```

**Initialize `ClassBalance`**

```python
class_balance_2 = ClassBalance(
    max_value=max_value,
    segments=segments,
    rows_data=rows_data,
    slider_data=slider_data,
    max_height=700,
    collapsable=True,
    clickable_name=False,
    clickable_segment=False,
)
```

**Create `Card` widget**

```python
card_2 = Card(
    title="Class Balance",
    content=Container([class_balance_2]),
)
```

### Create app layout

Prepare a layout for the app using `Card` widget with the `content` parameter.

```python
layout = Container(widgets=[card_1, card_2])
```

### Create app using layout

Create an app object with the layout parameter.

```python
app = sly.Application(layout=layout)
```

<video preload="none" playsinline="" autoplay="autoplay" muted="muted" loop="loop" width="900" height="750">
    <source src="https://github.com/supervisely-ecosystem/ui-widgets-demos/assets/79905215/9b2357a4-c424-4042-abd5-0219982a7c98" type="video/webm">
    <source src="https://github.com/supervisely-ecosystem/ui-widgets-demos/assets/79905215/e2ba397d-bf64-4e2a-adbf-b6b4fa3dcbd4" type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>
