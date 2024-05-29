import threading
import datetime
import logging
import time
from .hilo_servicio import HiloServicio
from .hilo_cliente import HiloCliente

logging.basicConfig(level=logging.DEBUG)

class EjecutarHilos:
    def __init__(self, url_servicio, url_cliente):
        self.url_servicio = url_servicio
        self.url_cliente = url_cliente

    def iniciar_hilos(self):
        tiempo_inicial = datetime.datetime.now()

        hilo_servicio = HiloServicio('hilo_servicio', self.url_servicio)
        hilo_cliente = HiloCliente('hilo_cliente', self.url_cliente)

        hilo_servicio.start()
        hilo_cliente.start()

        tiempo_final = datetime.datetime.now()
        logging.debug('Tiempo Transcurrido: ' + str((tiempo_final - tiempo_inicial).seconds) + ' segundos\n')