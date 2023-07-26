import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, Flexbox, PredictionsGallery

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

project_id = sly.env.project_id()
dataset_id = sly.env.dataset_id()
project_meta = sly.ProjectMeta.from_json(data=api.project.get_meta(id=project_id))

# create buttons to add predictions
add_three_btn = Button(text="add 3 predictions")
add_one_btn = Button(text="add 1 prediction")
btn_container = Flexbox([add_three_btn, add_one_btn])

# get all image infos in dataset
images_infos = api.image.get_list(dataset_id=dataset_id)
images_infos = sorted(images_infos, key=lambda image_info: image_info.name)
image_ids = [image_info.id for image_info in images_infos]


# get annotations for all images
anns_json = api.annotation.download_json_batch(dataset_id=dataset_id, image_ids=image_ids)
anns = [sly.Annotation.from_json(ann_json, project_meta) for ann_json in anns_json]
anns_generator = (ann for ann in anns[1:])


predictions_gallery = PredictionsGallery()

predictions_gallery.set_ground_truth(
    image_url=images_infos[0].full_storage_url,
    annotation=anns[0],
    title="Ground truth",
)


card = Card(
    title="Predictions Sequence",
    content=Container([predictions_gallery, btn_container]),
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)

prediction_num = 0

@add_three_btn.click
def set_btn_click_handler():
    global prediction_num
    predictions = []
    titles = []

    def _get_next_prediction(predictions, prediction_num):
        try:
            next_ann = next(anns_generator)
            predictions.append(next_ann)
            prediction_num += 1
            titles.append(f"Predictions {prediction_num} [treshold=0.5]")
        except StopIteration:
            sly.logger.info("No more predictions.")
        finally:
            return prediction_num

    prediction_num = _get_next_prediction(predictions, prediction_num)
    prediction_num = _get_next_prediction(predictions, prediction_num)
    prediction_num = _get_next_prediction(predictions, prediction_num)

    if len(predictions) > 0:
        predictions_gallery.add_predictions(annotations=predictions, titles=titles)


@add_one_btn.click
def set_btn_click_handler():
    global prediction_num
    try:
        next_ann = next(anns_generator)
        prediction_num += 1
        predictions_gallery.add_prediction(next_ann, f"Predictions {prediction_num} [treshold=0.5]")
    except StopIteration:
        sly.logger.info("No more predictions.")
