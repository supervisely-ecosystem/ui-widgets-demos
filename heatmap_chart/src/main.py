import os
from dotenv import load_dotenv
import supervisely as sly
from heatmap_chart.src.generate import multiplication_chart


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
app = sly.Application(
    templates_dir=os.path.join(os.getcwd(), "heatmap_chart", "templates")
)


# get project info from server
chart = sly.app.widgets.HeatmapChart(
    title="Multiplication Table",
    xaxis_title="",
    color_range="row",
    tooltip="Result multiplication of {x} * {series_name}",
)

data = multiplication_chart()

lines = []
for idx, line in enumerate(data):
    lines.append({"name": idx + 1, "x": list(range(1, 11)), "y": line})
chart.add_series_batch(lines)
