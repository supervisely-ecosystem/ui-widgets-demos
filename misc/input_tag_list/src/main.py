import os
import supervisely as sly
from supervisely.app.widgets import Card, Container, Button, Text, InputTagList
from dotenv import load_dotenv


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# Create different types of tag metas
tag_meta_none = sly.TagMeta("none_tag", sly.TagValueType.NONE)
tag_meta_string = sly.TagMeta("string_tag", sly.TagValueType.ANY_STRING)
tag_meta_num = sly.TagMeta("number_tag", sly.TagValueType.ANY_NUMBER)
tag_meta_oneof = sly.TagMeta(
    "oneof_tag", sly.TagValueType.ONEOF_STRING, possible_values=["option1", "option2", "option3"]
)

# Additional tag metas for demonstration
tag_meta_quality = sly.TagMeta(
    "quality", sly.TagValueType.ONEOF_STRING, possible_values=["high", "medium", "low"]
)
tag_meta_category = sly.TagMeta("category", sly.TagValueType.ANY_STRING)
tag_meta_confidence = sly.TagMeta("confidence", sly.TagValueType.ANY_NUMBER)

# Create a list of tag metas
tag_metas = [
    tag_meta_none,
    tag_meta_string,
    tag_meta_num,
    tag_meta_oneof,
    tag_meta_quality,
    tag_meta_category,
    tag_meta_confidence,
]

# Create InputTagList widget
input_tag_list = InputTagList(tag_metas=tag_metas, max_width=400, max_height=200)

# Create buttons for demonstration
btn_select_all = Button("Select All")
btn_deselect_all = Button("Deselect All")
btn_select_specific = Button("Select random")
btn_get_selected = Button("Get Selected Tags")
btn_set_values = Button("Set Sample Values")

# Text widget to display results
result_text = Text("Select tags and click buttons to see the results", status="info")


# Event handlers
@btn_select_all.click
def select_all():
    input_tag_list.select_all()
    result_text.text = "All tags selected"


@btn_deselect_all.click
def deselect_all():
    input_tag_list.deselect_all()
    result_text.text = "All tags deselected"


@btn_select_specific.click
def select_specific():
    input_tag_list.select(["quality", "category"])
    result_text.text = "Selected 'quality' and 'category' tags"


@btn_get_selected.click
def get_selected():
    selected_tags = input_tag_list.get_selected_tags()

    if selected_tags:
        result_info = f"Selected {len(selected_tags)} tags:\n"
        for tag in selected_tags:
            result_info += f"- {tag.meta.name}: {tag.value} (type: {tag.meta.value_type})\n"
    else:
        result_info = "No tags selected"

    result_text.text = result_info


@btn_set_values.click
def set_sample_values():
    sample_values = {
        "string_tag": "sample text",
        "number_tag": 42,
        "oneof_tag": "option2",
        "quality": "high",
        "category": "demo",
        "confidence": 0.95,
    }
    input_tag_list.set_values(sample_values)
    result_text.text = "Sample values set for all tags"


# Selection change handler
@input_tag_list.selection_changed
def on_selection_changed(selected_tag_metas):
    if selected_tag_metas:
        names = [tm.name for tm in selected_tag_metas]
        result_text.text = f"Selection changed: {', '.join(names)}"
    else:
        result_text.text = "No tags selected"


# Create layout
buttons_container = Container(
    [btn_select_all, btn_deselect_all, btn_select_specific, btn_get_selected, btn_set_values],
    direction="vertical",
    gap=10,
)

main_container = Container(
    [Container([input_tag_list, result_text], direction="vertical", gap=20), buttons_container],
    direction="horizontal",
    gap=20,
)

card = Card(
    title="InputTagList Widget Demo",
    content=main_container,
    description="This demo shows how to use the InputTagList widget with different tag types and operations.",
)

layout = Container(widgets=[card])
app = sly.Application(layout=layout)
