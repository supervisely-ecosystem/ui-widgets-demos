import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, SelectCudaDevice, Container, Text


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))
api = sly.Api()

cuda_device = SelectCudaDevice(
    get_list_on_init=True,
    sort_by_free_ram=True,
    include_cpu_option=True,
)

cuda_device.refresh()

value_changed_info = Text(status="info")
value_changed_info.hide()


@cuda_device.value_changed
def new_device_selected(device: str):
    text = "Value changed: {}".format(device)
    value_changed_info.text = text
    value_changed_info.show()


card = Card(
    title="SelectCudaDevice",
    content=Container(widgets=[value_changed_info, cuda_device]),
)

layout = Container(widgets=[card])
app = sly.Application(layout=layout)
