# Launch this app with:
# misc.ctbupdates.select_user.src.main:app

import os
import supervisely as sly
from supervisely.api.user_api import UserInfo
from supervisely.app.widgets import Card, Container, SelectUser
from dotenv import load_dotenv


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
team_id = sly.env.team_id()

all_users = api.user.get_team_members(team_id)
select_user = SelectUser(team_id=team_id, multiple=True)

container = Container([select_user])
card = Card(title="Select User", content=container)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@select_user.value_changed
def on_user_changed(selected_users: list[UserInfo]):
    print(f"Selected users: {[user.login for user in selected_users]}")
    print(f"Selected users count: {len(selected_users)}")
