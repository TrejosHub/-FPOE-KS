import tkinter.messagebox as messagebox
import requests
from Modelos.servicios import Servicios

class ValidarRegistarServicios:
    def __init__(self, vista):
        self.vista = vista
        self.servicio = Servicios("", "", "", "")

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

        response = requests.get("http://localhost:8000/v1/cliente")
        if response.status_code != 200:
            messagebox.showerror("Error", "Error al obtener la lista de clientes.")
            return
        clientes = response.json()

        cedula_existe = False
        for cliente in clientes:
            if cliente['cedula'] == int(cedula):
                cedula_existe = True
                break

        if not cedula_existe:
            messagebox.showerror("Error", "La cédula ingresada no corresponde a un cliente registrado.")
            return

        if not descripcion.replace(" ", "").isalnum():
            return

        if not valor.isdigit():
            messagebox.showerror("Error", "El valor debe ser un número.")
            return

        messagebox.showinfo("Éxito", "Diligenciado correctamente.")

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
        print(response.status_code)
        print(response.content)