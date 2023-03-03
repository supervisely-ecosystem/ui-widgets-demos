import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Container, Switch, OneOf, Text, Card

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

switch = Switch(on_content=Text("ON content"), off_content=Text("OFF content"))
switch_one_of = OneOf(switch)


@switch.value_changed
def print_val(val):
    print(val)


layout = Container(
    widgets=[Card(title="Switch", content=switch), Card(title="OneOf", content=switch_one_of)]
)
app = sly.Application(layout=layout)
