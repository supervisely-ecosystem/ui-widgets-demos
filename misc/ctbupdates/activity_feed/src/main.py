# Launch this app with:
# misc.ctbupdates.activity_feed.src.main:app

import os
import supervisely as sly
from supervisely.app.widgets import Card, Container, ActivityFeed, Text
from dotenv import load_dotenv


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

completed_item = ActivityFeed.Item(content=Text("Completed task"), status="completed")
processing_item = ActivityFeed.Item(content=Text("Processing data"), status="in_progress")
pending_item = ActivityFeed.Item(content=Text("Pending review"), status="pending")
items = [completed_item, processing_item, pending_item]
activity_feed = ActivityFeed(items=items)

container = Container([activity_feed])
card = Card(title="Activity Feed", content=container)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
