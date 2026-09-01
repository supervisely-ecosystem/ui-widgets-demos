# Launch this app with:
# misc.ctbupdates.select_tag.src.main:app

import os
import supervisely as sly
from supervisely.app.widgets import Card, Container, SelectTag
from dotenv import load_dotenv


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

tag_meta_cat = sly.TagMeta("cat", sly.TagValueType.NONE)
tag_meta_dog = sly.TagMeta("dog", sly.TagValueType.NONE)
tag_meta_horse = sly.TagMeta("horse", sly.TagValueType.NONE)
tag_meta_sheep = sly.TagMeta("sheep", sly.TagValueType.NONE)
tag_metas = [tag_meta_cat, tag_meta_dog, tag_meta_horse, tag_meta_sheep]
select_tag = SelectTag(tag_metas, multiple=True, show_add_new_tag=True)

container = Container([select_tag])
card = Card(title="Select Tag", content=container)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@select_tag.value_changed
def on_tag_value_changed(selected_tags: list[sly.TagMeta]):
    print(f"Selected tags: {[tag.name for tag in selected_tags]}")
    print(f"Selected tags count: {len(selected_tags)}")


@select_tag.tag_created
def on_tag_created(new_tag: sly.TagMeta):
    print(f"New tag created: {new_tag.name}, value type: {new_tag.value_type}")
