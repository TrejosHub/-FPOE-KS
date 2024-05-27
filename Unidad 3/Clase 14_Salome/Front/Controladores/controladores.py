import tkinter
import requests
from Vistas.tablas import Tabla
from tkinter import messagebox


class Controladores():
    def __init__(self, vista):
        self.vista = vista
        self.url = 'http://localhost:8000/v1/papitas'
        self.tabla = Tabla


    def el_usuario_quiere_salir(self):
        if messagebox.askyesno("Salir de la Aplicación", "¿Seguro que deseas cerrar la App?"):
            self.vista.root.destroy()

    def validar_marca(self, event, widget):
        marcaValidada = widget.get()
        if not marcaValidada.isalpha():
            self.vista.labelOcultoMarca.config(text="Error: La marca solo debe contener letras.", fg="red")
        else:
            self.vista.labelOcultoMarca.config(text="")

    def validar_sabor(self, event, widget):
        saborValidado = widget.get()
        if not saborValidado.isalpha():
            self.vista.labelOcultoSabor.config(text="Error: El sabor solo debe contener letras.", fg="red")
        else:
            self.vista.labelOcultoSabor.config(text="")

    def validar_color(self, event, widget):
        colorValidado = widget.get()
        if not colorValidado.isalpha():
            self.vista.labelColorOculto.config(text="Error: El color solo debe contener letras.", fg="red")
        else:
            self.vista.labelColorOculto.config(text="")

    def validar_cantidad(self, event, widget):
        cantidadValidada = widget.get()
        if not cantidadValidada.replace('.', '', 1).isdigit():
            self.vista.labelCantidadOculto.config(text="Error: La cantidad debe ser un número decimal (.)", fg="red")
        else:
            self.vista.labelCantidadOculto.config(text="")

    def validar_id(self, event, widget):
        idValidado = widget.get()
        if not idValidado.isdigit():
            self.vista.labelIDOculto.config(text="Error: El ID debe ser un número.", fg="red")
        else:
            self.vista.labelIDOculto.config(text="")

    def diligenciar(self):
        marca = self.vista.txtMarca.get()
        sabor = self.vista.txtSabor.get()
        color = self.vista.txtColor.get()
        cantidad = self.vista.txtCantidad.get()

        if not (marca and sabor and color and cantidad):
            messagebox.showerror("Error", "Todos los campos deben estar completos")
            return

        if not marca.isalpha():
            messagebox.showerror("Error", "La marca solo debe contener letras")
            return

        if not sabor.isalpha():
            messagebox.showerror("Error", "El sabor solo debe contener letras")
            return

        if not color.isalpha():
            messagebox.showerror("Error", "El color solo debe contener letras")
            return

        if not cantidad.replace('.', '', 1).isdigit():
            messagebox.showerror("Error", "La cantidad debe ser un número decimal (.)")
            return

        data = {
            "marca": marca,
            "sabor": sabor,
            "color": color,
            "cantidad": cantidad
        }

        response = requests.post(self.url, data=data)
        messagebox.showinfo("Éxito", "Guardado correctamente.")

        self.vista.txtMarca.delete(0, tkinter.END)
        self.vista.txtSabor.delete(0, tkinter.END)
        self.vista.txtColor.delete(0, tkinter.END)
        self.vista.txtCantidad.delete(0, tkinter.END)
        self.vista.txtID.delete(0, tkinter.END)
        self.vista.txtMarca.focus_set()

        self.boton_consultar_todo()

    def actualizar(self, id, marca, sabor, color, cantidad):
        id = self.vista.txtID.get()
        marca = self.vista.txtMarca.get()
        sabor = self.vista.txtSabor.get()
        color = self.vista.txtColor.get()
        cantidad = self.vista.txtCantidad.get()

        if not (marca and sabor and color and cantidad):
            messagebox.showerror("Error", "Todos los campos deben estar completos")
            return

        if not marca.isalpha():
            messagebox.showerror("Error", "La marca solo debe contener letras")
            return

        if not sabor.isalpha():
            messagebox.showerror("Error", "El sabor solo debe contener letras")
            return

        if not color.isalpha():
            messagebox.showerror("Error", "El color solo debe contener letras")
            return

        if not cantidad.replace('.', '', 1).isdigit():
            messagebox.showerror("Error", "La cantidad debe ser un número decimal (.)")
            return

        data = {
            "marca": marca,
            "sabor": sabor,
            "color": color,
            "cantidad": cantidad
        }

        response = requests.put(self.url + '/' + id + '/', data=data)
        messagebox.showinfo("Éxito", "Actualizado correctamente.")

        self.vista.txtMarca.delete(0, tkinter.END)
        self.vista.txtSabor.delete(0, tkinter.END)
        self.vista.txtColor.delete(0, tkinter.END)
        self.vista.txtCantidad.delete(0, tkinter.END)
        self.vista.txtID.delete(0, tkinter.END)
        self.vista.txtMarca.focus_set()

        self.boton_consultar_todo()

    def boton_consultar(self, id):
        data = []
        resultado = self.consultar(id)

        if isinstance(resultado, dict):
            data.append((resultado.get('id'), resultado.get('marca'), resultado.get('sabor'), resultado.get('color'), resultado.get('cantidad')))

        self.vista.tabla.refrescar(data)

        self.vista.txtID.delete(0, tkinter.END)
        self.vista.txtMarca.focus_set()

    def boton_consultar_todo(self):
        marca = self.vista.txtMarca.get()
        sabor = self.vista.txtSabor.get()
        color = self.vista.txtColor.get()
        cantidad = self.vista.txtCantidad.get()

        data = []
        resultado = self.consultar_todo(marca, sabor, color, cantidad)
        for elemento in resultado:
            data.append((elemento.get('id'), elemento.get('marca'), elemento.get('sabor'), elemento.get('color'), elemento.get('cantidad')))
        self.vista.tabla.refrescar(data)

    def boton_filtrar(self):
        marca = self.vista.txtMarca.get()
        sabor = self.vista.txtSabor.get()
        color = self.vista.txtColor.get()
        cantidad = self.vista.txtCantidad.get()

        data = []
        resultado = self.consultar_todo(marca, sabor, color, cantidad)
        for elemento in resultado:
            data.append((elemento.get('id'), elemento.get('marca'), elemento.get('sabor'), elemento.get('color'), elemento.get('cantidad')))
        self.vista.tabla.refrescar(data)

        self.vista.txtMarca.delete(0, tkinter.END)
        self.vista.txtSabor.delete(0, tkinter.END)
        self.vista.txtColor.delete(0, tkinter.END)
        self.vista.txtCantidad.delete(0, tkinter.END)
        self.vista.txtID.delete(0, tkinter.END)
        self.vista.txtMarca.focus_set()

    def consultar(self, id):
        resultado = requests.get(self.url + '/' + str(id))
        return resultado.json()

    def eliminar(self, id):
        resultado = requests.delete(self.url + '/' + str(id))
        return resultado.status_code

    def consultar_todo(self, marca, sabor, color, cantidad):
        url = self.url + "?"
        if marca:
            url += "marca=" + marca + "&"
        if sabor:
            url += "sabor=" + sabor + "&"
        if color:
            url += "color=" + color + "&"
        if cantidad:
            url += "cantidad=" + cantidad + "&"
        print(url)
        resultado = requests.get(url)
        return resultado.json()