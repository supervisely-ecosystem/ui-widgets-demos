import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Checkbox, Container, Empty, Field, Input

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

button = Button()
checkbox = Checkbox("checkbox")
input = Input()

container = Container([input, checkbox, button])

field_1 = Field(
    content=container,
    title="Field 1",
    description="Field description",
)

field_2 = Field(
    content=Container([Input(), Input(), Button()]),
    title="Field 2",
    description="Field description",
)

card = Card(
    title="Card",
    description="Card Description",
    content=Container([field_1, field_2]),
)
app = sly.Application(layout=card)
