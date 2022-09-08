import os
from dotenv import load_dotenv
import supervisely as sly


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
app = sly.Application(
    templates_dir=os.path.join(os.getcwd(), "010_compare_images", "templates")
)


# 1. Compare images from the same project
# get project info from server
project_id = int(os.environ["modal.state.slyProjectId"])
project = api.project.get_info_by_id(project_id)
meta_json = api.project.get_meta(id=project_id)
meta = sly.ProjectMeta.from_json(data=meta_json)

# get left image and ann
left_image_id = int(os.environ["modal.state.slyImageIdLeft"])
left_image = api.image.get_info_by_id(id=left_image_id)
left_ann_json = api.annotation.download_json(image_id=left_image_id)
left_ann = sly.Annotation.from_json(data=left_ann_json, project_meta=meta)

# get right image and ann
right_image_id = int(os.environ["modal.state.slyImageIdRight"])
right_image = api.image.get_info_by_id(id=right_image_id)
right_ann_json = api.annotation.download_json(image_id=right_image_id)
right_ann = sly.Annotation.from_json(data=right_ann_json, project_meta=meta)

# create Compare Images widget and set images
compare_images = sly.app.widgets.CompareImages()
compare_images.set_left(
    title=left_image.name, image_url=left_image.preview_url, ann=left_ann
)
compare_images.set_right(
    title=right_image.name, image_url=right_image.preview_url, ann=right_ann
)


# # 2. Compare images from different projects
# # get project info for left image from server
# left_image_project_id = int(os.environ["modal.state.slyProjectIdLeft"])
# left_image_project = api.project.get_info_by_id(left_image_project_id)
# left_image_meta_json = api.project.get_meta(id=left_image_project_id)
# left_image_meta = sly.ProjectMeta.from_json(data=left_image_meta_json)

# # get left image and ann
# image_id = int(os.environ["modal.state.slyImageIdLeft"])
# left_image = api.image.get_info_by_id(id=left_image_id)
# left_ann_json = api.annotation.download_json(image_id=left_image_id)
# left_ann = sly.Annotation.from_json(data=left_ann_json, project_meta=left_image_meta)

# # get project info for right image from server
# right_image_project_id = int(os.environ["modal.state.slyProjectIdRight"])
# right_image_project = api.project.get_info_by_id(right_image_project_id)
# right_image_meta_json = api.project.get_meta(id=right_image_project_id)
# right_image_meta = sly.ProjectMeta.from_json(data=right_image_meta_json)

# # get right image and ann
# image_id = int(os.environ["modal.state.slyImageIdRight"])
# right_image = api.image.get_info_by_id(id=right_image_id)
# right_ann_json = api.annotation.download_json(image_id=right_image_id)
# right_ann = sly.Annotation.from_json(data=right_ann_json, project_meta=right_image_meta)

# # create Compare Images widget and set images
# compare_images = sly.app.widgets.CompareImages()
# compare_images.set_left(
#     title=left_image.name, image_url=left_image.preview_url, ann=left_ann
# )
# compare_images.set_right(
#     title=right_image.name, image_url=right_image.preview_url, ann=right_ann
# )
