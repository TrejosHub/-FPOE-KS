import tkinter as tk
import tkinter.messagebox as messagebox
from Controladores.validacion_registrar_clientes import ValidarRegistarClientes

class InterfazRegistrarCliente:
    def __init__(self, menu):
        self.ventana = tk.Toplevel(menu)
        self.ventana.focus_set()
        self.ventana.title("Registrar Cliente")
        self.ventana.geometry("270x470")
        self.ventana.resizable(0, 0)
        self.controladores = ValidarRegistarClientes(self)
        self.crear_interfaz()

    def crear_interfaz(self):
        self.titulo = tk.Label(self.ventana, text="Registrar Cliente")
        self.titulo.grid(row=0, column=0, columnspan=2)

        self.lblNombre = tk.Label(self.ventana, text="Nombre: ", pady=20, padx=15)
        self.lblNombre.grid(row=1, column=0)
        self.txtNombre = tk.Entry(self.ventana, width=20)
        self.txtNombre.grid(row=1, column=1)
        self.txtNombre.bind("<KeyRelease>", lambda event: self.controladores.validar_nombre(event, self.txtNombre))
        self.lblOcultoNombre = tk.Label(self.ventana, text="", fg="red")
        self.lblOcultoNombre.grid(row=2, column=0, columnspan=2)

        self.lblApellido = tk.Label(self.ventana, text="Apellido: ", pady=20, padx=15)
        self.lblApellido.grid(row=3, column=0)
        self.txtApellido = tk.Entry(self.ventana, width=20)
        self.txtApellido.grid(row=3, column=1)
        self.txtApellido.bind("<KeyRelease>", lambda event: self.controladores.validar_apellido(event, self.txtApellido))
        self.lblOcultoApellido = tk.Label(self.ventana, text="", fg="red")
        self.lblOcultoApellido.grid(row=4, column=0, columnspan=2)

        self.lblCedula = tk.Label(self.ventana, text="Cédula: ", pady=20, padx=15)
        self.lblCedula.grid(row=5, column=0)
        self.txtCedula = tk.Entry(self.ventana, width=20)
        self.txtCedula.grid(row=5, column=1)
        self.txtCedula.bind("<KeyRelease>", lambda event: self.controladores.validar_cedula(event, self.txtCedula))
        self.lblOcultoCedula = tk.Label(self.ventana, text="", fg="red")
        self.lblOcultoCedula.grid(row=6, column=0, columnspan=2)

        self.lblTelefono = tk.Label(self.ventana, text="Teléfono: ", pady= 20, padx=15)
        self.lblTelefono.grid(row=7, column=0)
        self.txtTelefono = tk.Entry(self.ventana, width=20)
        self.txtTelefono.grid(row=7, column=1)
        self.txtTelefono.bind("<KeyRelease>", lambda event: self.controladores.validar_telefono(event, self.txtTelefono))
        self.lblOcultoTelefono = tk.Label(self.ventana, text="", fg="red")
        self.lblOcultoTelefono.grid(row=8, column=0, columnspan=2)

        self.lblCorreo = tk.Label(self.ventana, text="Correo : ", pady=20, padx=15)
        self.lblCorreo.grid(row=9, column=0)
        self.txtCorreo = tk.Entry(self.ventana, width=20)
        self.txtCorreo.grid(row=9, column=1)
        self.txtCorreo.bind("<KeyRelease>", lambda event: self.controladores.validar_correo(event, self.txtCorreo))
        self.lblOcultoCorreo = tk.Label(self.ventana, text="", fg="red")
        self.lblOcultoCorreo.grid(row=10, column=0, columnspan=2)

        self.btnGuardar = tk.Button(self.ventana, text="Guardar", command=self.controladores.diligenciar)
        self.btnGuardar.grid(row=11, column=0, columnspan=2)