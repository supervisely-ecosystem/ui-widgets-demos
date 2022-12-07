import os

import numpy as np
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, TextArea, Container

load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

text_area_1 = TextArea(value="Some text in the text area.\nThat widget can display multiple rows of text.\nThird sentence.", 
                       autosize=False)

text_area_2 = TextArea(value="This is the same widget, but with autosize=True. \nDue to this, it stretches under the content. \nYou don't have to scroll to see all the content.", 
                       autosize=True)

container = Container(widgets=[text_area_1, text_area_2])
card = Card(title="My card", content=container)
app = sly.Application(layout=card)
