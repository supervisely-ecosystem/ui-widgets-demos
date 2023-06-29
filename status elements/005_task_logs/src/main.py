import supervisely as sly
from supervisely.app.widgets import Card, Container, TaskLogs


logs = TaskLogs()
card = Card(title="Task Logs", content=logs)
layout = Container(widgets=[card])

app = sly.Application(layout=layout)
