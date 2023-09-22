import os
from collections import defaultdict

from dotenv import load_dotenv
import supervisely as sly
from supervisely.app.widgets import Button, Card, ClassBalance, Container, Flexbox, Text
from supervisely.imaging.color import rgb2hex
from tqdm import tqdm

# for convenient debug, has no effect in production
if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))


api = sly.Api()

############## Simple example how to use ClassBalance widget ##################

# prepare data for ClassBalance widget
max_value = 1000
segments = [
    {"name": "train", "key": "train", "color": "#1892f8"},
    {"name": "val", "key": "val", "color": "#25e298"},
    {"name": "test", "key": "test", "color": "#fcaf33"},
]

rows_data = [
    {
        "nameHtml": "<strong>black-pawn</strong>",
        "name": "black-pawn",
        "total": 1000,
        "disabled": False,
        "segments": {"train": 600, "val": 350, "test": 50},
    },
    {
        "nameHtml": "<strong>white-pawn</strong>",
        "name": "white-pawn",
        "total": 700,
        "disabled": False,
        "segments": {"train": 400, "val": 250, "test": 50},
    },
]

slider_data = {
    "black-pawn": [
        {
            "moreExamples": ["https://www.w3schools.com/howto/img_nature.jpg"],
            "preview": "https://www.w3schools.com/howto/img_nature.jpg",
        }
    ],
    "white-pawn": [
        {
            "moreExamples": ["https://i.imgur.com/35pUPD2.jpg"],
            "preview": "https://i.imgur.com/35pUPD2.jpg",
        }
    ],
}


# initialize ClassBalance widget
class_balance_1 = ClassBalance(
    max_value=max_value,
    segments=segments,
    rows_data=rows_data,
    slider_data=slider_data,
    max_height=700,
    collapsable=True,
)


card_1 = Card(
    title="Simple example how to use ClassBalance widget",
    content=Container([class_balance_1]),
    collapsable=True,
)
card_1.collapse()

########### Advanced example how to use ClassBalance widget ##################

static_dir = os.path.join(sly.app.get_data_dir(), "static")
sly.fs.mkdir(static_dir, remove_content_if_exists=True)
project_meta = sly.ProjectMeta.from_json(api.project.get_meta(sly.env.project_id()))
dataset = api.dataset.get_info_by_id(sly.env.dataset_id())

PADDINGS = {"top": "20px", "left": "20px", "bottom": "20px", "right": "20px"}

progress = tqdm(desc=f"Processing datasets...", total=dataset.items_count)
image_infos = api.image.get_list(dataset.id)
image_ids = [image_info.id for image_info in image_infos]
imame_nps = api.image.download_nps(dataset.id, image_ids)
anns_json = api.annotation.download_json_batch(dataset.id, image_ids)
anns = [sly.Annotation.from_json(json, project_meta) for json in anns_json]

# prepare data for ClassBalance widget
crop_id = 0
slider_data = defaultdict(list)
new_slider_data = defaultdict(list)
objclass_stats = defaultdict(lambda: defaultdict(lambda: 0))
# collect cropped images for image sliders
for image_info, img, ann in zip(image_infos, imame_nps, anns):
    for idx, objclass in enumerate(project_meta.obj_classes):
        # crop current image to separated images which contain current class instance
        crops = sly.aug.instance_crop(img, ann, objclass.name, False, PADDINGS)
        objclass_stats[objclass.name]["total"] += len(crops)

        for crop_img, crop_ann in crops:
            # draw annotations on image and upload result crop image to Team Files
            crop_ann.draw_pretty(crop_img)
            path = os.path.join(static_dir, f"{crop_id}-{image_info.name}")
            static_path = os.path.join("static", os.path.basename(path))
            crop_id += 1
            sly.image.write(path, crop_img)

            # collect cropped image paths for ClassBalance widget
            if idx == 0:
                slider_data[objclass.name].append({"preview": static_path})
            else:
                new_slider_data[objclass.name].append({"preview": static_path})

    # count number of objects with each tag
    for label in ann.labels:
        for tag in label.tags:
            objclass_stats[label.obj_class.name][tag.name] += 1

    progress.update(1)

# prepare rows data
rows_data = []
new_rows_data = []

tag_metas = project_meta.tag_metas
for idx, obj_class in enumerate(project_meta.obj_classes):
    data = {}
    data["name"] = obj_class.name
    data["nameHtml"] = f"<strong>{obj_class.name}</strong>"
    data["total"] = objclass_stats[obj_class.name]["total"]
    data["disabled"] = False
    data["segments"] = {}
    for tag_meta in tag_metas:
        data["segments"][tag_meta.name] = objclass_stats[obj_class.name][tag_meta.name]
    if idx == 0:
        rows_data.append(data)
    else:
        new_rows_data.append(data)

segments = [{"name": tm.name, "key": tm.name, "color": rgb2hex(tm.color)} for tm in tag_metas]

# initialize ClassBalance widget
class_balance_2 = ClassBalance(
    max_value=max([stat["total"] for stat in objclass_stats.values()]),
    segments=segments[:-1],
    rows_data=rows_data,
    slider_data=slider_data,
    max_height=700,
    collapsable=True,
    clickable_name=True,
    clickable_segment=True,
)

add_segment_btn = Button("Add segment")
add_row_btn = Button("Add row data")
add_slider_data_btn = Button("Add slider data")

buttons = Flexbox([add_segment_btn, add_row_btn, add_slider_data_btn], "horizontal")
text = Text()

card_2 = Card(
    title="Advanced example how to use ClassBalance widget",
    content=Container([class_balance_2, buttons, text]),
    collapsable=True,
)
card_2.collapse()
layout = Container(widgets=[card_1, card_2])

app = sly.Application(layout=layout, static_dir=static_dir)


@class_balance_2.click
def show_item(res):
    if res.get("segmentValue") is not None and res.get("segmentName") is not None:
        info = (
            f"Class {res['name']} contain {res['segmentValue']} tags with name {res['segmentName']}"
        )
        if res["segmentName"] == "val":
            status = "success"
        elif res["segmentName"] == "test":
            status = "warning"
        elif res["segmentName"] == "trash":
            status = "error"
        else:
            status = "info"
    else:
        info = f"Class {res['name']}"
        status = "text"

    text.set(text=info, status=status)


@add_segment_btn.click
def add_segment():
    class_balance_2.add_segments(segments[-1:])


@add_row_btn.click
def add_row():
    class_balance_2.add_rows_data(new_rows_data)


@add_slider_data_btn.click
def add_slider_data():
    class_balance_2.add_slider_data(new_slider_data)
