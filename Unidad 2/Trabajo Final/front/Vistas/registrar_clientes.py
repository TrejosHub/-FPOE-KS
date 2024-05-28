import tkinter as tk
import tkinter
import tkinter.messagebox as messagebox
from Controladores.validacion_registrar_clientes import ValidarRegistarClientes
from .tabla_cliente import TablaCliente

class InterfazRegistrarCliente:
    def __init__(self, menu):
        titulos = ["Identificador", "Nombre", "Apellido", "Cédula", "Teléfono", "Correo"]
        columnas = ['id', 'nombre', 'apellido', 'cedula', 'telefono', 'correo']
        data = []

        self.ventana = tk.Toplevel(menu)
        self.ventana.focus_set()
        self.ventana.title("Registrar Cliente")
        self.controladores = ValidarRegistarClientes(self)
        self.crear_interfaz()

        self.tabla = TablaCliente(self.ventana, titulos, columnas, data)
        self.tabla.tabla.grid(column=0, row=15, columnspan=3, padx=15, pady=15)

        self.controladores.boton_consultar_todo_cliente()
        
        self.tabla.tabla.bind('<<TreeviewSelect>>', self.seleccionar_elementos_cliente)
        self.tabla.tabla.bind('<Delete>', self.borrar_cliente)

    def crear_interfaz(self):
        self.titulo = tk.Label(self.ventana, text="Ingresar Datos del Cliente")
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

        self.lblTelefono = tk.Label(self.ventana, text="Teléfono: ", pady=20, padx=15)
        self.lblTelefono.grid(row=7, column=0)
        self.txtTelefono = tk.Entry(self.ventana, width=20)
        self.txtTelefono.grid(row=7, column=1)
        self.txtTelefono.bind("<KeyRelease>", lambda event: self.controladores.validar_telefono(event, self.txtTelefono))
        self.lblOcultoTelefono = tk.Label(self.ventana, text="", fg="red")
        self.lblOcultoTelefono.grid(row=8, column=0, columnspan=2)

        self.lblCorreo = tk.Label(self.ventana, text="Correo: ", pady=20, padx=15)
        self.lblCorreo.grid(row=9, column=0)
        self.txtCorreo = tk.Entry(self.ventana, width=20)
        self.txtCorreo.grid(row=9, column=1)
        self.txtCorreo.bind("<KeyRelease>", lambda event: self.controladores.validar_correo(event, self.txtCorreo))
        self.lblOcultoCorreo = tk.Label(self.ventana, text="", fg="red")
        self.lblOcultoCorreo.grid(row=10, column=0, columnspan=2)

        self.lblIDCliente = tk.Label(self.ventana, text= "ID:", padx=20, pady=15)
        self.lblIDCliente.grid(row=11, column=0)
        self.txtIDCliente = tk.Entry(self.ventana, width=20)
        self.txtIDCliente.grid(row=11, column=1)

        self.btnGuardar = tk.Button(self.ventana, text="Guardar", padx=10, pady=5, command=self.controladores.diligenciar_cliente)
        self.btnGuardar.grid(row=12, column=0, columnspan=2, padx=10, pady=10)

        self.btnConsultarTodo = tk.Button(self.ventana, text="Consultar Todos los Clientes", command=self.controladores.boton_consultar_todo_cliente)
        self.btnConsultarTodo.grid(row=6, column=2, columnspan=2)

        self.btnConsultarCedula = tk.Button(self.ventana, text="Consultar Cliente por Cédula", command=lambda: self.controladores.boton_consultar_cedula(self.txtCedula.get()))
        self.btnConsultarCedula.grid(row=5, column=2,columnspan=2)

        self.btnFiltrarCliente = tk.Button(self.ventana, text="Filtrar Cliente(s)", command=self.controladores.boton_filtrar_cliente)
        self.btnFiltrarCliente.grid(row=9, column=2, columnspan=2)

        self.btnActualizarCliente = tk.Button(self.ventana, text="Actualizar Cliente", command=lambda: self.actualizar_cliente(self.txtIDCliente.get(), self.txtNombre.get(), self.txtApellido.get(), self.txtCedula.get(), self.txtTelefono.get(), self.txtCorreo.get()))
        self.btnActualizarCliente.grid(row=8, column=2, columnspan=2)

        self.btnLimpiarCampos = tk.Button(self.ventana, text="Limpiar Campos", padx=10, pady=5, command= self.limpiar_campos)
        self.btnLimpiarCampos.grid(row=12, column=1, columnspan=2, padx=10, pady=10)

        self.btnInformacion = tk.Button(self.ventana, text="Información !", command=self.informacion, padx=10, pady=5)
        self.btnInformacion.grid(row=0, column=2, padx=10, pady=10)
        
    def seleccionar_elementos_cliente(self, _):
        for i in self.tabla.tabla.selection():
            valores = self.tabla.tabla.item(i)['values']
            self.txtIDCliente.delete(0, tkinter.END)
            self.txtNombre.delete(0, tkinter.END)
            self.txtApellido.delete(0, tkinter.END)
            self.txtCedula.delete(0, tkinter.END)
            self.txtTelefono.delete(0, tkinter.END)
            self.txtCorreo.delete(0, tkinter.END)
            self.txtIDCliente.insert(0, valores[0])
            self.txtNombre.insert(0, valores[1])
            self.txtApellido.insert(0, valores[2])
            self.txtCedula.insert(0, valores[3])
            self.txtTelefono.insert(0, valores[4])
            self.txtCorreo.insert(0, valores[5])

    def borrar_cliente(self, _):
        for i in self.tabla.tabla.selection():
            self.controladores.boton_eliminar_cliente(self.tabla.tabla.item(i)['values'][0])
            self.tabla.tabla.delete(i)
            messagebox.showinfo("Éxito", "Eliminado correctamente.")
            self.limpiar_campos()

    def actualizar_cliente(self, id, nombre, apellido, cedula, telefono, correo):
        self.controladores.actualizar_cliente(id, nombre, apellido, cedula, telefono, correo)

    def limpiar_campos(self):
        self.txtNombre.delete(0, tkinter.END)
        self.txtApellido.delete(0, tkinter.END)
        self.txtCedula.delete(0, tkinter.END)
        self.txtTelefono.delete(0, tkinter.END)
        self.txtCorreo.delete(0, tkinter.END)
        self.txtIDCliente.delete(0, tkinter.END)
        self.txtNombre.focus_set()

    def informacion(self):
        messagebox.showinfo("Información", "Para seleccionar un cliente dar click al cliente requerido en la tabla.\nPara eliminar un cliente presionar la tecla 'Suprimir' de su teclado una vez seleccionado el cliente.")