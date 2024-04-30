import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG)

class Hilo6(threading.Thread):
    def __init__(self, nombre_hilo, nombre_persona):
        threading.Thread.__init__(self, name=nombre_hilo, target=Hilo6.run)
        self.nombreHilo = nombre_hilo
        self.nombre_persona = nombre_persona

    def guardar_nombre(self, nombre):
            with open("nombres.txt", "a") as file:
                file.write(nombre + "\n")
                logging.debug(f"Nombre guardado en archivo: {nombre}")
                
    def run(self):
        while True:
            nombre = input("Por favor, introduce tu nombre: ")
            print("Nombre introducido:", nombre)
            self.guardar_nombre(nombre)
            time.sleep(5)