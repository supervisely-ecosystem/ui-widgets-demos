import os

import numpy as np
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, LineChart, Container, Grid, MyText

load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

def get_lineplot():
    size1 = 10
    x1 = list(range(size1))
    y1 = np.random.randint(low=10, high=148, size=size1).tolist()
    s1 = [{"x": x, "y": y} for x, y in zip(x1, y1)]

    size2 = 20
    x2 = list(range(size2))
    y2 = np.random.randint(low=0, high=300, size=size2).tolist()
    s2 = [{"x": x, "y": y} for x, y in zip(x2, y2)]

    line_chart = LineChart(
        title=f"Loss {y2[-1]}",
        series=[{"name": "Train", "data": s1}, {"name": "Val", "data": s2}],
        xaxis_type="category",
    )
    return line_chart


# card = Card(
#     title="Train Val plots",
#     content=Grid([get_lineplot(), get_lineplot(), get_lineplot()], columns=3)
# )
# layout = Container(widgets=[card])
# app = sly.Application(layout=layout)


# button = MyButton(text='Get Text', button_type='warning', button_size='large', plain=True, show_loading=True)

textarea = MyText(text='Lorem ipsum dolor sit amet')
card = Card(title="My card", content=textarea)
app = sly.Application(layout=card)
