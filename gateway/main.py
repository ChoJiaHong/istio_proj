#先建立簡單的fastapi
from threading import Thread
from scheduler.scheduler import init_scheduler
from fastapi import FastAPI
import uvicorn
from utils import JsonFileHandler

app = FastAPI()

# 初始化排程器 區域
#=======================================================================================================
init_scheduler(app)


#註冊 區域
#=======================================================================================================
register = JsonFileHandler.open_file("register.json")





@app.get("/")
def read_root():
    return {"Hello": "World"}