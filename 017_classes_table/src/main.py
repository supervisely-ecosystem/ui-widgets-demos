import os
from dotenv import load_dotenv
import supervisely as sly
from supervisely.project.project_meta import ProjectMeta

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
app = sly.Application(
    templates_dir=os.path.join(os.getcwd(), "017_classes_table", "templates")
)
project_id = int(os.environ["modal.state.slyProjectId"])
class_table = sly.app.widgets.ClassesTable(project_id=project_id)
label = sly.app.widgets.Text("")


@class_table.value_changed
def class_table_value_changed(selected_classes):
    label.text = f"Selected classes: {', '.join(selected_classes)}"
