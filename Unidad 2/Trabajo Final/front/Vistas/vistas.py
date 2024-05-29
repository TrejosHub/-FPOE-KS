# Vistas/vistas.py
import tkinter
import tkinter.messagebox as messagebox
from Controladores.controladores import Controlador
from Vistas.registrar_clientes import InterfazRegistrarCliente
from Vistas.registrar_servicio import InterfazRegistrarServicio
from Controladores.hilo import EjecutarHilos  # Asegúrate de que esta ruta sea correcta

class Vista:
    def __init__(self):
        self.ventana = tkinter.Tk()
        self.ventana.geometry("550x200")
        self.ventana.geometry("+500+80")
        self.ventana.title("Menú Principal")
        self.ventana.resizable(0, 0)
        self.ventana.focus_set()

        self.controladores = Controlador(self)

        self.menu = tkinter.Menu(self.ventana)
        self.ventana.config(menu=self.menu)

        self.menuClientes = tkinter.Menu(self.menu)
        self.menu.add_cascade(label="Menú Gestionar Clientes", menu=self.menuClientes)
        self.menuClientes.add_command(label="Gestionar Clientes", command=lambda: self.registrarCliente())

        self.menuServicios = tkinter.Menu(self.menu)
        self.menu.add_cascade(label="Menú Gestionar Servicios", menu=self.menuServicios)
        self.menuServicios.add_command(label="Gestionar Servicios", command=lambda: self.registrarServicio())

        self.menuSalir = tkinter.Menu(self.menu)
        self.menu.add_cascade(label="Salir", menu=self.menuSalir)
        self.menuSalir.add_command(label="Salir", command=lambda: self.controladores.el_usuario_quiere_salir())

        self.lblBienvenida = tkinter.Label(self.ventana, text="Bienvenido al software oficial de Lavelopues S.A.", font=("Arial", 12))
        self.lblBienvenida.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # Iniciar los hilos al inicializar la ventana
        self.iniciar_hilos()

        self.ventana.mainloop()

    def iniciar_hilos(self):
        url_servicio = 'http://localhost:8000/v1/servicio'
        url_cliente = 'http://localhost:8000/v1/cliente'

        ejecutor = EjecutarHilos(url_servicio, url_cliente)
        ejecutor.iniciar_hilos()

    def registrarCliente(self):
        interfaz_registrar_cliente = InterfazRegistrarCliente(self.menu)

    def registrarServicio(self):
        interfaz_registrar_servicio = InterfazRegistrarServicio(self.menu)

