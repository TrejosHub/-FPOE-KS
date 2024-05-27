import tkinter
from Controladores.controladores import Controladores
import requests
# from .tablas import Tabla


class Vista():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Papitas")
        self.root.geometry("400x530")
        self.root.resizable(0, 0)


        self.labelTitulo = tkinter.Label(self.root, text="Diligencie el Formulario")
        self.labelTitulo.grid(column=0, row=0, padx=15, pady=15, columnspan=2)

        self.labelMarca = tkinter.Label(self.root, text="Marca")
        self.labelMarca.grid(column=0, row=1, padx=20, pady=20)
        self.txtMarca = tkinter.Entry(self.root, width=30)
        self.txtMarca.grid(column=1, row=1)

        self.labelOcultoNombre = tkinter.Label(self.root, text="")
        self.labelOcultoNombre.grid(column=0, row=2, columnspan= 2)

        self.labelSabor = tkinter.Label(self.root, text="Sabor")
        self.labelSabor.grid(column=0, row=3, padx=20, pady=20)
        self.txtSabor = tkinter.Entry(self.root, width=30)
        self.txtSabor.grid(column=1, row=3)

        self.labelOcultoApellido = tkinter.Label(self.root, text="")
        self.labelOcultoApellido.grid(column=0, row=4, columnspan= 2)

        self.labelColor = tkinter.Label(self.root, text="Color")
        self.labelColor.grid(column=0, row=5, padx=20, pady=20)
        self.txtColor = tkinter.Entry(self.root, width=30)
        self.txtColor.grid(column=1, row=5)

        self.labelCorreoOculto = tkinter.Label(self.root, text="")
        self.labelCorreoOculto.grid(column=0, row=6, columnspan= 2)

        self.labelCantidad = tkinter.Label(self.root, text="Cantidad")
        self.labelCantidad.grid(column=0, row=7, padx=20, pady=20)
        self.txtCantidad = tkinter.Entry(self.root, width=30)
        self.txtCantidad.grid(column=1, row=7)

        self.labelEdadOculto = tkinter.Label(self.root, text="")
        self.labelEdadOculto.grid(column=0, row=8, columnspan= 2)

        self.labelID = tkinter.Label(self.root, text="Id: ")
        self.labelID.grid(column=0, row=9, padx=20, pady=20)
        self.txtID = tkinter.Entry(self.root, text="")
        self.txtID.grid(column=1, row=10)

        self.labelIDOculto = tkinter.Label(self.root, text="")
        self.labelIDOculto.grid(column=0, row=10, columnspan= 2)

        # self.labelIDtabla = tkinter.Label(self.root, text="Tabla")
        # self.labelIDtabla.grid(column=0, row=10, padx=15, pady=15, columnspan=2)
        # self.txtIDtabla = tkinter.Entry(self.root, width=30)
        # self.txtIDtabla.grid(column=1, row=10)
        # self.tabla.tabla.grid(column=0, row=14, columnspan=3, padx=15, pady=15)


        self.controladores = Controladores(self)


        botonDiligenciar = tkinter.Button(self.root, text="Diligenciar", command=self.controladores.diligenciar)
        botonDiligenciar.grid(column=0, row=11, columnspan=2, padx=15, pady=15)

        botonConsultar = tkinter.Button(self.root, text="Consultar", command=lambda: self.controladores.boton_consultar(self.txtID.get()))
        botonConsultar.grid(column=1, row=11, columnspan=2, padx=15, pady=15)

        botonConsultarTodo = tkinter.Button(self.root, text="Consultar Todo:", command=self.controladores.boton_consultar_todo)
        botonConsultarTodo.grid(column=2, row=11, columnspan=2, padx=15, pady=15)

        botonConsultarFiltro = tkinter.Button(self.root, text="Filtar", command=self.controladores.boton_filtrar)
        botonConsultarFiltro.grid(column=3, row=11, columnspan=2, padx=15, pady=15)
    
        self.txtMarca.bind("<KeyRelease>", lambda event: self.controladores.validar_marca(event, self.txtMarca))
        self.txtSabor.bind("<KeyRelease>", lambda event: self.controladores.validar_sabor(event, self.txtSabor))
        self.txtColor.bind("<KeyRelease>", lambda event: self.controladores.validar_color(event, self.txtColor))
        self.txtCantidad.bind("<KeyRelease>", lambda event: self.controladores.validar_cantidad(event, self.txtCantidad))
        self.txtID.bind("<KeyRelease>", lambda event: self.controladores.validar_id(event, self.txtID))
        # self.tabla.tabla.bind('<<Treeviewselect>>', seleccionar_elemento)
        # self.tabla.tabla.bind('<Delete>', borrar_elemento)



        self.root.protocol("WM_DELETE_WINDOW", self.controladores.el_usuario_quiere_salir)

        self.root.mainloop()