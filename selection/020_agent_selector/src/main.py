import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, AgentSelector, Text, Container

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

team_id = sly.env.team_id()
agent_selector = AgentSelector(team_id, show_only_gpu=False, show_only_running=True)

agent_id_preview = Text("", "text")
agent_name_preview = Text("", "text")
agent_preview_container = Container([agent_id_preview, agent_name_preview])
agent_preview_container.hide()

container = Container([agent_selector, agent_preview_container])
layout = Card(title="AgentSelector", content=container)
app = sly.Application(layout=layout)


@agent_selector.value_changed
def get_selected_row(agent_id):
    agent_preview_container.hide()
    agent_info = api.agent.get_info_by_id(agent_id)
    agent_id_preview.set(f"Agent ID: {agent_info.id}", "text")
    agent_name_preview.set(f"Agent Name: {agent_info.name}", "text")
    agent_preview_container.show()
