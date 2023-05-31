import os, markdown

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Flexbox, Markdown, Button


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()


button_text = Button(text="Set md text")
button_clean = Button(text="Clean md")
button_readme = Button(text="Set md readme")
buttons_container = Flexbox(widgets=[button_text, button_clean, button_readme])


md_path = os.path.join(os.getcwd(), "misc/markdown/README.md")
f = open(md_path, "r")
md = markdown.markdown(f.read())

markdown = Markdown()

card = Card(title="Markdown", content=Container([markdown, buttons_container]))
layout = Container(widgets=[card], direction="vertical")
app = sly.Application(layout=layout)


@button_text.click
def simple_content():
    markdown.set_value("### Title \n *some markdown text*")


@button_clean.click
def clear_content():
    markdown.set_value("")


@button_readme.click
def readme_content():
    markdown.set_value(md)
