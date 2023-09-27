import os
import json

from dotenv import load_dotenv
import supervisely as sly
from supervisely.app.widgets import Button, Card, Container, Editor, Flexbox, Text, ImageSlider

# for convenient debug, has no effect in production
if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()


image_urls = [
    "https://www.w3schools.com/howto/img_nature.jpg",
    "https://www.quackit.com/pix/samples/18m.jpg",
    "https://i.imgur.com/35pUPD2.jpg",
    "https://i.imgur.com/fB2DBcM.jpeg",
    "https://i.imgur.com/OpSj3JE.jpg",
]

example_urls = [
    [
        "https://www.w3schools.com/howto/img_nature.jpg",
        "https://www.quackit.com/pix/samples/18m.jpg",
        "https://i.imgur.com/35pUPD2.jpg",
        "https://i.imgur.com/fB2DBcM.jpeg",
        "https://i.imgur.com/OpSj3JE.jpg",
    ],
    ["https://www.quackit.com/pix/samples/18m.jpg"],
    ["https://i.imgur.com/35pUPD2.jpg"],
    ["https://i.imgur.com/fB2DBcM.jpeg"],
    ["https://i.imgur.com/OpSj3JE.jpg"],
]


combined_data = [
    {
        "preview": "https://i.imgur.com/0XbKOJ3.jpeg",
        "moreExamples": ["https://i.imgur.com/0XbKOJ3.jpeg", "https://i.imgur.com/mIcObyL.jpeg"],
    },
    {
        "preview": "https://i.imgur.com/3rYHhEu.jpeg",
        "moreExamples": [
            "https://i.imgur.com/3rYHhEu.jpeg",
            "https://i.imgur.com/pSafUhg.jpeg",
            "https://i.imgur.com/yKc0xTb.jpeg",
        ],
    },
]

image_slider = ImageSlider(previews=image_urls, examples=example_urls)


image_url = Text(status="info")
image_index = Text(status="info")
image_examples = Text(status="info")
data_length = Text(status="info")

text_container = Container(widgets=[image_url, image_index, image_examples, data_length])

button_url = Button(text="Get info")
button_set_url = Button(text="Select image by url")
button_set_index = Button(text="Select image by index")
button_extend_data = Button(text="Extend data")
button_set_data = Button(text="Set new data")
button_toggle_selectable = Button(text="Toggle selectable")
button_get_data = Button(text="Get data")

buttons_container = Flexbox(
    widgets=[
        button_url,
        button_set_url,
        button_set_index,
        button_extend_data,
        button_set_data,
        button_toggle_selectable,
        button_get_data,
    ]
)

all_data = Editor(height_lines=20)
all_data.hide()

card = Card(
    title="Image Slider",
    content=Container([image_slider, text_container, buttons_container, all_data]),
)

layout = Container(widgets=[card])

app = sly.Application(layout=layout)


@button_url.click
def get_info():
    image_url.text = f"Image URL: {image_slider.get_selected_preview()}"
    image_index.text = f"Image index on slider: {image_slider.get_selected_idx()}"
    image_examples.text = f"Image examples: {image_slider.get_selected_examples()}"
    data_length.text = f"Data length: {image_slider.get_data_length()}"


@button_set_url.click
def set_url():
    image_slider.set_selected_preview("https://i.imgur.com/OpSj3JE.jpg")
    get_info()


@button_set_index.click
def set_index():
    image_slider.set_selected_idx(2)
    get_info()


@button_extend_data.click
def extend_data():
    image_slider.append_data(combined_data=combined_data[:1])
    get_info()


@button_set_data.click
def set_data():
    image_slider.set_data(combined_data=combined_data)
    get_info()


@button_toggle_selectable.click
def toggle_selectable():
    if image_slider.is_selectable:
        image_slider.disable_selection()
    else:
        image_slider.enable_selection()


@button_get_data.click
def get_data():
    data = image_slider.get_data()
    all_data.set_text(json.dumps(data, indent=4))
    all_data.show()
