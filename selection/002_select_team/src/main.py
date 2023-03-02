import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Button, Card, Container, NotificationBox, SelectTeam

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

team_id = sly.env.team_id()

# initialize widgets we will use in UI
select_team = SelectTeam()

ok_btn = Button("OK")
notification_box = NotificationBox()

card = Card(
    title="Select Team",
    content=Container(widgets=[select_team, ok_btn, notification_box]),
)

layout = Container(widgets=[card])

app = sly.Application(layout=layout)


@ok_btn.click
def show_team_members():
    team_id = select_team.get_selected_id()
    team = api.team.get_info_by_id(team_id)
    notification_box.set(
        title=f"Team '{team.name}'",
        description=f"Your role in the team: {team.role}",
    )
