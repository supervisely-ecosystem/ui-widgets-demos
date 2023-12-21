import os
import supervisely as sly
from supervisely.app.widgets import Card, Container, TagsListSelector, Text, NotificationBox
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

notification_box = NotificationBox(title="No tags", description="Provide tags to the widget.")
tags_list_selector = TagsListSelector(tag_metas, multiple=True, empty_notification=notification_box)
selected_tags_cnt = Text(f"Selected Tags: 0 / {len(tag_metas)}")

container = Container(widgets=[selected_tags_cnt, tags_list_selector])

card = Card(
    title="Tags List Selector",
    content=container,
)

layout = card
app = sly.Application(layout=layout)


@tags_list_selector.selection_changed
def on_selection_changed(selected_tags):
    selected_tags_cnt.set(f"Selected Tags: {len(selected_tags)} / {len(tag_metas)}", "text")
