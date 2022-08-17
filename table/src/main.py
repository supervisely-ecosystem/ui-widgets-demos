import os
from dotenv import load_dotenv
import supervisely as sly
from table.src.generate import multiplication_table

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
app = sly.Application(templates_dir=os.path.join(os.getcwd(), "table", "templates"))


# initialize widgets we will use in UI
table = sly.app.widgets.Table(width="100%")

# create and read table
df = multiplication_table()
table.read_pandas(df)
