import os
import supervisely as sly
from supervisely.app.widgets import Button, Card, Container, RandomSplitsTable, Text
from dotenv import load_dotenv


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

project_id = sly.env.project_id()

project = api.project.get_info_by_id(project_id)
items_count = project.items_count

random_splits_table = RandomSplitsTable(
    items_count=items_count,
    start_train_percent=40,
)

button = Button("Button")
text = Text()

card = Card(
    title="Random Splits Table",
    content=Container([random_splits_table, button, text]),
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@button.click
def show_split_settings():
    text.text = random_splits_table.get_splits_counts()
