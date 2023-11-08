import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Cascader, Text

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()


# initialize widgets we will use in UI

pussy_black_cat = Cascader.Item(value="pussy cat", label="pussy cat")
smooth_haired_cat = Cascader.Item(value="smooth-haired cat", label="smooth-haired cat")
black_cat = Cascader.Item(
    value="black cat", label="black cat", children=[pussy_black_cat, smooth_haired_cat]
)
white_cat = Cascader.Item(value="white cat", label="white cat")
red_cat = Cascader.Item(value="red cat", label="red cat")

angry_dog = Cascader.Item(value="angry dog", label="angry dog", disabled=True)
kind_dog = Cascader.Item(value="kind dog", label="kind dog")

animals = [
    Cascader.Item(value="cat", label="cat", children=[black_cat, white_cat, red_cat]),
    Cascader.Item(value="dog", label="dog", children=[angry_dog, kind_dog]),
    Cascader.Item(value="horse", label="horse"),
    Cascader.Item(value="sheep", label="sheep"),
]

select_items = Cascader(items=animals)
select_items.select_item(["cat", "black cat", "pussy cat"])

text = Text()

card = Card(
    title="Cascader",
    content=Container(widgets=[select_items, text]),
)

layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@select_items.value_changed
def show_item(res):
    if res == []:
        return

    info = f"You choise: {'/'.join(str(x) for x in res)} item"
    text.set(text=info, status="info")
