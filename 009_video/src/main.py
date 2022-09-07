import os
from dotenv import load_dotenv
import supervisely as sly


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely-umar.env"))

api = sly.Api()
app = sly.Application(templates_dir=os.path.join(os.getcwd(), "009_video", "templates"))


# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()
# sly_app = sly.app.fastapi.create()

# app._fastapi.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# 25598 - pavel
# 3267370 - max dev
# 25598 - umar
video_id = 25598

video = sly.app.widgets.Video(video_id=video_id)
