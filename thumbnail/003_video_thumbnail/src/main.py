import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, VideoThumbnail

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# get video info from server
video_id = int(os.environ["modal.state.slyVideoId"])
video_info = api.video.get_info_by_id(id=video_id)

# initialize widgets we will use in UI
video_thumbnail = VideoThumbnail(info=video_info)
card = Card(
    title="Video Thumbnail",
    content=Container(widgets=[video_thumbnail]),
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
