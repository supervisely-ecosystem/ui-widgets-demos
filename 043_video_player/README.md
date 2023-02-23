# Video Player

## Introduction

In this tutorial you will learn how to use `VideoPlayer` widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/videoplayer)

## Function signature

```python
VideoPlayer(url=None, mime_type="video/mp4", widget_id=None)
```

![default](https://user-images.githubusercontent.com/120389559/218763470-5c25c9ca-39c5-462d-ab90-618f1f5bb765.gif)

## Parameters

| Parameters  | Type  |                 Description                  |
| :---------: | :---: | :------------------------------------------: |
|    `url`    | `str` | Video url or local path to video on the host |
| `mime_type` | `str` |                  Video type                  |
| `widget_id` | `str` |               Id of the widget               |

### url

Video url or local path to video on the host. Determines the video to be displayed on widget.

**type:** `str`

**default value:** `None`

### mime_type

Determines video type.

**type:** `str`

**default value:** `video/mp4`

ID of the widget.

**type:** `str`

**default value:** `None`

## Methods and attributes

|               Attributes and Methods                | Description                               |
| :-------------------------------------------------: | ----------------------------------------- |
| `set_video(url: str, mime_type: str = "video/mp4")` | Set video in `VideoPlayer` widget by url. |
|                      `play()`                       | Start video to play.                      |
|                      `pause()`                      | Stop video playback.                      |
|              `get_current_timestamp()`              | Return current video playing step.        |
|         `set_current_timestamp(value: int)`         | Set current video playing step.           |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/043_video_player/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/043_video_player/src/main.py)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, Flexbox, InputNumber, VideoPlayer
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Initialize `VideoPlayers` we will use in UI

```python
video_url = "https://user-images.githubusercontent.com/79905215/210067166-e5531dae-d090-436e-bb3b-f053e2e831eb.mp4"
video_type = "video/mp4"
video_meta = sly.video.get_info(video_url)

video1 = VideoPlayer(url=video_url, mime_type=video_type)
video2 = VideoPlayer()
video2.set_video(url=video_url, mime_type=video_type)
```

### Initialize buttons to control widget

```python
play_btn = Button(text="Play", button_size="mini", icon="zmdi zmdi-play")
pause_btn = Button(text="Pause", button_size="mini", icon="zmdi zmdi-pause")

get_time_btn = Button(text="Get timestamp", button_size="mini")
input_time = InputNumber(
    value=0,
    min=0,
    max=round(video_meta["duration"], 1),
    step=0.1,
)
set_time_btn = Button(text="Set timestamp", button_size="mini")
# create containers for control form
controls_container = Flexbox(
    widgets=[play_btn, pause_btn, get_time_btn, input_time, set_time_btn],
    center_content=True,
)
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card1 = Card(
    title="Video player",
    content=video1,
)
card2 = Card(
    title="Controls - operations from python code",
    content=Container(widgets=[video2, controls_container]),
)

layout = Container(widgets=[card1, card2], direction="horizontal", fractions=[1, 1])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```

### Handle button clicks

Use the decorator as shown below to handle button click. We have 4 buttons: to play video, to stop video, to get timestamp, to set timestamp.

```python
# start playing video
@play_btn.click
def play():
    video2.play()


# pause video
@pause_btn.click
def pause():
    video2.pause()


# get current timestamp
@get_time_btn.click
def get_current_timestamp():
    input_time.value = video2.get_current_timestamp()


# set current timestamp
@set_time_btn.click
def set_current_timestamp():
    time_to_set = input_time.get_value()
    video2.set_current_timestamp(time_to_set)

```

![layout](https://user-images.githubusercontent.com/120389559/218772680-b5c85128-d325-40a7-ae0a-0bf5a70a9d47.gif)
