import os
import supervisely as sly
from supervisely.app.widgets import Card, Container, MatchTagMetas
from dotenv import load_dotenv


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

project_id_left = 17208
meta_json_left = api.project.get_meta(project_id_left)
project_meta_left = sly.ProjectMeta.from_json(meta_json_left)
tag_metas_left = project_meta_left.tag_metas

project_id_right = 17752
meta_json_right = api.project.get_meta(project_id_right)
project_meta_right = sly.ProjectMeta.from_json(meta_json_right)
tag_metas_right = project_meta_right.tag_metas


match = MatchTagMetas(
    left_collection=tag_metas_left,
    right_collection=tag_metas_right,
    left_name="left tags",
    right_name="right tags",
)


card = Card(
    title="Match Tags",
    content=match,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)

print(match.get_stat())