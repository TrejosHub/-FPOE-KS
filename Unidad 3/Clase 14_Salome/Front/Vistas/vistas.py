import tkinter
from Controladores.controladores import Controladores
import requests
from .tablas import Tabla
from tkinter import messagebox

class Vista():
    def __init__(self):
        titulos = ['Identificador', 'Marca', 'Sabor', 'Color', 'Cantidad']
        columnas = ['id', 'marca', 'sabor', 'color', 'cantidad']
        data = []

        self.root = tkinter.Tk()
        self.root.title("Papitas")
        self.root.resizable(0, 0)

        self.tabla = Tabla(self.root, titulos, columnas, data)  

        self.labelTitulo = tkinter.Label(self.root, text="Diligencie el Formulario")
        self.labelTitulo.grid(column=0, row=0, padx=15, pady=15, columnspan=2)

        self.labelMarca = tkinter.Label(self.root, text="Marca")
        self.labelMarca.grid(column=0, row=1, padx=20, pady=20)
        self.txtMarca = tkinter.Entry(self.root, width=30)
        self.txtMarca.grid(column=1, row=1)

        self.labelOcultoNombre = tkinter.Label(self.root, text="")
        self.labelOcultoNombre.grid(column=0, row=2, columnspan=2)

        self.labelSabor = tkinter.Label(self.root, text="Sabor")
        self.labelSabor.grid(column=0, row=3, padx=20, pady=20)
        self.txtSabor = tkinter.Entry(self.root, width=30)
        self.txtSabor.grid(column=1, row=3)

        self.labelOcultoApellido = tkinter.Label(self.root, text="")
        self.labelOcultoApellido.grid(column=0, row=4, columnspan=2)

        self.labelColor = tkinter.Label(self.root, text="Color")
        self.labelColor.grid(column=0, row=5, padx=20, pady=20)
        self.txtColor = tkinter.Entry(self.root, width=30)
        self.txtColor.grid(column=1, row=5)

        self.labelCorreoOculto = tkinter.Label(self.root, text="")
        self.labelCorreoOculto.grid(column=0, row=6, columnspan=2)

        self.labelCantidad = tkinter.Label(self.root, text="Cantidad")
        self.labelCantidad.grid(column=0, row=7, padx=20, pady=20)
        self.txtCantidad = tkinter.Entry(self.root, width=30)
        self.txtCantidad.grid(column=1, row=7)

        self.labelEdadOculto = tkinter.Label(self.root, text="")
        self.labelEdadOculto.grid(column=0, row=8, columnspan=2)

        self.labelID = tkinter.Label(self.root, text="Id: ")
        self.labelID.grid(column=0, row=9, padx=20, pady=20)
        self.txtID = tkinter.Entry(self.root, width=30)
        self.txtID.grid(column=1, row=9)

        self.labelIDOculto = tkinter.Label(self.root, text="")
        self.labelIDOculto.grid(column=0, row=10, columnspan=2)

        self.controladores = Controladores(self)

        self.botonDiligenciar = tkinter.Button(self.root, text="Diligenciar", command=self.controladores.diligenciar)
        self.botonDiligenciar.grid(column=0, row=11, columnspan=1, padx=8, pady=8)

        self.botonConsultar = tkinter.Button(self.root, text="Consultar", command=lambda: self.controladores.boton_consultar(self.txtID.get()))
        self.botonConsultar.grid(column=1, row=11, columnspan=1, padx=8, pady=8)

        self.botonConsultarTodo = tkinter.Button(self.root, text="Consultar Todo", command=self.controladores.boton_consultar_todo)
        self.botonConsultarTodo.grid(column=2, row=11, columnspan=1, padx=8, pady=8)

        self.botonConsultarFiltro = tkinter.Button(self.root, text="Filtrar", command=self.controladores.boton_filtrar)
        self.botonConsultarFiltro.grid(column=3, row=11, columnspan=1, padx=8, pady=8)

        self.botonActualizar = tkinter.Button(self.root, text="Actualizar", command=lambda: self.controladores.actualizar(self.txtID.get(), self.txtMarca.get(), self.txtSabor.get(), self.txtColor.get(), self.txtCantidad.get()))
        self.botonActualizar.grid(column=0, row=12, columnspan=1, padx=8, pady=8)

        self.botonLimpiar = tkinter.Button(self.root, text="Limpiar Campos", command=self.limpiar_campos)
        self.botonLimpiar.grid(column=1, row=12, columnspan=1, padx=8, pady=8)

        self.botonEliminar = tkinter.Button(self.root, text="Eliminar", command=lambda: self.borrar_elemento(None))
        self.botonEliminar.grid(column=2, row=12, columnspan=1, padx=8, pady=8)

        self.tabla = Tabla(self.root, titulos, columnas, data)
        self.tabla.tabla.grid(column=0, row=13, columnspan=1, padx=8, pady=8)


        def seleccionar_elemento(_):
            for i in self.tabla.tabla.selection():
                valores = self.tabla.tabla.item(i)['values']
                self.txtID.delete(0, tkinter.END)
                self.txtID.insert(0, valores[0])
                self.txtMarca.delete(0, tkinter.END)
                self.txtMarca.insert(0, valores[1])
                self.txtSabor.delete(0, tkinter.END)
                self.txtSabor.insert(0, valores[2])
                self.txtColor.delete(0, tkinter.END)
                self.txtColor.insert(0, valores[3])
                self.txtCantidad.delete(0, tkinter.END)
                self.txtCantidad.insert(0, valores[4])



        def borrar_elemento(_):
            for i in self.tabla.tabla.selection():
                self.controladores.eliminar(self.tabla.tabla.item(i)['values'][0])
                self.tabla.tabla.delete(i)
                self.limpiar_campos()
                messagebox.showinfo("Éxito", "Eliminado correctamente.")


        self.txtMarca.bind("<KeyRelease>", lambda event: self.controladores.validar_marca(event, self.txtMarca))
        self.txtSabor.bind("<KeyRelease>", lambda event: self.controladores.validar_sabor(event, self.txtSabor))
        self.txtColor.bind("<KeyRelease>", lambda event: self.controladores.validar_color(event, self.txtColor))
        self.txtCantidad.bind("<KeyRelease>", lambda event: self.controladores.validar_cantidad(event, self.txtCantidad))
        self.txtID.bind("<KeyRelease>", lambda event: self.controladores.validar_id(event, self.txtID))
        self.tabla.tabla.bind('<<Treeviewselect>>', seleccionar_elemento)
        self.tabla.tabla.bind('<Delete>', borrar_elemento)



        self.root.protocol("WM_DELETE_WINDOW", self.controladores.el_usuario_quiere_salir)

        self.root.mainloop()
    
    def actulizar(self, id, marca, sabor, color, cantidad):
        self.controladores.actualizar(id, marca, sabor, color, cantidad)

    def limpiar_campos(self):
        self.txtMarca.delete(0, tkinter.END)
        self.txtSabor.delete(0, tkinter.END)
        self.txtColor.delete(0, tkinter.END)
        self.txtCantidad.delete(0, tkinter.END)
        self.txtID.delete(0, tkinter.END)
        self.txtMarca.focus_set()