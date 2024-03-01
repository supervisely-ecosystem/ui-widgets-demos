import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, AgentSelector

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

agent_selector = AgentSelector(team_id=8)
card = Card(title="AgentSelector", content=agent_selector)
app = sly.Application(layout=card)


@agent_selector.value_changed
def get_agent_id(id):
    print(id)
