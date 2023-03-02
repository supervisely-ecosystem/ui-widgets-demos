import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, FileThumbnail
import supervisely.io.env as env

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

team_id = env.team_id()

# prepare file to upload in Team files
local_filepath = "/Users/almaz/job/text.txt"

# remote path in Team files
remote_filepath = "/file_thumbnail_demo/text.txt"

if api.file.exists(team_id, remote_filepath):
    api.file.remove(team_id, remote_filepath)

# upload file from local directory to Team files
api.file.upload(team_id, local_filepath, remote_filepath)

# get file info from server
fileinfo = api.file.get_info_by_path(team_id, remote_filepath)

# initialize widgets we will use in UI and set FileInfo
file_thumbnail = FileThumbnail(info=fileinfo)

card = Card(
    title="File Thumbnail",
    content=Container(widgets=[file_thumbnail]),
)

layout = Container(widgets=[card])
app = sly.Application(layout=layout)
