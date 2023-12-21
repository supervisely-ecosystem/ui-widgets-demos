import os
import supervisely as sly
from supervisely.app.widgets import (
    Card,
    Container,
    TagsListPreview,
    TagsListSelector,
    Text,
)
from dotenv import load_dotenv


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

cat_tag_meta = sly.TagMeta("cat", sly.TagValueType.NONE)
dog_tag_meta = sly.TagMeta("dog", sly.TagValueType.ANY_NUMBER)
horse_tag_meta = sly.TagMeta("horse", sly.TagValueType.ANY_STRING)
cow_tag_meta = sly.TagMeta("cow", sly.TagValueType.ONEOF_STRING, possible_values=["moo", "mooo"])
zebra_tag_meta = sly.TagMeta("zebra", sly.TagValueType.NONE)
tag_metas = [
    cat_tag_meta,
    dog_tag_meta,
    horse_tag_meta,
    cow_tag_meta,
    zebra_tag_meta,
]

tags_list_selector = TagsListSelector(tag_metas, multiple=True)

empty_text = Text("No tags selected", "text")
tags_list_preview = TagsListPreview(empty_text=empty_text)
preview_text = Text(f"Selected Tags: 0 / {len(tag_metas)}", "text")
preview_container = Container([preview_text, tags_list_preview])

container = Container(widgets=[tags_list_selector, preview_container])

card = Card(
    title="Tags List Preview",
    content=container,
)

layout = card
app = sly.Application(layout=layout)


@tags_list_selector.selection_changed
def on_selection_changed(selected_tags):
    preview_text.set(f"Selected Tags: {len(selected_tags)} / {len(tag_metas)}", "text")
    tags_list_preview.set(selected_tags)
