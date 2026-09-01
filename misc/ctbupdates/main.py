import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Container  # Select,
from supervisely.app.widgets import (
    ActivityFeed,
    Button,
    Card,
    Checkbox,
    Modal,
    SelectClass,
    SelectTag,
    SelectTeam,
    SelectUser,
    SelectWorkspace,
    Text,
)

# Learn more about the recommended environment variables in the official documentation:
# https://developer.supervisely.com/getting-started/environment-variables/
# Ensure that supervisely.env contains SERVER_ADDRESS and API_TOKEN.
load_dotenv(os.path.expanduser("~/supervisely.env"))
# Ensure that local.env contains TEAM_ID and WORKSPACE_ID.
load_dotenv("local.env")

# Getting the team and workspace ID from environment variables (from local.env file).
team_id = sly.env.team_id()
workspace_id = sly.env.workspace_id()

# Creating an instance of the API, using credentials from supervisely.env file.
api: sly.Api = sly.Api.from_env()

cat_obj_class = sly.ObjClass("cat", sly.Rectangle)
dog_obj_class = sly.ObjClass("dog", sly.Rectangle)
horse_obj_class = sly.ObjClass("horse", sly.Rectangle)
sheep_obj_class = sly.ObjClass("sheep", sly.Rectangle)
cow_obj_class = sly.ObjClass("cow", sly.Rectangle)
elephant_obj_class = sly.ObjClass("elephant", sly.Rectangle)
bear_obj_class = sly.ObjClass("bear", sly.Rectangle)
zebra_obj_class = sly.ObjClass("zebra", sly.Rectangle)
obj_classes = [
    cat_obj_class,
    dog_obj_class,
    horse_obj_class,
    sheep_obj_class,
    cow_obj_class,
    elephant_obj_class,
    bear_obj_class,
    zebra_obj_class,
]

select_team = SelectTeam(show_label=False)
# team_field = Field(select_team, title="Team")
select_workspace = SelectWorkspace(show_label=True, compact=True)
# workspace_field = Field(select_workspace, title="Workspace")

# team_workspace_flexbox = Flexbox(
#     widgets=[team_field, workspace_field],
# )


@select_team.value_changed
def _team_changed(selected_team_id: int):
    print(f"Selected team ID: {selected_team_id}")


select_class = SelectClass(
    obj_classes,
    multiple=True,
    show_add_new_class=True,
)

refresh_users_btn = Button("Refresh Users List")
check_btn = Button("Checks")

update_workspace_btn = Button("Update Workspace")

checkboxes = [Checkbox(f"Option {i}", checked=(i % 2 == 0)) for i in range(1, 6)]
container_checks = Container(widgets=checkboxes)


def print_checkbox(*args, **kwargs):
    print("Checkbox changed:", args, kwargs)


for checkbox in checkboxes:
    checkbox.value_changed(print_checkbox)


select_tag = SelectTag(multiple=True)


completed_item = ActivityFeed.Item(content=Text("Completed task"), status="completed")
processing_item = ActivityFeed.Item(content=Text("Processing data"), status="in_progress")
pending_item = ActivityFeed.Item(content=Text("Pending review"), status="pending")
items = [completed_item, processing_item, pending_item]
activity_feed = ActivityFeed(items=items)

afeed_modal = Modal(title="Activity Feed Example", widgets=[activity_feed])
show_modal_btn = Button("Show Activity Feed Modal")


@show_modal_btn.click
def _show_modal():
    afeed_modal.show_modal()


# select_test = Select(items=[], multiple=True, placeholder="Select options")
selected_classes_cnt = Text(f"Selected classes: 0 / {len(obj_classes)}")
select_annotator_user = SelectUser(roles=["annotator"], multiple=True)
select_admin_user = SelectUser(roles=["admin"], multiple=True)
container = Container(
    widgets=[
        selected_classes_cnt,
        select_class,
        select_annotator_user,
        select_admin_user,
        refresh_users_btn,
        # select_test,
        # select_workspace,
        select_workspace,
        select_team,
        check_btn,
        update_workspace_btn,
        select_tag,
        container_checks,
        afeed_modal,
        show_modal_btn,
    ]
)

card = Card(
    title="Classes List Selector",
    content=container,
)

layout = card
app = sly.Application(layout=layout)


@select_class.class_created
def _class_created(new_class: sly.ObjClass):
    print(f"New class created: {new_class.name}, geometry: {new_class.geometry_type}")


@select_class.value_changed
def _value_changed(selected: list[sly.ObjClass]):
    print(f"Selected classes: {[cls.name for cls in selected]}, total: {len(selected)}")


@refresh_users_btn.click
def _refresh_users():
    select_annotator_user.set_team_id(team_id)
    select_admin_user.set_team_id(team_id)

    # test_items = [
    #     Select.Item(1, name="Option 1"),
    #     Select.Item(2, name="Option 2"),
    # ]

    # select_test.set(items=test_items)


@select_annotator_user.value_changed
def _annotator_user_changed(selected: list):
    print(f"Selected annotator users: {[user.login for user in selected]}")


@select_admin_user.value_changed
def _admin_user_changed(selected: list):
    print(f"Selected admin users: {[user.login for user in selected]}")


@select_workspace.value_changed
def _workspace_changed(workspace_id: int):
    print(f"Selected workspace ID: {workspace_id}")
    team_id = select_workspace.get_team_id()
    print(f"Selected workspace's team ID: {team_id}")


@check_btn.click
def _check():
    selected_classes = select_class.get_selected_class()
    names = [obj_class.name for obj_class in selected_classes]
    print(f"Checked selected classes: {names}")

    selected_annotators = select_annotator_user.get_selected_user()
    names = [user.name for user in selected_annotators]
    print(f"Checked selected annotator users: {names}")


@update_workspace_btn.click
def _update_workspace():
    # select_workspace.set_ids(team_id=team_id, workspace_id=workspace_id)
    select_workspace.set_team_id(team_id)


@afeed_modal.value_changed
def _afeed_value_changed(is_open: bool):
    print(f"Activity Feed modal value changed: {is_open}")
