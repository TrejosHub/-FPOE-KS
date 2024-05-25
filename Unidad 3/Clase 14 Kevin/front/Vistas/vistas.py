import tkinter
import tkinter.messagebox as messagebox
from Controladores.controladores import Controladores
from .tabla import Tabla

class Vista:
    def __init__(self):

        titulos = ["Identificador", "Material", "Altura", "Peso", "Estilo"]
        columnas = ['id', 'material', 'altura', 'peso', 'estilo']
        data = []

        self.root = tkinter.Tk()
        self.root.title("API Silla")
        
        self.labelTitulo = tkinter.Label(self.root, text="Datos de la Silla")
        self.labelTitulo.grid(column=0, row=0, padx=15, pady=15, columnspan=2)

        self.labelMaterial = tkinter.Label(self.root, text="Material")
        self.labelMaterial.grid(column=0, row=1, padx=20, pady=20)
        self.txtMaterial = tkinter.Entry(self.root, width=30)
        self.txtMaterial.grid(column=1, row=1)

        self.labelOcultoMaterial = tkinter.Label(self.root, text="")
        self.labelOcultoMaterial.grid(column=0, row=2, columnspan=2)

        self.labelAltura = tkinter.Label(self.root, text="Altura (cms)")
        self.labelAltura.grid(column=0, row=3, padx=20, pady=20)
        self.txtAltura = tkinter.Entry(self.root, width=30)
        self.txtAltura.grid(column=1, row=3)

        self.labelOcultoAltura = tkinter.Label(self.root, text="")
        self.labelOcultoAltura.grid(column=0, row=4, columnspan=2)

        self.labelPeso = tkinter.Label(self.root, text="Peso (kg)")
        self.labelPeso.grid(column=0, row=5, padx=20, pady=20)
        self.txtPeso = tkinter.Entry(self.root, width=30)
        self.txtPeso.grid(column=1, row=5)

        self.labelPesoOculto = tkinter.Label(self.root, text="")
        self.labelPesoOculto.grid(column=0, row=6, columnspan=2)

        self.labelEstilo = tkinter.Label(self.root, text="Estilo")
        self.labelEstilo.grid(column=0, row=7, padx=20, pady=20)
        self.txtEstilo = tkinter.Entry(self.root, width=30)
        self.txtEstilo.grid(column=1, row=7)

        self.labelEstiloOculto = tkinter.Label(self.root, text="")
        self.labelEstiloOculto.grid(column=0, row=8, columnspan=2)

        self.labelID = tkinter.Label(self.root, text="ID: ")
        self.labelID.grid(column=0, row=10, padx=20, pady=20)
        self.txtID = tkinter.Entry(self.root, width=30)
        self.txtID.grid(column=1, row=10)

        self.labelIDOculto = tkinter.Label(self.root, text="")
        self.labelIDOculto.grid(column=0, row=11, columnspan=2)

        self.controladores = Controladores(self)

        self.botonDiligenciar = tkinter.Button(self.root, text="Guardar", command=self.controladores.diligenciar)
        self.botonDiligenciar.grid(column=0, row=9, columnspan=2, padx=15, pady=15)

        self.botonConsultar = tkinter.Button(self.root, text="Consultar por ID", command=lambda: self.controladores.boton_consultar(self.txtID.get()))
        self.botonConsultar.grid(column=2, row=1, padx=15, pady=15)

        self.botonConsultarTodo = tkinter.Button(self.root, text="Consultar Todo", command=self.controladores.boton_consultar_todo)
        self.botonConsultarTodo.grid(column=2, row=3, padx=15, pady=15)

        self.botonConsultarFiltro = tkinter.Button(self.root, text="Consultar por Filtro", command=self.controladores.boton_filtrar)
        self.botonConsultarFiltro.grid(column=2, row=5, padx=15, pady=15)

        self.botonActualizar = tkinter.Button(self.root, text="Actualizar", command=lambda: self.actualizar(self.txtID.get(), self.txtMaterial.get(), self.txtAltura.get(), self.txtPeso.get(), self.txtEstilo.get()))
        self.botonActualizar.grid(column=2, row=7, padx=15, pady=15)

        self.botonLimpiar = tkinter.Button(self.root, text="Limpiar Campos", command=self.limpiar_campos)
        self.botonLimpiar.grid(column=1, row=9, padx=15, pady=15)

        def borrar_elemento(_):
            for i in self.tabla.tabla.selection():
                self.controladores.eliminar(self.tabla.tabla.item(i)['values'][0])
                self.tabla.tabla.delete(i)
                self.limpiar_campos()
                messagebox.showinfo("Éxito", "Eliminado correctamente.")

        self.botonEliminar = tkinter.Button(self.root, text="Eliminar", command=lambda: borrar_elemento(None))
        self.botonEliminar.grid(column=2, row=9, padx=15, pady=15)

        self.tabla = Tabla(self.root, titulos, columnas, data)
        self.tabla.tabla.grid(column=0, row=11, columnspan=3, padx=15, pady=15)

        self.controladores.boton_consultar_todo()

        def seleccionar_elemento(_):
            for i in self.tabla.tabla.selection():
                valores = self.tabla.tabla.item(i)['values']
                self.txtID.delete(0, tkinter.END)
                self.txtID.insert(0, valores[0])
                self.txtMaterial.delete(0, tkinter.END)
                self.txtMaterial.insert(0, valores[1])
                self.txtAltura.delete(0, tkinter.END)
                self.txtAltura.insert(0, valores[2])
                self.txtPeso.delete(0, tkinter.END)
                self.txtPeso.insert(0, valores[3])
                self.txtEstilo.delete(0, tkinter.END)
                self.txtEstilo.insert(0, valores[4])

        self.txtMaterial.bind("<KeyRelease>", lambda event: self.controladores.validar_material(event, self.txtMaterial))
        self.txtAltura.bind("<KeyRelease>", lambda event: self.controladores.validar_altura(event, self.txtAltura))
        self.txtEstilo.bind("<KeyRelease>", lambda event: self.controladores.validar_estilo(event, self.txtEstilo))
        self.txtPeso.bind("<KeyRelease>", lambda event: self.controladores.validar_peso(event, self.txtPeso))
        self.txtID.bind("<KeyRelease>", lambda event: self.controladores.validar_id(event, self.txtID))
        self.tabla.tabla.bind('<<TreeviewSelect>>', seleccionar_elemento)
        self.tabla.tabla.bind('<Delete>', borrar_elemento)

        self.root.protocol("WM_DELETE_WINDOW", self.controladores.el_usuario_quiere_salir)

        self.root.mainloop()

    def actualizar(self, id, material, altura, peso, estilo):
        self.controladores.actualizar(id, material, altura, peso, estilo)

    def limpiar_campos(self):
        self.txtMaterial.delete(0, tkinter.END)
        self.txtAltura.delete(0, tkinter.END)
        self.txtEstilo.delete(0, tkinter.END)
        self.txtPeso.delete(0, tkinter.END)
        self.txtID.delete(0, tkinter.END)
        self.txtMaterial.focus_set()