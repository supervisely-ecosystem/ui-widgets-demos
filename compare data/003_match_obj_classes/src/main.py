import os
import supervisely as sly
from supervisely.app.widgets import Card, Container, MatchObjClasses
from dotenv import load_dotenv


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

project_id_left = int(os.environ["modal.state.slyProjectId_left"])
meta_json_left = api.project.get_meta(project_id_left)
project_meta_left = sly.ProjectMeta.from_json(meta_json_left)
left_classes = project_meta_left.obj_classes

project_id_right = int(os.environ["modal.state.slyProjectId_right"])
meta_json_right = api.project.get_meta(project_id_right)
project_meta_right = sly.ProjectMeta.from_json(meta_json_right)
right_classes = project_meta_right._obj_classes


match = MatchObjClasses(
    left_collection=left_classes, right_collection=right_classes, suffix="erity"
)


card = Card(
    title="Match Classes",
    content=match,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
