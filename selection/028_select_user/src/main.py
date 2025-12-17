import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, NotificationBox, SelectUser
from supervisely.api.user_api import UserInfo
from typing import List

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
team_id = sly.env.team_id()
users = api.user.get_team_members(team_id)

select_user = SelectUser(
    users=users,
    team_id=team_id,
    filterable=True,
    placeholder="Select a user",
    multiple=True,
)

notification_box = NotificationBox()

card = Card(
    title="Select User",
    content=Container(widgets=[select_user, notification_box]),
)

layout = Container(widgets=[card])

app = sly.Application(layout=layout)


@select_user.value_changed
def on_user_selected(selected_users: List[UserInfo]):
    user_logins = [user.login for user in selected_users]
    print(f"Selected users: {user_logins}")
    notification_box.set(
        title="Users selected",
        description=f"Selected users: {', '.join(user_logins)}",
    )
