import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, NotificationBox, SelectTag

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# Create some initial tags with different value types
tag_weather = sly.TagMeta("weather", sly.TagValueType.ANY_STRING)
tag_count = sly.TagMeta("count", sly.TagValueType.ANY_NUMBER)

colors = ["red", "green", "blue"]
tag_color = sly.TagMeta("color", sly.TagValueType.ONEOF_STRING, possible_values=colors)

tag_verified = sly.TagMeta("verified", sly.TagValueType.NONE)

tags = [
    tag_weather,
    tag_count,
    tag_color,
    tag_verified,
]

# Initialize SelectTag widget
select_tag = SelectTag(
    tags=tags,
    filterable=True,
    placeholder="Select a tag",
    multiple=True,
    show_add_new_tag=True,
)

notification_box = NotificationBox()

card = Card(
    title="Select Tag",
    content=Container(widgets=[select_tag, notification_box]),
)

layout = Container(widgets=[card])

app = sly.Application(layout=layout)


@select_tag.value_changed
def on_tag_selected(selected_tags):
    if isinstance(selected_tags, list):
        tag_names = [tag.name for tag in selected_tags]
        notification_box.set(
            title="Tags selected",
            description=f"Selected tags: {', '.join(tag_names)}",
        )
    else:
        notification_box.set(
            title="Tag selected",
            description=f"Selected tag: {selected_tags.name}",
        )


@select_tag.tag_created
def on_tag_created(new_tag: sly.TagMeta):
    notification_box.set(
        title="New tag created",
        description=f"You have created a new tag: {new_tag.name} (type: {new_tag.value_type})",
    )
