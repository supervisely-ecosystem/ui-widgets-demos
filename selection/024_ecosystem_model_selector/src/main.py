import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Text
from ecosystem_model_selector import EcosystemModelSelector


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))
api = sly.Api()

model_selector = EcosystemModelSelector(api=api)

selection_changed_info = Text(status="info")
selection_changed_info.hide()


@model_selector.table.value_changed
def model_selected(selected_row):
    if selected_row:
        try:
            selected_model = model_selector.get_selected()
            text = f"Selected model: {selected_model['name']} ({selected_model['framework']})"
            selection_changed_info.text = text
            selection_changed_info.show()
        except Exception as e:
            selection_changed_info.text = f"Error getting selected model: {str(e)}"
            selection_changed_info.show()
    else:
        selection_changed_info.hide()


card = Card(
    title="EcosystemModelSelector",
    content=Container(widgets=[selection_changed_info, model_selector]),
)

layout = Container(widgets=[card])
app = sly.Application(layout=layout)
