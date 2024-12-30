import supervisely as sly
import random, os
from supervisely.app.widgets import Card, Container, IFrame, Bokeh, Text, Button, InputNumber
from dotenv import load_dotenv

# if sly.is_development():
#     load_dotenv("local.env")
#     load_dotenv(os.path.expanduser("~/supervisely.env"))


def get_plot(idx=0):
    # data = sly.json.load_json_file("charts and plots/012_bokeh_chart/src/series.json")
    # x_coordinates = [point["x"] for point in data]
    # y_coordinates = [point["y"] for point in data]
    x_coordinates = [random.uniform(0, 10) for _ in range(100)]
    y_coordinates = [random.uniform(0, 10) for _ in range(100)]
    color = sly.color.rgb2hex(sly.color.random_rgb())
    plot = Bokeh.Circle(
        x_coordinates,
        y_coordinates,
        radii=0.05,
    )
    plot = Bokeh.Circle(
        x_coordinates,
        y_coordinates,
        radii=0.05,
        colors=[color] * len(x_coordinates),
        legend_label=f"Plot {idx}",
        plot_id=f"plot_{idx}",
    )
    return plot


# plot = get_plot()
bokeh = Bokeh(
    plots=[],
    x_axis_visible=True,
    y_axis_visible=True,
    grid_visible=True,
    show_legend=True,
    legend_location="right",
    legend_click_policy="hide",
)
# bokeh.clear()
# bokeh.add_plots([plot])
iframe = IFrame()


iframe.set(bokeh.html_route_with_timestamp, height="650px", width="100%")
bokeh_card = Card(title="Chart", content=Container([iframe]))


text = Text()
btn = Button("Add plots")

size_input = InputNumber(min=0.01, value=0.05, step=0.01)
size_btn = Button("Change size of dots", button_size="small")
dots = Container([size_input, size_btn], direction=["horizontal"])
preview_card = Card(title="Preview", content=Container([text, btn, dots]))

charts = Container([bokeh_card], direction=["horizontal"])
layout = Container(widgets=[charts, preview_card])
app = sly.Application(layout=layout)


@bokeh.value_changed
def on_click(selected_ids):
    text.text = f"Selected ids: {selected_ids}"


@btn.click
def on_click():
    plots = [get_plot(i) for i in range(3)]
    bokeh.clear()
    bokeh.add_plots(plots)
    iframe.set(bokeh.html_route_with_timestamp, height="650px", width="100%")
    text.text = "Plot updated"


@size_btn.click
def on_click():
    size = size_input.value
    bokeh.update_radii(size)
    iframe.set(bokeh.html_route_with_timestamp, height="650px", width="100%")
    text.text = "Size of dots updated"
