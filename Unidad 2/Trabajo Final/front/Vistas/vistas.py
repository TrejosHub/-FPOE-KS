import tkinter 
import tkinter.messagebox as messagebox
from Controladores.controladores import Controlador
from Vistas.registrar_clientes import InterfazRegistrarCliente 
class Vista:
    def __init__(self):
        self.ventana = tkinter.Tk()        
        self.ventana.geometry("550x200")
        self.ventana.geometry("+500+80")
        self.ventana.title("Menú Principal")
        self.ventana.resizable(0,0)
        self.ventana.focus_set()
        
        self.controladores = Controlador(self)

        self.menu = tkinter.Menu(self.ventana)
        self.ventana.config(menu=self.menu)
        
        self.menuClientes = tkinter.Menu(self.menu)
        self.menu.add_cascade(label= "Gestionar Clientes", menu= self.menuClientes)
        self.menuClientes.add_command(label= "Registrar Cliente", command= lambda: self.registrarCliente())
        self.menuClientes.add_separator()
        self.menuClientes.add_command(label= "Actualizar Cliente", command= lambda: self.actualizarCliente())
        self.menuClientes.add_separator()
        self.menuClientes.add_command(label= "Borrar Cliente", command= lambda: self.borrarCliente())
        self.menuClientes.add_separator()
        self.menuClientes.add_command(label= "Consultar Cliente", command= lambda: self.consultarCliente())


        self.menuServicios = tkinter.Menu(self.menu)
        self.menu.add_cascade(label= "Gestionar Servicios", menu= self.menuServicios)
        self.menuServicios.add_command(label= "Registrar Servicio", command= lambda: self.registrarServicio())
        self.menuServicios.add_separator()
        self.menuServicios.add_command(label= "Actualizar Servicio", command= lambda: self.actualizarServicio())
        self.menuServicios.add_separator()
        self.menuServicios.add_command(label= "Borrar Servicio", command= lambda: self.borrarServicio())
        self.menuServicios.add_separator()
        self.menuServicios.add_command(label= "Consultar Servicio", command= lambda: self.consultarServicio())

        self.menuSalir = tkinter.Menu(self.menu)
        self.menu.add_cascade(label= "Salir", menu= self.menuSalir)
        self.menuSalir.add_command(label= "Salir", command= lambda: self.controladores.el_usuario_quiere_salir())

        self.lblBienvenida = tkinter.Label(self.ventana, text="Bienvenido al software de Lavelopues S.A.", font=("Arial", 12))
        self.lblBienvenida.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.ventana.mainloop()

    def registrarCliente(self):
        interfaz_registrar_cliente = InterfazRegistrarCliente(self.menu)