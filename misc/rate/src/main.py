import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Rate


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api: sly.Api = sly.Api.from_env()


infos = ["oops", "disappointed", "normal", "good", "great"]
colors = ["#1414E4", "#2DE414", "#F7BA2A"]

rate = Rate(colors=colors, texts=infos, text_color="#E414D7", show_text=True, void_color="#17202A")

card = Card(
    "Rate",
    content=Container([rate]),
)


layout = Container(widgets=[card])
app = sly.Application(layout=layout)
