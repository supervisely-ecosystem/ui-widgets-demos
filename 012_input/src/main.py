import os
from dotenv import load_dotenv
import supervisely as sly


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
app = sly.Application(templates_dir=os.path.join(os.getcwd(), "012_input", "templates"))

input_text = sly.app.widgets.Input(placeholder="Type: Text")
input_textarea = sly.app.widgets.Input(type="textarea", placeholder="Type: Textarea")
