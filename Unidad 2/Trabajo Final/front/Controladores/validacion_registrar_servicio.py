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
        if not descripcionValidada.replace(" ", "").isalpha():
            self.vista.lblOcultoDescripcion.config(text="Error: La descripción solo debe contener letras.", fg="red")
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
        cedula_cliente = self.vista.txtCedulaServicio.get()
        descripcion = self.vista.txtDescripcion.get()
        valor = self.vista.txtValor.get()

        if not (nombre and cedula_cliente and descripcion and valor):
            messagebox.showerror("Error", "Todos los campos deben estar completos.")
            return

        if not nombre.replace(" ", "").isalpha():
            messagebox.showerror("Error", "El nombre solo debe contener letras.")
            return

        if not cedula_cliente.isdigit():
            messagebox.showerror("Error", "La cédula debe ser un número.")
            return
        
        if not descripcion.replace(" ", "").isalpha():
            messagebox.showerror("Error", "La descripcion solo debe contener letras.")
            return

        if not valor.isdigit():
            messagebox.showerror("Error", "El valor debe ser un número.")
            return

        messagebox.showinfo("Éxito", "Diligenciado correctamente.")

        self.servicio.nombre_servicio.set(nombre)
        self.servicio.cedula_cliente.set(cedula_cliente)
        self.servicio.descripcion.set(descripcion)
        self.servicio.valor.set(valor)

        data = {
            "nombre_servicio": nombre,
            "cedula_cliente": cedula_cliente,
            "descripcion": descripcion,
            "valor": valor
        }

        response = requests.post("http://localhost:8000/v1/servicio", data=data)
        print(response.status_code)
        print(response.content)