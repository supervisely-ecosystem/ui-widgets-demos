import os
import supervisely as sly
from supervisely.app.widgets import Card, Container, BenchmarkReportSelector, Button, Text
from dotenv import load_dotenv


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

team_id = 33
workspace_id = 90


model_comparison_selector = BenchmarkReportSelector(team_id)

model_comparison_selector.set(573, "instance segmentation", [0])


button = Button("Show selected models")
text = Text("")

container = Container([model_comparison_selector, button, text])

card = Card(
    title="Model Comparison Selector",
    content=container,
)
layout = Container(widgets=[card])
app = sly.Application(layout=layout)


@model_comparison_selector.value_changed
def model_comparison_selector_value_changed_handler(value):
    selected_rows = model_comparison_selector.get_selected_rows()
    output_text = f"Selected models: ({len(selected_rows)}) - {selected_rows}"

    selected_ids = model_comparison_selector.get_selected_row_indexes()
    output_text += f"\nSelected models: ({len(selected_ids)}) - {selected_ids}"

    selected_project = model_comparison_selector.get_selected_project_id()
    selected_task_type = model_comparison_selector.get_selected_task_type()
    selected_infos = model_comparison_selector.get_selected_benchmark_infos()

    text.set(output_text, "info")


@model_comparison_selector.project_changed
def model_comparison_selector_project_changed_handler(project_id):
    print(f"Project changed to: {project_id}")


@model_comparison_selector.task_type_changed
def model_comparison_selector_task_type_changed_handler(task_type):
    print(f"Task type changed to: {task_type}")


@button.click
def button_click_handler():
    selected_rows = model_comparison_selector.get_selected_rows()
    output_text = f"Selected models: ({len(selected_rows)}) - {selected_rows}"

    selected_ids = model_comparison_selector.get_selected_row_indexes()
    output_text += f"\nSelected models: ({len(selected_ids)}) - {selected_ids}"

    text.set(output_text, "info")
