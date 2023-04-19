import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Text, Tree, Button

load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api: sly.Api = sly.Api.from_env()


data = [
    {
        "label": "Level one 1",
        "children": [
            {
                "label": "Level two 1-1",
                "children": [
                    {"label": "Level three 1-1-1"},
                    {"label": "Level three 1-1-2"},
                ],
            }
        ],
    },
    {
        "label": "Level one 2",
        "children": [{"label": "Level two 2-1"}, {"label": "Level two 2-2"}],
    },
    {
        "label": "Level one 3",
        "children": [
            {"label": "Level two 3-1", "disabled": True},
            {"label": "Level two 3-2"},
        ],
    },
]

node_1 = Tree.Node(label="Level one 1")
child_1 = Tree.Node(label="Level two 1-1")
child_11 = Tree.Node(label="Level three 1-1-1")
child_12 = Tree.Node(label="Level three 1-1-2")
child_1.add_children([child_11, child_12])
node_1.add_children([child_1])


child_2_1 = Tree.Node(label="Level two 2-1")
child_2_2 = Tree.Node(label="Level two 2-2")
node_2 = Tree.Node(label="Level one 2", children=[child_2_1, child_2_2])

node_3 = Tree.Node(label="Level one 3")
child_3_1 = Tree.Node(label="Level two 3-1", disabled=True)
child_3_2 = Tree.Node(label="Level two 3-2")
node_3.add_children([child_3_1, child_3_2])


nodes = [node_1, node_2, node_3]


tree = Tree(data=nodes, show_checkbox=True)

# tree.set_data(nodes)

# tree.disable_node(5)
# tree.unable_node(8)

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
    # node_4 = {
    #     "label": "Level one 4",
    #     "children": [{"label": "Level two 4-1"}, {"label": "Level two 4-2"}],
    # }

    # node_5 = {"label": "Level one 5"}
    node_4 = Tree.Node(label="Level one 4")
    child_4_1 = Tree.Node(label="Level two 4-1")
    node_4.add_children([child_4_1])
    node_5 = Tree.Node(label="Level one 5")
    tree.add_nodes([node_4, node_5])


@tree.node_click
def show_node(node: Tree.Node):
    info = f"Current node id={node.get_id()}, label text: {node.get_label()}"
    text.set(text=info, status="info")


@tree.check_change
def show_check(res):
    info = f"Current checkbox id={res['id']}"
    text.set(text=info, status="info")
