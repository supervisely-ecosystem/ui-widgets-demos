import os
import supervisely as sly
from supervisely.app.widgets import Card, Container, InputTag
from dotenv import load_dotenv


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()


tag_meta = sly.TagMeta(
    "my_tag", sly.TagValueType.ONEOF_STRING, possible_values=["value1", "value2", "value3"]
)

input_tag = InputTag(tag_meta)


card = Card(
    title="Input Tag",
    content=input_tag,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
