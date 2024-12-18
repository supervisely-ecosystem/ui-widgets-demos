import supervisely as sly
import random, os
from supervisely.app.widgets import Card, Container, IFrame, Bokeh, Text, Button
from dotenv import load_dotenv

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))


def get_plot():
    # data = sly.json.load_json_file("charts and plots/012_bokeh_chart/src/series.json")
    # x_coordinates = [point["x"] for point in data]
    # y_coordinates = [point["y"] for point in data]
    x_coordinates = [random.uniform(0, 10) for _ in range(100)]
    y_coordinates = [random.uniform(0, 10) for _ in range(100)]
    plot = Bokeh.Circle(x_coordinates, y_coordinates, radii=0.05)
    return plot


plot = get_plot()
bokeh = Bokeh(plots=[], x_axis_visible=True, y_axis_visible=True, grid_visible=True)
# bokeh.clear()
# bokeh.add_plots([plot])
iframe = IFrame()


iframe.set(bokeh.html_route_with_timestamp, height="650px", width="100%")
bokeh_card = Card(title="Chart", content=Container([iframe]))


text = Text()
btn = Button()
preview_card = Card(title="Preview", content=Container([text, btn]))

charts = Container([bokeh_card], direction=["horizontal"])
layout = Container(widgets=[charts, preview_card])
app = sly.Application(layout=layout)


@bokeh.value_changed
def on_click(selected_ids):
    text.text = f"Selected ids: {selected_ids}"


@btn.click
def on_click():
    plot = get_plot()
    bokeh.clear()
    bokeh.add_plots([plot])
    iframe.set(bokeh.html_route_with_timestamp, height="650px", width="100%")
    text.text = "Plot updated"
