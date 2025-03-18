import time
from threading import Thread
import json
def save_file(file_content,file_name):
    with open(file_name, 'w') as f:
            json.dump(file_content, f)

def open_file(file_name):
    file_content = {}
    with open(file_name, 'r') as f:
        file_content = json.load(f)
    return file_content

#定時儲存檔案
def periodic_save_file(file_content,file_name):
    while True:
        save_file(file_content,file_name)
        time.sleep(10)