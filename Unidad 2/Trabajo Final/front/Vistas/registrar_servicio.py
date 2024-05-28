import tkinter as tk
import tkinter
import tkinter.messagebox as messagebox
from Controladores.validacion_registrar_servicio import ValidarRegistarServicios
from .tabla_servicio import TablaServicio

class InterfazRegistrarServicio:
    def __init__(self, menu):

        titulos = ["Identificador", "Nombre", "Cédula Cliente", "Descripción", "Valor"]
        columnas = ['id', 'nombre_servicio', 'cedula', 'descripcion', 'valor']
        data = []

        self.ventana = tk.Toplevel(menu)
        self.ventana.focus_set()
        self.ventana.title("Gestionar Servicios")
        self.controladores = ValidarRegistarServicios(self)
        self.crear_interfaz_servicio()
        
        self.tabla = TablaServicio(self.ventana, titulos, columnas, data)
        self.tabla.tabla.grid(column=0, row=15, columnspan=3, padx=15, pady=15)

        self.controladores.boton_consultar_todo_servicio()

        self.tabla.tabla.bind('<<TreeviewSelect>>', self.seleccionar_elementos_servicio)
        self.tabla.tabla.bind('<Delete>', self.borrar_servicio)

    def crear_interfaz_servicio(self):
        self.titulo = tk.Label(self.ventana, text="Ingresar Datos del Servicio")
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

        self.lblIDServicio = tk.Label(self.ventana, text= "ID", padx=20, pady=15)
        self.lblIDServicio.grid(row=9, column=0)
        self.txtIDServicio = tk.Entry(self.ventana, width=20)
        self.txtIDServicio.grid(row=9, column=1)

        self.btnGuardar = tk.Button(self.ventana, text="Guardar", padx=10, pady=5, command=self.controladores.diligenciarServicio)
        self.btnGuardar.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

        self.btnConsultarTodo = tk.Button(self.ventana, text="Consultar Todos los Servicios", command= self.controladores.boton_consultar_todo_servicio)
        self.btnConsultarTodo.grid(row=4, column=2, columnspan=2)

        self.btnConsultarCedulaServicio = tk.Button(self.ventana, text="Consultar Servicio por Cédula del Cliente", command=lambda: self.controladores.boton_consultar_cedula_servicio(self.txtCedulaServicio.get()))
        self.btnConsultarCedulaServicio.grid(row=3, column=2,columnspan=2)

        self.btnFiltrarServicios = tk.Button(self.ventana, text="Filtrar Servicio(s)", command= self.controladores.boton_filtrar_servicio)
        self.btnFiltrarServicios.grid(row=6, column=2, columnspan=2)

        self.btnActualizarServicio = tk.Button(self.ventana, text="Actualizar Servicio", command=lambda: self.actualizar_servicio(self.txtIDServicio.get(), self.txtNombreServicio.get(), self.txtCedulaServicio, self.txtDescripcion.get(), self.txtValor.get()))
        self.btnActualizarServicio.grid(row=5, column=2, columnspan=2)

        self.btnLimpiarCampos = tk.Button(self.ventana, text="Limpiar Campos", padx=10, pady=5, command= self.limpiar_campos)
        self.btnLimpiarCampos.grid(row=10, column=1, columnspan=2, padx=10, pady=10)

        self.btnInformacion = tk.Button(self.ventana, text="Información !", command=self.informacion, padx=10, pady=5)
        self.btnInformacion.grid(row=0, column=2, padx=10, pady=10)

    def seleccionar_elementos_servicio(self, _):
        for i in self.tabla.tabla.selection():
            valores = self.tabla.tabla.item(i)['values']
            self.txtIDServicio.delete(0, tkinter.END)
            self.txtIDServicio.insert(0, valores[0])
            self.txtNombreServicio.delete(0, tkinter.END)
            self.txtNombreServicio.insert(0, valores[1])
            self.txtCedulaServicio.delete(0, tkinter.END)
            self.txtCedulaServicio.insert(0, valores[2])
            self.txtDescripcion.delete(0, tkinter.END)
            self.txtDescripcion.insert(0, valores[3])
            self.txtValor.delete(0, tkinter.END)
            self.txtValor.insert(0, valores[4])

    def borrar_servicio(self, _):
            for i in self.tabla.tabla.selection():
                self.controladores.boton_eliminar_servicio(self.tabla.tabla.item(i)['values'][0])
                self.tabla.tabla.delete(i)
                messagebox.showinfo("Éxito", "Eliminado correctamente.")
                self.limpiar_campos()

    def actualizar_servicio(self, id, nombre_servicio, cedula, descripcion, valor):
        self.controladores.actualizar_servicio(id, nombre_servicio, cedula, descripcion, valor)

    def limpiar_campos(self):
        self.txtNombreServicio.delete(0, tkinter.END)
        self.txtCedulaServicio.delete(0, tkinter.END)
        self.txtDescripcion.delete(0, tkinter.END)
        self.txtValor.delete(0, tkinter.END)
        self.txtIDServicio.delete(0, tkinter.END)
        self.txtNombreServicio.focus_set()

    def informacion(self):
        messagebox.showinfo("Información", "Para seleccionar un servicio dar click al servicio requerido en la tabla.\nPara eliminar un servicio presionar la tecla 'Suprimir' de su teclado una vez seleccionado el servicio.")