import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Tree

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

nodes = [
    Tree.Node(
        label="Node 1",
        children=[
            Tree.Node(label="Node 1.1", children=[Tree.Node(label="Node 1.1.1")], disabled=True),
            Tree.Node(label="Node 1.2"),
            Tree.Node(label="Node 1.3"),
        ],
    ),
    Tree.Node(
        label="Node 2",
        children=[
            Tree.Node(label="Node 2.1"),
            Tree.Node(label="Node 2.2"),
            Tree.Node(label="Node 2.3"),
        ],
    ),
    Tree.Node(
        label="Node 3",
        children=[
            Tree.Node(label="Node 3.1"),
            Tree.Node(label="Node 3.2"),
            Tree.Node(
                label="Node 3.3",
                children=[
                    Tree.Node(label="Node 3.3.1"),
                    Tree.Node(label="Node 3.3.2"),
                    Tree.Node(label="Node 3.3.3"),
                ],
            ),
        ],
    ),
]

tree = Tree(
    data=nodes,
    selectable=True,
    accordion=True,
)

card = Card(title="Tree", content=tree)
app = sly.Application(layout=card)
