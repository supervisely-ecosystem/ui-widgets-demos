import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Image, SelectString


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

dataset_id = sly.env.dataset_id()

images = api.image.get_list(dataset_id=dataset_id)

select_string = SelectString(
    values=[img.name for img in images],
    items_links=[img.full_storage_url for img in images],
)

image = Image()

card = Card(
    title="Select string",
    content=Container(
        [select_string, image],
        direction="horizontal",
        fractions=[1, 1],
    ),
)

layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@select_string.value_changed
def display_select_string(value):
    if value is not None:
        img = api.image.get_info_by_name(dataset_id, value)
        image.set(url=img.full_storage_url)
