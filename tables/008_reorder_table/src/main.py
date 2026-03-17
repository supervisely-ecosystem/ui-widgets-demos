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

refresh_btn = Button("Refresh")
apply_btn = Button("Apply changes")

saved_data = [list(row) for row in data]

top_right_controls = Container(
    [apply_btn, refresh_btn],
    direction="horizontal",
)
reorder_table = ReorderTable(
    columns=columns,
    data=data,
    page_size=5,
    content_top_right=top_right_controls,
)


def update_state(order):
    reordered_data = reorder_table.get_reordered_data()
    reordered_names = [row[0] for row in reordered_data]


@reorder_table.order_changed
def handle_reorder(order):
    update_state(order)


@refresh_btn.click
def refresh_state():
    reorder_table.set_data(columns, saved_data)
    update_state(reorder_table.get_order())


@apply_btn.click
def apply_changes():
    saved_data[:] = [list(row) for row in reorder_table.get_reordered_data()]
    reorder_table.set_data(columns, saved_data)
    update_state(reorder_table.get_order())


content = Container([reorder_table])
card = Card(title="ReorderTable", content=content)

app = sly.Application(layout=card)
