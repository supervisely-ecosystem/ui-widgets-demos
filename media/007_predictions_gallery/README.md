# Predictions Gallery

## Introduction

The **`PredictionsGallery`** widget is a custom widget in Supervisely designed for displaying ground truth and predictions in a grid format. It allows users to navigate through multiple pages of predictions and provides zooming functionality, making it convenient for visualizing annotated image results.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/widgets/media/predictionsseqience)

## Function signature

```python
PredictionsGallery(
    slider_title="epochs",
    enable_zoom=False,
    opacity=0.4,
    widget_id=None,
)
```

<p align="center">
  <img src="https://github.com/supervisely/developer-portal/assets/79905215/1f1adfcd-4fce-489c-bf4f-d8acbbc5a1be" alt="PredictionsGallery" />
</p>

## Parameters

|   Parameters   |       Type        |               Description                |
| :------------: | :---------------: | :--------------------------------------: |
| `slider_title` |  `Optional[str]`  | Measurement units in the widget controls |
| `enable_zoom`  | `Optional[bool]`  |   Enable zoom on `PredictionsGallery`    |
|   `opacity`    | `Optional[float]` |             Objects opacity              |
|  `widget_id`   |  `Optional[str]`  |             Id of the widget             |

### slider_title

Measurement units in the widget controls.

**type:** `Optional[str]`

**default value:** `epochs`

```python
predictions_gallery = PredictionsGallery(slider_title="predictions")
```

<p align="center">
  <img src="https://github.com/supervisely/developer-portal/assets/79905215/88ec3b86-4916-4904-96e2-44f38822fc0b" alt="PredictionsGallery title" />
</p>

### enable_zoom

Enable zoom on `PredictionsGallery`.

**type:** `Optional[bool]`

**default value:** `False`

```python
predictions_gallery = PredictionsGallery(enable_zoom=True)
```

<p align="center">
  <img src="https://github.com/supervisely/developer-portal/assets/79905215/6c7ea31c-c9cd-4931-a80c-d246f620923d" alt="PredictionsGallery zoom" />
</p>

### opacity

Objects opacity.

**type:** `Optional[float]`

**default value:** `0.4`

```python
predictions_gallery = PredictionsGallery(opacity=0.8)
```

![opacity](https://github.com/supervisely/developer-portal/assets/79905215/27e1ad16-2073-40bf-abf7-eed6ee7bbc41)

### widget_id

ID of the widget.

**type:** `str`

**default value:** `None`

## Methods and attributes

|                              Attributes and Methods                               | Description                                                                             |
| :-------------------------------------------------------------------------------: | --------------------------------------------------------------------------------------- |
|    `set_ground_truth(image_url: str, annotation: sly.Annotation, title: str)`     | Sets the ground truth image and annotation to display in the `PredictionsGallery`.      |
| `add_predictions(annotations: List[sly.Annotation], titles: Optional[List[str]])` | Adds a list of predictions with their corresponding titles to the `PredictionsGallery`. |
|             `add_prediction(annotation: sly.Annotation, title: str)`              | Adds a single prediction with an optional title to the `PredictionsGallery`.            |
|                                    `disable()`                                    | Disables the `PredictionsGallery` widget controls.                                      |
|                                    `enable()`                                     | Enables the `PredictionsGallery` widget controls.                                       |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/media/007_predictions_gallery/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/media/007_predictions_gallery/src/main.py)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, Flexbox, PredictionsGallery
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Get project ID and dataset ID from environment variables

```python
project_id = sly.env.project_id()
dataset_id = sly.env.dataset_id()
project_meta = sly.ProjectMeta.from_json(data=api.project.get_meta(id=project_id))
```

### Create `Button` widgets for adding predictions

```python
add_three_btn = Button(text="add 3 predictions")
add_one_btn = Button(text="add 1 prediction")
btn_container = Flexbox([add_three_btn, add_one_btn])
```

### Prepare images and annotations for `PredictionsGallery` widget

```python
# get all image infos in dataset
images_infos = api.image.get_list(dataset_id=dataset_id)
images_infos = sorted(images_infos, key=lambda image_info: image_info.name)
image_ids = [image_info.id for image_info in images_infos]


# get annotations for all images
anns_json = api.annotation.download_json_batch(dataset_id=dataset_id, image_ids=image_ids)
anns = [sly.Annotation.from_json(ann_json, project_meta) for ann_json in anns_json]
anns_generator = (ann for ann in anns[1:])
```

### Initialize `PredictionsGallery` widget we will use in UI

```python
predictions_gallery = PredictionsGallery()
```

### Set ground truth image and annotation

```python
predictions_gallery.set_ground_truth(
    image_url=images_infos[0].full_storage_url,
    annotation=anns[0],
    title="Ground truth",
)
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card = Card(
    title="Predictions Sequence",
    content=Container([predictions_gallery, btn_container]),
)
layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```

### Add function to add predictions

```python
prediction_num = 0

@add_three_btn.click
def set_btn_click_handler():
    global prediction_num
    predictions = []
    titles = []

    def _get_next_prediction(predictions, prediction_num):
        try:
            next_ann = next(anns_generator)
            predictions.append(next_ann)
            prediction_num += 1
            titles.append(f"Predictions {prediction_num} [treshold=0.5]")
        except StopIteration:
            sly.logger.info("No more predictions.")
        finally:
            return prediction_num

    prediction_num = _get_next_prediction(predictions, prediction_num)
    prediction_num = _get_next_prediction(predictions, prediction_num)
    prediction_num = _get_next_prediction(predictions, prediction_num)

    if len(predictions) > 0:
        predictions_gallery.add_predictions(annotations=predictions, titles=titles)


@add_one_btn.click
def set_btn_click_handler():
    global prediction_num
    try:
        next_ann = next(anns_generator)
        prediction_num += 1
        predictions_gallery.add_prediction(next_ann, f"Predictions {prediction_num} [treshold=0.5]")
    except StopIteration:
        sly.logger.info("No more predictions.")
```


### Run app

<p align="center">
  <img src="https://github.com/supervisely/developer-portal/assets/79905215/63e81630-84d9-47a9-bb44-50372484d619" alt="PredictionsGallery app" />
</p>
