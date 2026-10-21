from threading import Thread, Lock
from datetime import datetime

file_lock = Lock()

def write_log(message):
  with file_lock:
    with open("game_log.txt","a") as file:
      current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      
      file.write(current_time + " | " + message + "\n")
      
      
      
def log_event(message):
  worker = Thread(target=write_log, args =(message,))
  

  worker.start()
  worker.join()
