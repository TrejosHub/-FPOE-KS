import tkinter.messagebox as messagebox
import requests
import tkinter
from Modelos.servicios import Servicios

class ValidarRegistarServicios:
    def __init__(self, vista):
        self.vista = vista
        self.servicio = Servicios("", "", "", "")
        self.url = "http://localhost:8000/v1/servicio"

    def validar_nombre_servicio(self, event, widget):
        nombreServicioValidado = widget.get()
        if not nombreServicioValidado.replace(" ", "").isalpha():
            self.vista.lblOcultoNombreServicio.config(text="Error: El nombre solo debe contener letras.", fg="red")
        else:
            self.vista.lblOcultoNombreServicio.config(text="")
    
    def validar_cedula_servicio(self, event, widget):
        cedulaServicioValidada = widget.get()
        if not cedulaServicioValidada.isdigit():
            self.vista.lblOcultoCedulaServicio.config(text="Error: La cédula debe ser un número.", fg="red")
        else:
            self.vista.lblOcultoCedulaServicio.config(text="")

    def validar_descripcion(self, event, widget):
        descripcionValidada = widget.get()
        if not descripcionValidada.replace(" ", "").isalnum():
            self.vista.lblOcultoDescripcion.config(text="Error: La descripción solo debe contener letras, números y/o espacios.", fg="red")
        else:
            self.vista.lblOcultoDescripcion.config(text="")

    def validar_valor(self, event, widget):
        valorValidado = widget.get()
        if not valorValidado.isdigit():
            self.vista.lblOcultoValor.config(text="Error: El valor debe ser un número.", fg="red")
        else:
            self.vista.lblOcultoValor.config(text="")

    def diligenciarServicio(self):
        nombre = self.vista.txtNombreServicio.get()
        cedula = self.vista.txtCedulaServicio.get()
        descripcion = self.vista.txtDescripcion.get()
        valor = self.vista.txtValor.get()

        if not (nombre and cedula and descripcion and valor):
            messagebox.showerror("Error", "Todos los campos deben estar completos.")
            return

        if not nombre.replace(" ", "").isalpha():
            messagebox.showerror("Error", "El nombre solo debe contener letras.")
            return

        if not cedula.isdigit():
            messagebox.showerror("Error", "La cédula debe ser un número.")
            return

        if not descripcion.replace(" ", "").isalnum():
            return

        if not valor.isdigit():
            messagebox.showerror("Error", "El valor debe ser un número.")
            return

        self.servicio.nombre_servicio.set(nombre)
        self.servicio.cedula.set(cedula)
        self.servicio.descripcion.set(descripcion)
        self.servicio.valor.set(valor)

        data = {
            "nombre_servicio": nombre,
            "cedula": cedula,
            "descripcion": descripcion,
            "valor": valor
        }

        response = requests.post("http://localhost:8000/v1/servicio", data=data)
        messagebox.showinfo("Éxito", "Diligenciado correctamente.")

        self.vista.txtNombreServicio.delete(0, tkinter.END)
        self.vista.txtCedulaServicio.delete(0, tkinter.END)
        self.vista.txtDescripcion.delete(0, tkinter.END)
        self.vista.txtValor.delete(0, tkinter.END)
        self.vista.txtIDServicio.delete(0, tkinter.END)
        self.vista.txtNombreServicio.focus_set()

        self.boton_consultar_todo_servicio()

    def actualizar_servicio(self, id, nombre, cedula, descripcion, valor):
        id = self.vista.txtIDServicio.get()
        nombre = self.vista.txtNombreServicio.get()
        cedula = self.vista.txtCedulaServicio.get()
        descripcion = self.vista.txtDescripcion.get()
        valor = self.vista.txtValor.get()

        if not (nombre and cedula and descripcion and valor):
            messagebox.showerror("Error", "Todos los campos deben estar completos.")
            return

        if not nombre.replace(" ", "").isalpha():
            messagebox.showerror("Error", "El nombre solo debe contener letras.")
            return

        if not cedula.isdigit():
            messagebox.showerror("Error", "La cédula debe ser un número.")
            return

        if not descripcion.replace(" ", "").isalnum():
            return

        if not valor.isdigit():
            messagebox.showerror("Error", "El valor debe ser un número.")
            return

        self.servicio.nombre_servicio.set(nombre)
        self.servicio.cedula.set(cedula)
        self.servicio.descripcion.set(descripcion)
        self.servicio.valor.set(valor)

        data = {
            "nombre_servicio": nombre,
            "cedula": cedula,
            "descripcion": descripcion,
            "valor": valor
        }

        response = requests.put(self.url + '/' + id + '/', data=data)
        messagebox.showinfo("Éxito", "Actualizado correctamente.")

        self.vista.txtNombreServicio.delete(0, tkinter.END)
        self.vista.txtCedulaServicio.delete(0, tkinter.END)
        self.vista.txtDescripcion.delete(0, tkinter.END)
        self.vista.txtValor.delete(0, tkinter.END)
        self.vista.txtIDServicio.delete(0, tkinter.END)
        self.vista.txtNombreServicio.focus_set()

        self.boton_consultar_todo_servicio()

    def consultar_servicio(self, cedula):
        resultado = requests.get(self.url + '/' + str(cedula))
        return resultado.json()

    def eliminar_servicio(self, cedula):
        resultado = requests.delete(self.url + '/' + str(cedula))
        return resultado.status_code

    def consultar_todo_servicio(self, nombre_servicio, cedula, descripcion, valor):
        url = self.url + "?"
        if nombre_servicio:
            url += "nombre_servicio=" + nombre_servicio + "&"
        if cedula:
            url += "cedula=" + cedula + "&"
        if descripcion:
            url += "descripcion=" + descripcion + "&"
        if valor:
            url += "valor=" + valor + "&"

        print(url)
        resultado = requests.get(url)
        return resultado.json()
    
    def boton_consultar_todo_servicio(self):
        nombre_servicio = self.vista.txtNombreServicio.get()
        cedula = self.vista.txtCedulaServicio.get()
        descripcion = self.vista.txtDescripcion.get()
        valor = self.vista.txtValor.get()

        data = []
        resultado = self.consultar_todo_servicio(nombre_servicio, cedula, descripcion, valor)
        for elemento in resultado:
            data.append((elemento.get('id'), elemento.get('nombre_servicio'), elemento.get('cedula'), elemento.get('descripcion'), elemento.get('valor')))
        self.vista.tabla.refrescar(data)

    def boton_consultar_cedula_servicio(self, cedula):
        nombre_servicio = self.vista.txtNombreServicio.get()
        cedula = self.vista.txtCedulaServicio.get()
        descripcion = self.vista.txtDescripcion.get()
        valor = self.vista.txtValor.get()

        data = []
        resultado = self.consultar_todo_servicio(nombre_servicio, cedula, descripcion, valor)
        for elemento in resultado:
            data.append((elemento.get('id'), elemento.get('nombre_servicio'), elemento.get('cedula'), elemento.get('descripcion'), elemento.get('valor')))
        self.vista.tabla.refrescar(data)

        self.vista.txtNombreServicio.delete(0, tkinter.END)
        self.vista.txtCedulaServicio.delete(0, tkinter.END)
        self.vista.txtDescripcion.delete(0, tkinter.END)
        self.vista.txtValor.delete(0, tkinter.END)
        self.vista.txtIDServicio.delete(0, tkinter.END)
        self.vista.txtNombreServicio.focus_set()

    def boton_filtrar_servicio(self):
        nombre_servicio = self.vista.txtNombreServicio.get()
        cedula = self.vista.txtCedulaServicio.get()
        descripcion = self.vista.txtDescripcion.get()
        valor = self.vista.txtValor.get()

        data = []
        resultado = self.consultar_todo_servicio(nombre_servicio, cedula, descripcion, valor)
        for elemento in resultado:
            data.append((elemento.get('id'), elemento.get('nombre_servicio'), elemento.get('cedula'), elemento.get('descripcion'), elemento.get('valor')))
        self.vista.tabla.refrescar(data)

        self.vista.txtNombreServicio.delete(0, tkinter.END)
        self.vista.txtCedulaServicio.delete(0, tkinter.END)
        self.vista.txtDescripcion.delete(0, tkinter.END)
        self.vista.txtValor.delete(0, tkinter.END)
        self.vista.txtIDServicio.delete(0, tkinter.END)
        self.vista.txtNombreServicio.focus_set()

    def boton_eliminar_servicio(self, id):
        resultado = requests.delete(self.url + '/' + str(id))
        return resultado.status_code