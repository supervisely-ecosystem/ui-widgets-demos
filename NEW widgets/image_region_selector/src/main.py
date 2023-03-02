import os
from random import choice

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, ImageRegionSelector, Checkbox

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api.from_env()

dataset_id = 55222
image_info_list = api.image.get_list(dataset_id)
smart_tool = ImageRegionSelector(image_info=image_info_list[0])

@smart_tool.bbox_changed
def bbox_updated(new_scaled_bbox):
    sly.logger.info(f"new_scaled_bbox: {new_scaled_bbox}")

button = Button('New random image')
@button.click
def print():
    smart_tool.image_update(image_info=image_info_list[5])
    
card = Card(
    title="Title",
    content=Container(widgets=[smart_tool, button]),
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)