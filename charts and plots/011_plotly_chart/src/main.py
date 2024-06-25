import plotly.express as px
import plotly.graph_objects as go

import os
import supervisely as sly


from supervisely.app.widgets import Button, Card, Container, PlotlyChart, Text
from dotenv import load_dotenv
import numpy as np

from .demo_data import demo_data_21

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

btn = Button("1 > 2 figure")
fig1 = go.Figure()

x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 17, 14]
z = np.random.rand(10, 40)
fig1.add_trace(go.Scatter(x=x, y=y, mode="lines", name="Line Plot"))
fig1.update_layout(xaxis_title="X Axis", yaxis_title="Y Axis")
plotly_chart_1 = PlotlyChart(figure=fig1)
text_1 = Text()


fig2 = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
plotly_chart_2 = PlotlyChart(figure=fig2)
text_2 = Text()

df = px.data.iris()  # iris is a pandas DataFrame
fig3 = px.scatter(df, x="sepal_width", y="sepal_length")
plotly_chart_3 = PlotlyChart(figure=fig3)
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
plotly_chart_4 = PlotlyChart(figure=fig4)
text_4 = Text()

df = px.data.iris()
fig5 = px.scatter(df, x="sepal_width", y="sepal_length", color="petal_length")
plotly_chart_5 = PlotlyChart(figure=fig5)
text_5 = Text()

df = px.data.iris()
fig6 = px.scatter(df, x="sepal_width", y="sepal_length", color="species", symbol="species")
plotly_chart_6 = PlotlyChart(figure=fig6)
text_6 = Text()

df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df.loc[df["pop"] < 2.0e6, "country"] = "Other countries"  # Represent only large countries
fig7 = px.pie(df, values="pop", names="country")
plotly_chart_7 = PlotlyChart(figure=fig7)
text_7 = Text()

df = px.data.tips()
fig8 = px.pie(df, values="tip", names="day")
plotly_chart_8 = PlotlyChart(figure=fig8)
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
plotly_chart_9 = PlotlyChart(figure=fig9)
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
plotly_chart_10 = PlotlyChart(figure=fig10)
text_10 = Text()

df = px.data.tips()
fig11 = px.bar(df, x="sex", y="total_bill", color="smoker", barmode="group", height=400)
plotly_chart_11 = PlotlyChart(figure=fig11)
text_11 = Text()

df = px.data.tips()
fig12 = px.histogram(
    df, x="sex", y="total_bill", color="smoker", barmode="group", histfunc="avg", height=400
)
plotly_chart_12 = PlotlyChart(figure=fig12)
text_12 = Text()

df = px.data.medals_long()
fig13 = px.bar(df, x="medal", y="count", color="nation")
plotly_chart_13 = PlotlyChart(figure=fig13)
text_13 = Text()


df = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
fig14 = px.bar(df, y="pop", x="country")
plotly_chart_14 = PlotlyChart(figure=fig14)
text_14 = Text()


plotly_chart_15 = PlotlyChart(figure=demo_data_21)
text_15 = Text()

plotly_chart_16 = PlotlyChart()
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
plotly_chart_16.set_figure(fig16)
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
plotly_chart_17 = PlotlyChart(figure=fig17)
text_17 = Text()

fig18 = go.Figure(go.Sunburst(
    labels=[ "Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents=["",    "Eve",  "Eve",  "Seth", "Seth", "Eve",  "Eve",  "Awan",  "Eve" ],
    values=[  65,    14,     12,     10,     2,      6,      6,      4,       4],
    branchvalues="total",
))
fig18.update_layout(margin = dict(t=0, l=0, r=0, b=0))
plotly_chart_18 = PlotlyChart(figure=fig18)
text_18 = Text()

card = Card(
    title="PlotlyChart",
    content=Container(
        [
            btn,
            Container([plotly_chart_1, text_1]),
            Container([plotly_chart_2, text_2]),
            Container([plotly_chart_3, text_3]),
            Container([plotly_chart_4, text_4]),
            Container([plotly_chart_5, text_5]),
            Container([plotly_chart_6, text_6]),
            Container([plotly_chart_7, text_7]),
            Container([plotly_chart_8, text_8]),
            Container([plotly_chart_9, text_9]),
            Container([plotly_chart_10, text_10]),
            Container([plotly_chart_11, text_11]),
            Container([plotly_chart_12, text_12]),
            Container([plotly_chart_13, text_13]),
            Container([plotly_chart_14, text_14]),
            Container([plotly_chart_15, text_15]),
            Container([plotly_chart_16, text_16]),
            Container([plotly_chart_17, text_17]),
            Container([plotly_chart_18, text_18]),
        ]
    ),
)

layout = Container(widgets=[card])

app = sly.Application(layout=layout)


@plotly_chart_1.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}"
    text_1.text = texts


@plotly_chart_2.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}"
    text_2.text = texts


@plotly_chart_3.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}"
    text_3.text = texts


@plotly_chart_4.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}, marker size: {datapoint.marker_size}"
    text_4.text = texts


@plotly_chart_5.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}, marker color: {datapoint.marker_color}"
    text_5.text = texts


@plotly_chart_6.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}, marker color: {datapoint.marker_color}"
    text_6.text = texts


@plotly_chart_7.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nvalue: {datapoint.value}, i: {datapoint.i}"
    text_7.text = texts


@plotly_chart_8.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nvalue: {datapoint.value}, i: {datapoint.i}"
    text_8.text = texts


@plotly_chart_9.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}"
    text_9.text = texts


@plotly_chart_10.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}"
    text_10.text = texts


@plotly_chart_11.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}"
    text_11.text = texts


@plotly_chart_12.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}"
    text_12.text = texts


@plotly_chart_13.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}"
    text_13.text = texts


@plotly_chart_14.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}"
    text_14.text = texts


@plotly_chart_15.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}, customdata: {datapoint.customdata}"
    text_15.text = texts


@plotly_chart_16.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}, customdata: {datapoint.customdata}"
    text_16.text = texts


@plotly_chart_17.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}, customdata: {datapoint.customdata}"
    text_17.text = texts

@plotly_chart_18.click
def click_handler(datapoints):
    texts = ""
    for datapoint in datapoints:
        texts += f"\nx: {datapoint.x}, y: {datapoint.y}, customdata: {datapoint.customdata}"
    text_18.text = texts


@btn.click
def click_handler():
    _fig = plotly_chart_1.get_figure()
    plotly_chart_2.set_figure(_fig)
