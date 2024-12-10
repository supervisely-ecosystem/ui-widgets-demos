import os
import supervisely as sly
from supervisely.app.widgets import Card, Container, InputTag
from dotenv import load_dotenv


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()


tag_meta_none = sly.TagMeta("none", sly.TagValueType.NONE)
tag_meta_string = sly.TagMeta("any_string", sly.TagValueType.ANY_STRING)
tag_meta_num = sly.TagMeta("any_number", sly.TagValueType.ANY_NUMBER)
tag_meta_onf = sly.TagMeta(
    "one of", sly.TagValueType.ONEOF_STRING, possible_values=["value1", "value2", "value3"]
)

input_tag_none = InputTag(tag_meta_none, hide_switch=False)
input_tag_string = InputTag(tag_meta_string, hide_switch=True)
input_tag_num = InputTag(tag_meta_num, hide_switch=False)
input_tag_onf = InputTag(tag_meta_onf, hide_switch=True)

container = Container([input_tag_none, input_tag_string, input_tag_num, input_tag_onf])

card = Card(
    title="Input Tag",
    content=container,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
