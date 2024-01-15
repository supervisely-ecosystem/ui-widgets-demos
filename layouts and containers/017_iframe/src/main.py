import os
from pathlib import Path
import supervisely as sly
from supervisely.app.widgets import Card, Container, IFrame, Button
from dotenv import load_dotenv


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

static_dir = Path("layouts and containers/017_iframe/static")
iframe = IFrame("static/index_1.html", height="300px", width="300px")


button_template_1 = Button("Template 1")
button_template_2 = Button("Template 2")
button_template_3 = Button("Template 3")

button_container = Container(
    widgets=[button_template_1, button_template_2, button_template_3], direction="horizontal"
)

container = Container(widgets=[iframe, button_container])

layout = Card(
    title="IFrame",
    content=container,
)
app = sly.Application(layout=layout, static_dir=static_dir)


@button_template_1.click
def set_template_1():
    iframe.set("static/index_1.html", height="300px", width="300px")


@button_template_2.click
def set_template_2():
    iframe.set("static/index_2.html", height="500px", width="500px")


@button_template_3.click
def set_template_3():
    iframe.set("static/index_3.html", height="200px", width="1000px")
