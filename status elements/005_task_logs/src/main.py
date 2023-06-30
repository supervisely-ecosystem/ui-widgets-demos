import supervisely as sly
from supervisely.app.widgets import Button, Card, Container, InputNumber, TaskLogs


task_id = 36925
logs = TaskLogs()
logs.set_task_id(task_id)

btn = Button("Set task id", button_size="small")
input_task_id = InputNumber(size="small", controls=False)

container = Container(widgets=[input_task_id, btn, logs])

card = Card(content=container, title="Logs")
layout = Container(widgets=[card])

app = sly.Application(layout=layout)


@btn.click
def set_task_id():
    task_id = int(input_task_id.get_value())
    logs.set_task_id(task_id)
