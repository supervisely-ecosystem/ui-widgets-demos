import os

import pandas as pd
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, ClassicTable, Container


# function that creates example pandas table
def multiplication_table():
    a = list(range(1, 11))
    b = list(range(1, 6))

    data = []
    for row in b:
        temp = [round(row * number, 1) for number in a]
        data.append(temp)

    a = [f"Col#{str(i)}" for i in a]
    b = [str(i) for i in b]
    return pd.DataFrame(data=data, index=b, columns=a)


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# initialize widgets we will use in UI
classic_table = ClassicTable()

# create and read table
df = multiplication_table()
classic_table.read_pandas(df)

card = Card(
    title="Classic Table",
    content=classic_table,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)
