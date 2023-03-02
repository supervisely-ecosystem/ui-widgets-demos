import supervisely as sly
from supervisely.app.widgets import Container, BindedInputNumber, Card

binded_input_number = BindedInputNumber()

card = Card(
    title="Binded Input Number",
    content=Container(widgets=[binded_input_number]),
)

layout = Container(widgets=[card])
app = sly.Application(layout=layout)
