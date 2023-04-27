import os, markdown

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Markdown, Button


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()


button_readme = Button(text="Set md readme")
button_text = Button(text="Set md text")
button_clean = Button(text="Clean md")
buttons_container = Container(
    widgets=[button_readme, button_text, button_clean], direction="horizontal"
)


md_path = os.path.join(os.getcwd(), "misc/markdown/README.md")
f = open(md_path, "r")
md = markdown.markdown(f.read())

markdown = Markdown(content=md)

card = Card(title="Markdown", content=Container([markdown, buttons_container]))
layout = Container(widgets=[card], direction="vertical")
app = sly.Application(layout=layout)


@button_readme.click
def gmail_content():
    markdown.set_value(md)


@button_text.click
def google_content():
    markdown.set_value("some markdown text")


@button_clean.click
def clear():
    markdown.set_value("")
