import os
import random
from collections import defaultdict

from dotenv import load_dotenv
import supervisely as sly
from supervisely.app.widgets import Button, Card, ClassBalance, Container, Flexbox, Text
from tqdm import tqdm

# for convenient debug, has no effect in production
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
        "nameHtml": "<div>black-pawn</div>",
        "name": "black-pawn",
        "total": 1000,
        "disabled": False,
        "segments": {"train": 600, "val": 350, "test": 50},
    },
    {
        "name": "white-pawn",
        "total": 700,
        "disabled": False,
        "segments": {"train": 400, "val": 250, "test": 50},
    },
    {
        "name": "black-rook",
        "total": 450,
        "disabled": True,
        "segments": {"train": 300, "val": 150, "test": 0},
    },
    {
        "name": "white-rook",
        "total": 250,
        "disabled": False,
        "segments": {"train": 200, "val": 50, "test": 0},
    },
]

slider_data = {
    "black-pawn": [
        {
            "moreExamples": ["https://www.w3schools.com/howto/img_nature.jpg"],
            "preview": "https://www.w3schools.com/howto/img_nature.jpg",
        },
        {
            "moreExamples": ["https://www.quackit.com/pix/samples/18m.jpg"],
            "preview": "https://www.quackit.com/pix/samples/18m.jpg",
        },
    ],
    "white-pawn": [
        {
            "moreExamples": ["https://i.imgur.com/35pUPD2.jpg"],
            "preview": "https://i.imgur.com/35pUPD2.jpg",
        },
        {
            "moreExamples": ["https://i.imgur.com/fB2DBcM.jpeg"],
            "preview": "https://i.imgur.com/fB2DBcM.jpeg",
        },
    ],
    "black-rook": [
        {
            "moreExamples": ["https://i.imgur.com/OpSj3JE.jpg"],
            "preview": "https://i.imgur.com/OpSj3JE.jpg",
        },
        {
            "moreExamples": ["https://www.w3schools.com/howto/img_nature.jpg"],
            "preview": "https://www.w3schools.com/howto/img_nature.jpg",
        },
        {
            "moreExamples": ["https://www.quackit.com/pix/samples/18m.jpg"],
            "preview": "https://www.quackit.com/pix/samples/18m.jpg",
        },
    ],
    "white-rook": [
        {
            "moreExamples": ["https://i.imgur.com/35pUPD2.jpg"],
            "preview": "https://i.imgur.com/35pUPD2.jpg",
        },
        {
            "moreExamples": ["https://i.imgur.com/fB2DBcM.jpeg"],
            "preview": "https://i.imgur.com/fB2DBcM.jpeg",
        },
        {
            "moreExamples": ["https://i.imgur.com/OpSj3JE.jpg"],
            "preview": "https://i.imgur.com/OpSj3JE.jpg",
        },
    ],
}

new_data = {
    "segment": {"name": "Extra", "key": "extra", "color": "#611268"},
    "row_data": {
        "name": "extra-row",
        "total": 280,
        "disabled": False,
        "segments": {"train": 200, "val": 50, "test": 0, "extra": 30},
    },
    "slider_data": {
        "extra-row": [
            {
                "moreExamples": ["https://i.imgur.com/OpSj3JE.jpg"],
                "preview": "https://i.imgur.com/OpSj3JE.jpg",
            }
        ],
    },
}

# initialize ClassBalance widget
class_balance_1 = ClassBalance(
    max_value=max_value,
    segments=segments,
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

card_1 = Card(
    title="Class Balance",
    content=Container([class_balance_1, buttons, text]),
)


@class_balance_1.click
def show_item(res):
    if res.get("segmentValue") is not None and res.get("segmentName") is not None:
        info = (
            f"Class {res['name']} contain {res['segmentValue']} tags with name {res['segmentName']}"
        )
        if res["segmentName"] == "val":
            status = "success"
        elif res["segmentName"] == "test":
            status = "warning"
        else:
            status = "info"
    else:
        info = f"Class {res['name']}"
        status = "text"

    text.set(text=info, status=status)


@add_segment_btn.click
def add_segment():
    new_segment = new_data["segment"]
    class_balance_1.add_segments([new_segment])


@add_row_btn.click
def add_row():
    row_data = new_data["row_data"]
    class_balance_1.add_rows_data([row_data])


@add_slider_data_btn.click
def add_slider_data():
    slider_data = new_data["slider_data"]
    class_balance_1.add_slider_data(slider_data)


############## Advanced example how to use ClassBalance widget ##################

data_dir = sly.app.get_data_dir()
team_id = sly.env.team_id()
project_id = sly.env.project_id()
project_meta = sly.ProjectMeta.from_json(api.project.get_meta(project_id))
datasets = api.dataset.get_list(project_id)

# prepare data for ClassBalance widget
max_value = 0
rows_data = []
slider_data = defaultdict(list)

PADDINGS = {"top": "20px", "left": "20px", "bottom": "20px", "right": "20px"}
SAMPLE_RATE = 0.4  # ⬅️ change it
crop_id = 0
objclass_stats = defaultdict(lambda: defaultdict(lambda: 0))

progress = tqdm(desc=f"Processing datasets...", total=len(datasets))
for ds in datasets:
    sample_cnt = max(int(SAMPLE_RATE * ds.items_count), 1)
    image_infos = api.image.get_list(
        ds.id,
        filters=[{"field": "labelsCount", "operator": ">", "value": 0}],
    )
    random.shuffle(image_infos)
    image_infos = image_infos[:sample_cnt]
    image_ids = [image_info.id for image_info in image_infos]

    imame_nps = api.image.download_nps(ds.id, image_ids)
    anns_json = api.annotation.download_json_batch(ds.id, image_ids)
    anns = [sly.Annotation.from_json(json, project_meta) for json in anns_json]

    # collect infos and cropped images for image sliders
    for image_info, img, ann in zip(image_infos, imame_nps, anns):
        for objclass in project_meta.obj_classes:
            # crop current image to separated images which contain current class instance
            crops = sly.aug.instance_crop(img, ann, objclass.name, False, PADDINGS)
            objclass_stats[objclass.name]["total"] += len(crops)
            max_value = max(max_value, objclass_stats[objclass.name]["total"])

            for crop_img, crop_ann in crops:
                # draw annotations on image and upload result crop image to Team Files
                crop_ann.draw_pretty(crop_img)
                path = os.path.join(data_dir, f"{crop_id}-{image_info.name}")
                crop_id += 1
                sly.image.write(path, crop_img)
                file_info = api.file.upload(team_id, path, path)

                # collect cropped image url
                slider_data[objclass.name].append({"preview": file_info.full_storage_url})

        # count number of objects with each tag
        for label in ann.labels:
            for tag in label.tags:
                objclass_stats[label.obj_class.name][tag.name.lower()] += 1

    progress.update(1)

# prepare rows data
for obj_class in project_meta.obj_classes:
    data = {}
    data["name"] = obj_class.name
    data["nameHtml"] = f"<div>{obj_class.name}</div>"
    data["total"] = objclass_stats[obj_class.name]["total"]
    data["disabled"] = False
    data["segments"] = {
        "train": objclass_stats[obj_class.name]["train"],
        "val": objclass_stats[obj_class.name]["val"],
        "test": objclass_stats[obj_class.name]["test"],
    }
    rows_data.append(data)

# initialize ClassBalance widget
class_balance_2 = ClassBalance(
    max_value=max_value,
    segments=segments,
    rows_data=rows_data,
    slider_data=slider_data,
    max_height=700,
    collapsable=True,
    clickable_name=False,
    clickable_segment=False,
)


card_2 = Card(
    title="Class Balance",
    content=Container([class_balance_2]),
)

layout = Container(widgets=[card_1, card_2])

app = sly.Application(layout=layout)
