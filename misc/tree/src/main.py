import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Text, Tree, Button

load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api: sly.Api = sly.Api.from_env()


# data = [
#     {
#         "id": 1,
#         "label": "Level one 1",
#         "children": [
#             {
#                 "id": 4,
#                 "label": "Level two 1-1",
#                 "children": [
#                     {"id": 9, "label": "Level three 1-1-1"},
#                     {"id": 10, "label": "Level three 1-1-2"},
#                 ],
#             }
#         ],
#     },
#     {
#         "id": 2,
#         "label": "Level one 2",
#         "children": [{"id": 5, "label": "Level two 2-1"}, {"id": 6, "label": "Level two 2-2"}],
#     },
#     {
#         "id": 3,
#         "label": "Level one 3",
#         "children": [
#             {"id": 7, "label": "Level two 3-1", "disabled": True},
#             {"id": 8, "label": "Level two 3-2"},
#         ],
#     },
# ]

node_1 = Tree.Node(label="Level one 1", disabled=True)

node_2 = Tree.Node(label="Level one 2")
children_2_1 = Tree.Children(parent=node_2, label="Level two 2-1")
node_2.add_children(children=children_2_1)

nodes = [node_1, node_2]


tree = Tree(data=nodes, show_checkbox=True)

text = Text()


card = Card(
    "Tree",
    content=Container([tree, text]),
)


button = Button("Add node", "plus", "success")

text_2 = Text()

layout = Container(widgets=[card, text_2, button])
app = sly.Application(layout=layout)


@button.click
def add_node():
    node = tree.get_current_node()

    text_2.text = f"{node}"
    # node = Tree.Node(label="New node")
    # tree.add_node(node)

    # new_node = Tree.Node(label="New node")
    # tree.add_node(new_node)


@tree.node_click
def show_time(node: Tree.Node):
    info = f"{node}\nCurrent node id={node.get_id()}"  # , label text: {node.get_label()}"
    text.set(text=info, status="info")


@tree.check_change
def show_time(res):
    info = f"Current checkbox id={res['id']}"
    text.set(text=info, status="info")
