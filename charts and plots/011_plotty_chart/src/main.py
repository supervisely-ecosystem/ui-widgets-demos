import plotly.express as px
import plotly.graph_objects as go

import os

import supervisely as sly

from supervisely.app.widgets import Button, Card, Container, PlottyChart, Text
from dotenv import load_dotenv
import numpy as np

from .demo_data import demo_data_21

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api.from_env()

btn = Button("1 > 2 figure")
fig1 = go.Figure()

x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 17, 14]
z = np.random.rand(10, 40)
fig1.add_trace(go.Scatter(x=x, y=y, mode="lines", name="Line Plot"))
fig1.update_layout(xaxis_title="X Axis", yaxis_title="Y Axis")
plotty_chart_1 = PlottyChart(figure=fig1)
text_1 = Text()


fig2 = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
plotty_chart_2 = PlottyChart(figure=fig2)
text_2 = Text()

df = px.data.iris()  # iris is a pandas DataFrame
fig3 = px.scatter(df, x="sepal_width", y="sepal_length")
plotty_chart_3 = PlottyChart(figure=fig3)
text_3 = Text()

df = px.data.iris()
fig4 = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="species",
    size="petal_length",
    hover_data=["petal_width"],
)
plotty_chart_4 = PlottyChart(figure=fig4)
text_4 = Text()

df = px.data.iris()
fig5 = px.scatter(df, x="sepal_width", y="sepal_length", color="petal_length")
plotty_chart_5 = PlottyChart(figure=fig5)
text_5 = Text()

df = px.data.iris()
fig6 = px.scatter(df, x="sepal_width", y="sepal_length", color="species", symbol="species")
plotty_chart_6 = PlottyChart(figure=fig6)
text_6 = Text()

df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df.loc[df["pop"] < 2.0e6, "country"] = "Other countries"  # Represent only large countries
fig7 = px.pie(df, values="pop", names="country")
plotty_chart_7 = PlottyChart(figure=fig7)
text_7 = Text()

df = px.data.tips()
fig8 = px.pie(df, values="tip", names="day")
plotty_chart_8 = PlottyChart(figure=fig8)
text_8 = Text()


df = px.data.gapminder().query("country == 'Canada'")
fig9 = px.bar(
    df,
    x="year",
    y="pop",
    hover_data=["lifeExp", "gdpPercap"],
    color="lifeExp",
    labels={"pop": "population of Canada"},
    height=400,
)
plotty_chart_9 = PlottyChart(figure=fig9)
text_9 = Text()

df = px.data.gapminder().query("continent == 'Oceania'")
fig10 = px.bar(
    df,
    x="year",
    y="pop",
    hover_data=["lifeExp", "gdpPercap"],
    color="country",
    labels={"pop": "population of Canada"},
    height=400,
)
plotty_chart_10 = PlottyChart(figure=fig10)
text_10 = Text()

df = px.data.tips()
fig11 = px.bar(df, x="sex", y="total_bill", color="smoker", barmode="group", height=400)
plotty_chart_11 = PlottyChart(figure=fig11)
text_11 = Text()

df = px.data.tips()
fig12 = px.histogram(
    df, x="sex", y="total_bill", color="smoker", barmode="group", histfunc="avg", height=400
)
plotty_chart_12 = PlottyChart(figure=fig12)
text_12 = Text()

df = px.data.medals_long()
fig13 = px.bar(df, x="medal", y="count", color="nation")
plotty_chart_13 = PlottyChart(figure=fig13)
text_13 = Text()


df = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
fig14 = px.bar(df, y="pop", x="country")
plotty_chart_14 = PlottyChart(figure=fig14)
text_14 = Text()


plotty_chart_15 = PlottyChart(figure=demo_data_21)
text_15 = Text()

plotty_chart_16 = PlottyChart()
fig16 = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)
plotty_chart_16.set_figure(fig16)
text_16 = Text()


fig17 = go.Figure(
    data=[
        go.Sankey(
            node=dict(
                pad=15,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=["A1", "A2", "B1", "B2", "C1", "C2"],
                color="blue",
            ),
            link=dict(
                source=[0, 1, 0, 2, 3, 3],  # indices correspond to labels, eg A1, A2, A1, B1, ...
                target=[2, 3, 3, 4, 4, 5],
                value=[8, 4, 2, 8, 4, 2],
            ),
        )
    ]
)

fig17.update_layout(title_text="Basic Sankey Diagram", font_size=10)
plotty_chart_17 = PlottyChart(figure=fig17)
text_17 = Text()

fig18 = go.Figure(go.Sunburst(
    labels=[ "Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents=["",    "Eve",  "Eve",  "Seth", "Seth", "Eve",  "Eve",  "Awan",  "Eve" ],
    values=[  65,    14,     12,     10,     2,      6,      6,      4,       4],
    branchvalues="total",
))
fig18.update_layout(margin = dict(t=0, l=0, r=0, b=0))
plotty_chart_18 = PlottyChart(figure=fig18)
text_18 = Text()

card = Card(
    title="PlottyChart",
    content=Container(
        [
            btn,
            Container([plotty_chart_1, text_1]),
            Container([plotty_chart_2, text_2]),
            Container([plotty_chart_3, text_3]),
            Container([plotty_chart_4, text_4]),
            Container([plotty_chart_5, text_5]),
            Container([plotty_chart_6, text_6]),
            Container([plotty_chart_7, text_7]),
            Container([plotty_chart_8, text_8]),
            Container([plotty_chart_9, text_9]),
            Container([plotty_chart_10, text_10]),
            Container([plotty_chart_11, text_11]),
            Container([plotty_chart_12, text_12]),
            Container([plotty_chart_13, text_13]),
            Container([plotty_chart_14, text_14]),
            Container([plotty_chart_15, text_15]),
            Container([plotty_chart_16, text_16]),
            Container([plotty_chart_17, text_17]),
            Container([plotty_chart_18, text_18]),
        ]
    ),
)

layout = Container(widgets=[card])

app = sly.Application(layout=layout)


@plotty_chart_1.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}"
    text_1.text = texts


@plotty_chart_2.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}"
    text_2.text = texts


@plotty_chart_3.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}"
    text_3.text = texts


@plotty_chart_4.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}, marker size: {datapoint.marker_size}"
    text_4.text = texts


@plotty_chart_5.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}, marker color: {datapoint.marker_color}"
    text_5.text = texts


@plotty_chart_6.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}, marker color: {datapoint.marker_color}"
    text_6.text = texts


@plotty_chart_7.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nvalue: {datapoint.value}, i: {datapoint.i}"
    text_7.text = texts


@plotty_chart_8.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nvalue: {datapoint.value}, i: {datapoint.i}"
    text_8.text = texts


@plotty_chart_9.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}"
    text_9.text = texts


@plotty_chart_10.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}"
    text_10.text = texts


@plotty_chart_11.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}"
    text_11.text = texts


@plotty_chart_12.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}"
    text_12.text = texts


@plotty_chart_13.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}"
    text_13.text = texts


@plotty_chart_14.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}"
    text_14.text = texts


@plotty_chart_15.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}, customdata: {datapoint.customdata}"
    text_15.text = texts


@plotty_chart_16.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}, customdata: {datapoint.customdata}"
    text_16.text = texts


@plotty_chart_17.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}, customdata: {datapoint.customdata}"
    text_17.text = texts

@plotty_chart_18.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}, customdata: {datapoint.customdata}"
    text_18.text = texts


@btn.click
def click_handler():
    _fig = plotty_chart_1.get_figure()
    plotty_chart_2.set_figure(_fig)
