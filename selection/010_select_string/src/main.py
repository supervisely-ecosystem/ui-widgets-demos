import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, RadioTabs, Text, SelectString


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# select_string = SelectString(["string1", "string2", "string3"])
select_string = SelectString(["cat"])
select_string_mini = SelectString(["cat"], size="mini")
select_string_small = SelectString(["cat"], size="small")
select_string_large = SelectString(["cat"], size="large")


card = Card(
    # title="Radio tabs"
    content=Container(
        [select_string, select_string_mini, select_string_small, select_string_large]
    ),
)
# card_many_tabs = Card("Many radio tabs", content=many_tabs)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
