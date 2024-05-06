import tkinter as tk
import tkinter.messagebox as messagebox
from Controladores.validacion_registrar_servicio import ValidarRegistarServicios

class InterfazRegistrarServicio:
    def __init__(self, menu):
        self.ventana = tk.Toplevel(menu)
        self.ventana.focus_set()
        self.ventana.title("Registrar Servicio")
        self.ventana.geometry("550x420")
        self.ventana.resizable(0, 0)
        self.controladores = ValidarRegistarServicios(self)
        self.crear_interfaz_servicio()

    def crear_interfaz_servicio(self):
        self.titulo = tk.Label(self.ventana, text="Registrar Servicio")
        self.titulo.grid(row=0, column=0, columnspan=2)

        self.lblNombreServicio = tk.Label(self.ventana, text="Nombre del Servicio: ", pady=20, padx=15)
        self.lblNombreServicio.grid(row=1, column=0)
        self.txtNombreServicio = tk.Entry(self.ventana, width=20)
        self.txtNombreServicio.grid(row=1, column=1)
        self.txtNombreServicio.bind("<KeyRelease>", lambda event: self.controladores.validar_nombre_servicio(event, self.txtNombreServicio))
        self.lblOcultoNombreServicio = tk.Label(self.ventana, text="", fg="red")
        self.lblOcultoNombreServicio.grid(row=2, column=0, columnspan=2)

        self.lblCedulaCServicio = tk.Label(self.ventana, text="Cedula del Cliente: ", pady=20, padx=15)
        self.lblCedulaCServicio.grid(row=3, column=0)
        self.txtCedulaServicio = tk.Entry(self.ventana, width=20)
        self.txtCedulaServicio.grid(row=3, column=1)
        self.txtCedulaServicio.bind("<KeyRelease>", lambda event: self.controladores.validar_cedula_servicio(event, self.txtCedulaServicio))
        self.lblOcultoCedulaServicio = tk.Label(self.ventana, text="", fg="red")
        self.lblOcultoCedulaServicio.grid(row=4, column=0, columnspan=2)

        self.lblDescripcion = tk.Label(self.ventana, text="Descripción: ", pady=20, padx=15)
        self.lblDescripcion.grid(row=5, column=0)
        self.txtDescripcion = tk.Entry(self.ventana, width=50)
        self.txtDescripcion.grid(row=5, column=1)
        self.txtDescripcion.bind("<KeyRelease>", lambda event: self.controladores.validar_descripcion(event, self.txtDescripcion))
        self.lblOcultoDescripcion = tk.Label(self.ventana, text="", fg="red")
        self.lblOcultoDescripcion.grid(row=6, column=0, columnspan=2)

        self.lblValor = tk.Label(self.ventana, text="Valor: ", pady= 20, padx=15)
        self.lblValor.grid(row=7, column=0)
        self.txtValor = tk.Entry(self.ventana, width=20)
        self.txtValor.grid(row=7, column=1)
        self.txtValor.bind("<KeyRelease>", lambda event: self.controladores.validar_valor(event, self.txtValor))
        self.lblOcultoValor = tk.Label(self.ventana, text="", fg="red")
        self.lblOcultoValor.grid(row=8, column=0, columnspan=2)

        self.btnGuardar = tk.Button(self.ventana, text="Guardar", command=self.controladores.diligenciarServicio)
        self.btnGuardar.grid(row=11, column=0, columnspan=2)