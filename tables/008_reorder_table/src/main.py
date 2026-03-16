import supervisely as sly
from supervisely.app.widgets import Button, Card, Container, ReorderTable, Text


columns = ["Name", "Score", "Department"]
data = [
    ["Alice", 95, "CV"],
    ["Bob", 87, "NLP"],
    ["Carol", 92, "ML Platform"],
    ["David", 79, "MLOps"],
    ["Eve", 98, "Research"],
    ["Frank", 84, "Data Engineering"],
]

reset_btn = Button("Reset order")
reorder_table = ReorderTable(
    columns=columns,
    data=data,
    page_size=5,
    content_top_right=reset_btn,
)

refresh_btn = Button("Refresh state")


def update_state(order):
    reordered_data = reorder_table.get_reordered_data()
    reordered_names = [row[0] for row in reordered_data]


@reorder_table.order_changed
def handle_reorder(order):
    update_state(order)


@refresh_btn.click
def refresh_state():
    update_state(reorder_table.get_order())


@reset_btn.click
def reset_order():
    reorder_table.reset_order()
    update_state(reorder_table.get_order())


content = Container([reorder_table, refresh_btn])
card = Card(title="ReorderTable", content=content)

app = sly.Application(layout=card)
