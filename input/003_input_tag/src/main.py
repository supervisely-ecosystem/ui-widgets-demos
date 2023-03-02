import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, InputTag, Text

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

project_id = sly.env.project_id()
dataset_id = sly.env.dataset_id()

meta_json = api.project.get_meta(project_id)
project_meta = sly.ProjectMeta.from_json(meta_json)
tag_metas = project_meta.tag_metas

# initialize widgets we will use in UI
tag_inputs = [InputTag(t) for t in tag_metas]

toggle_btn = Button("Toggle")
value_text = Text()

tag_inputs_container = Container(widgets=tag_inputs)

container = Container(widgets=[tag_inputs_container, toggle_btn, value_text])

card = Card(title="Tag inputs", content=container)

layout = Container(widgets=[card])
app = sly.Application(layout=layout)

for tag_input in tag_inputs:

    @tag_input.value_changed
    def show_message(value):
        value_text.text = value


@toggle_btn.click
def toggle_tag_inputs():
    for tag_input in tag_inputs:
        if tag_input.is_active():
            tag_input.deactivate()
        else:
            tag_input.activate()
