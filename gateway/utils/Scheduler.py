from threading import Thread
from utils import JsonFileHandler
def Scheduler():
    #讀取register.json文件的內容
    register = JsonFileHandler.open_file(file_name)
    #建立一個定時任務將register的內容寫入register.json文件
    save_register_thread = Thread(target=JsonFileHandler.periodic_save_file, args=(register,file_name))
    save_register_thread.start()
    return save_register_thread