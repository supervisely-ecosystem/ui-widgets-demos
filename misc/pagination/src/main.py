import supervisely as sly
from supervisely.app.widgets import Button, Card, Container, Pagination, Text

pagination = Pagination(
    total=1000,
    page_size=50,
    layout=["prev", "pager", "next"],  # or just string layout="prev, pager, next"
    page_size_options=[10, 50, 100],
)

text_page = Text()
text_size = Text()
btn = Button("Set layout")

card = Card(
    "Pagination",
    content=Container([pagination, text_page, text_size, btn]),
)


layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@pagination.page_changed
def page_change(res):
    info = f"Current page number: {res}"
    text_page.set(text=info, status="info")


@pagination.page_size_changed
def page_size_change(res):
    info = f"Current page size: {res}"
    text_size.set(text=info, status="success")


@btn.click
def set_layout():
    pagination.set_layout(["prev", "pager", "next", "sizes"])
