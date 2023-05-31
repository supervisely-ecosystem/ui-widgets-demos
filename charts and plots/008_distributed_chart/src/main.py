import os
import supervisely as sly
from dotenv import load_dotenv

from supervisely.app.widgets import DistributedChart, Card

load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

colors = [
    "#008FFB",
    "#00E396",
    "#FEB019",
    "#FF4560",
    "#775DD0",
    "#3F51B5",
    "#546E7A",
    "#D4526E",
    "#8D5B4C",
    "#F86624",
]

dc = DistributedChart(title="Distributed Chart")

card = Card("Distributed Chart", content=dc)

names1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
values1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

names2 = ["name1", "name1", "name1", "name4", "name5"]
values2 = [1.2, 2.1, 3.7, 4, 5]


dc.set_series(names2, values2)
# dc.add_series(names1, values1)

# dc.delete_series(1)

print(dc.get_series(0))

layout = card
app = sly.Application(layout=layout)


@dc.click
def test(dp):
    print("click")

    print(dp)
