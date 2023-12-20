import os
import supervisely as sly
from supervisely.app.widgets import Card, Container, MembersListSelector, Text
from dotenv import load_dotenv


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

team_id = 8  # Change this to your team ID here or in the local.env file
# team_id = sly.env.team_id() # Uncomment this line to use the team ID from the local.env file

team_members = api.user.get_team_members(team_id)
members_list_selector = MembersListSelector(team_members, multiple=True)
selected_members_cnt = Text(f"Selected Members: 0 / {len(team_members)}")

container = Container(widgets=[selected_members_cnt, members_list_selector])

card = Card(
    title="Members List Selector",
    content=members_list_selector,
)

layout = card
app = sly.Application(layout=layout)


@members_list_selector.selection_changed
def on_selection_changed(selected_members):
    selected_members_cnt.set(
        f"Selected Members: {len(selected_members)} / {len(team_members)}", "text"
    )
