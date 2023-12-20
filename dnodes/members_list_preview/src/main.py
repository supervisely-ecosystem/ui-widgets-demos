import os
import supervisely as sly
from supervisely.app.widgets import (
    Card,
    Container,
    MembersListPreview,
    MembersListSelector,
    Text,
)
from dotenv import load_dotenv


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

team_id = 8  # Change this to your team ID
# team_id = sly.env.team_id() # Uncomment this line to use the team ID from the local.env file

members = api.user.get_team_members(team_id)
members_list_selector = MembersListSelector(members, multiple=True)

empty_text = Text("No members selected", "text")
members_list_preview = MembersListPreview(empty_text=empty_text)
preview_text = Text(f"Selected Members: 0 / {len(members)}", "text")
preview_container = Container([preview_text, members_list_preview])

container = Container(widgets=[members_list_selector, preview_container])

card = Card(
    title="Members List Preview",
    content=container,
)

layout = card
app = sly.Application(layout=layout)


@members_list_selector.selection_changed
def on_selection_changed(selected_members):
    preview_text.set(f"Selected Members: {len(selected_members)} / {len(members)}", "text")
    members_list_preview.set(selected_members)
