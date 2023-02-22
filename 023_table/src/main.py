import os

import pandas as pd
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Table


# function that creates example pandas table
def multiplication_table():
    a = list(range(1, 11))
    b = list(range(1, 6))

    data = []
    for row in b:
        temp = [round(row * number, 1) for number in a]
        temp[-1] = sly.app.widgets.Table.create_button("Delete row")
        data.append(temp)

    a = [f"Col#{str(i)}" for i in a]
    b = [str(i) for i in b]
    return pd.DataFrame(data=data, index=b, columns=a)


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# initialize widgets we will use in UI
table = Table()

# create and read table data
df = multiplication_table()
table.read_pandas(df)

card = Card(
    title="Table",
    content=table,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@table.download_as_csv
def download_as_csv():
    df = table.to_pandas()
    new_df = df.drop(["Col#10"], axis="columns")
    return new_df


@table.click
def handle_table_button(datapoint: sly.app.widgets.Table.ClickedDataPoint):
    if datapoint.button_name is None:
        return
    if datapoint.button_name == "Delete row":
        row_num = datapoint.row["Col#1"]
        table.delete_row("Col#1", row_num)
