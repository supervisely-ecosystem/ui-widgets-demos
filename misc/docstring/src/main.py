import os, requests

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Docstring, Button


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()


button_gmail_content = Button(text="Set gmail content")
button_google_content = Button(text="Set google content")
button_clean_content = Button(text="Clean content")
buttons_container = Container(
    widgets=[button_gmail_content, button_google_content, button_clean_content],
    direction="horizontal",
)

url = "https://www.google.com/"
r = requests.get(url)
url_content = r.text

docstring = Docstring(data=url_content)


card = Card(title="Docstring", content=Container([docstring, buttons_container]))
layout = Container(widgets=[card], direction="vertical")
app = sly.Application(layout=layout)


@button_gmail_content.click
def gmail_content():
    url = "https://www.gmail.com/"
    r = requests.get(url)
    url_content = r.text
    docstring.set_value(url_content)


@button_google_content.click
def google_content():
    url = "https://www.google.com/"
    r = requests.get(url)
    url_content = r.text
    docstring.set_value(url_content)


@button_clean_content.click
def clear():
    docstring.set_value("")
