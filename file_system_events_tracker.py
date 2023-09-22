import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from_dir ="C:/Users/Marcelo/Downloads/Aula"
to_dir="C:/Users/Marcelo/Desktop"
class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"olá, {event.src_path} foi criado")
    def on_deleted(self, event):
         print(f"olá, {event.src_path} foi excluido")

try:
            
             
    while True:
        time.sleep(2)
        print("executando...")     
except KeyboardInterrupt:
        print("interrompido!")
        Observer.stop()  
      

