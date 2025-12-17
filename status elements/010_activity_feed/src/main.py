import os
import supervisely as sly
from supervisely.app.widgets import Card, Container, ActivityFeed, Text
from dotenv import load_dotenv


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# Create items with custom content
item1 = ActivityFeed.Item(content=Text("Processing dataset"), status="completed")
item2 = ActivityFeed.Item(content=Text("Training model"), status="in_progress", number=2)
item3 = ActivityFeed.Item(content=Text("Generating report"), status="pending")

# Create activity feed
feed = ActivityFeed(items=[item1, item2, item3])

# Add item during runtime
new_item = ActivityFeed.Item(content=Text("Deploy model"), status="pending")
feed.add_item(new_item)

container = Container([feed])

card = Card(
    title="Activity Feed with Progress",
    content=container,
)
layout = card
app = sly.Application(layout=layout)
