import os

import numpy as np
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, LineChart, Container, Grid, Textarea

load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

textarea = Textarea(text="Some text in text area.\nThat element can display multiple rows of text.\nThird sentence.", 
                    autosize=False)
card = Card(title="My card", content=textarea)
app = sly.Application(layout=card)
