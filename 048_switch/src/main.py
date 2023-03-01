import supervisely as sly
from supervisely.app.widgets import Container, Switch, OneOf, Text, Card

switch = Switch(on_content=Text("ON Conent"), off_content=Text("OFF content"))
switch_one_of = OneOf(switch)

@switch.value_changed
def print_val(val):
    print(val)

layout = Container(widgets=[Card(title="Switch", content=switch), Card(title="OneOf", content=switch_one_of)])
app = sly.Application(layout=layout)
