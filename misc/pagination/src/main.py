import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Pagination, Text

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api: sly.Api = sly.Api.from_env()


pagination = Pagination(
    total=1000, page_size=20, page_sizes=[10, 20, 50], layout="prev, pager, next, sizes, total"
)

text_page = Text()
text_size = Text()

card = Card(
    "Pagination",
    content=Container([pagination, text_page, text_size]),
)


layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@pagination.current_change
def page_change(res):
    info = f"Current page number: {res}"
    text_page.set(text=info, status="info")


@pagination.size_change
def page_size_change(res):
    info = f"Current page size: {res}"
    text_size.set(text=info, status="success")
