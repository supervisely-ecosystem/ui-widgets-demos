import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, Flexbox, ImagePairSequence, Text


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()


project_id = sly.env.project_id()
dataset_id = sly.env.dataset_id()
project_meta = sly.ProjectMeta.from_json(data=api.project.get_meta(id=project_id))


data_dir = sly.app.get_data_dir()
static_dir = os.path.join(data_dir, "static")
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

# create buttons to add predictions
left_btn = Button(text="add 1 prediction to left")
right_btn = Button(text="add 1 prediction to right")
left_three_btn = Button(text="add 3 predictions to left")
right_three_btn = Button(text="add 3 predictions to right")
pair_btn = Button(text="add 1 pair")
pairs_batch_btn = Button(text="add 3 pairs")
clean_btn = Button(text="clean up")

btn_container = Flexbox(
    [left_btn, right_btn, left_three_btn, right_three_btn, pair_btn, pairs_batch_btn, clean_btn]
)
image_pair_sequence = ImagePairSequence()
text = Text()

card = Card(
    title="Image Pair Sequence",
    content=Container([image_pair_sequence]),
)

layout = Container(widgets=[btn_container, card, text])

app = sly.Application(layout=layout, static_dir=static_dir)


# get all image infos in dataset
used_names = set()
images_infos = api.image.get_list(dataset_id=dataset_id)
images_infos = sorted(images_infos, key=lambda image_info: image_info.name)
image_ids = [image_info.id for image_info in images_infos]
urls = [img.full_storage_url for img in images_infos]
paths = [
    os.path.join(static_dir, sly.generate_free_name(used_names, image_info.name, with_ext=True))
    for image_info in images_infos
]
static_paths = [os.path.join("static", os.path.basename(path)) for path in paths]

api.image.download_paths(dataset_id, image_ids, paths)


# get annotations for all images
anns_json = api.annotation.download_json_batch(dataset_id=dataset_id, image_ids=image_ids)
anns = [sly.Annotation.from_json(ann_json, project_meta) for ann_json in anns_json]

left_paths_generator = (path for path in static_paths)
right_paths_generator = (path for path in static_paths)
left_anns_generator = (ann for ann in anns)
right_anns_generator = (ann for ann in anns)


left_num = 0
right_num = 0


def get_next_prediction(side):
    global left_num, right_num
    path, ann, title = None, None, None
    url_gen = left_paths_generator if side == "left" else right_paths_generator
    ann_gen = left_anns_generator if side == "left" else right_anns_generator
    try:
        path = next(url_gen)
        ann = next(ann_gen)
        if side == "left":
            title = f"Predictions {left_num}"
            left_num += 1
        else:
            title = f"Predictions {right_num}"
            right_num += 1
    except StopIteration:
        sly.logger.info("No more predictions.")
        text.set(text="No more predictions.", status="info")
    finally:
        return path, ann, title


@pair_btn.click
def pair_btn_click_handler():
    left = get_next_prediction("left")
    right = get_next_prediction("right")
    if left[0] is not None and right[0] is not None:
        image_pair_sequence.append_pair(left=left, right=right)


@pairs_batch_btn.click
def pairs_batch_btn_click_handler():
    lefts = []
    rights = []

    for _ in range(3):
        left = get_next_prediction("left")
        right = get_next_prediction("right")

        if left[0] is not None and right[0] is not None:
            lefts.append(left)
            rights.append(right)

    if len(lefts) > 0 and len(rights) > 0:
        image_pair_sequence.extend_pairs(lefts, rights)


@left_btn.click
def left_btn_click_handler():
    path, ann, title = get_next_prediction("left")
    if path is not None:
        image_pair_sequence.append_left(path, ann, title)


@right_btn.click
def right_btn_click_handler():
    path, ann, title = get_next_prediction("right")
    if path is not None:
        image_pair_sequence.append_right(path, ann, title)


@left_three_btn.click
def left_three_btn_click_handler():
    data = []

    for _ in range(3):
        left = get_next_prediction("left")

        if left[0] is not None:
            data.append(left)

    if len(data) > 0:
        paths, anns, titles = zip(*data)
        image_pair_sequence.extend_left(paths=paths, anns=anns, titles=titles)


@right_three_btn.click
def right_three_btn_click_handler():
    data = []

    for _ in range(3):
        right = get_next_prediction("right")

        if right[0] is not None:
            data.append(right)

    if len(data) > 0:
        paths, anns, titles = zip(*data)
        image_pair_sequence.extend_right(paths=paths, anns=anns, titles=titles)


@clean_btn.click
def clean_btn_click_handler():
    image_pair_sequence.clean_up()
