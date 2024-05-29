import threading
import time
import logging
import requests


logging.basicConfig(level=logging.DEBUG)

class HiloServicio(threading.Thread):
    def __init__(self, nombre_hilo, url):
        threading.Thread.__init__(self, name=nombre_hilo)
        self.url = "http://localhost:8000/v1/servicio"

    def run(self):
        while True:
            self.consultar()
            time.sleep(60)
            
    def consultar(self):
        response = requests.get(self.url)
        data = response.json()
        with open("servicio.txt", 'w') as file: 
            for item in data:
                file.write(str(item) + '\n') 