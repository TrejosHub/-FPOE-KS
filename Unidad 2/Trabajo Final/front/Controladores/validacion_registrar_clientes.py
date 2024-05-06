import tkinter.messagebox as messagebox
import requests
from Modelos.cliente import Clientes

class ValidarRegistarClientes:
    def __init__(self, vista):
        self.vista = vista
        self.cliente = Clientes("", "", "", "", "")

    def validar_nombre(self, event, widget):
        nombre_validado = widget.get()
        if not nombre_validado.replace(" ", "").isalpha():
            self.vista.lblOcultoNombre.config(text="Error: El nombre solo debe contener letras.", fg="red")
        else:
            self.vista.lblOcultoNombre.config(text="")

    def validar_apellido(self, event, widget): 
        apellidoValidado = widget.get()         
        if not apellidoValidado.replace(" ", "").isalpha():
            self.vista.lblOcultoApellido.config(text="Error: El apellido solo debe contener letras.", fg="red")
        else:
            self.vista.lblOcultoApellido.config(text="")
    
    def validar_cedula(self, event, widget):
        cedula_validada = widget.get()
        if not cedula_validada.isdigit():
            self.vista.lblOcultoCedula.config(text="Error: La cédula debe ser un número.", fg="red")
        else:
            self.vista.lblOcultoCedula.config(text="")
    
    def validar_telefono(self, event, widget):
        telefono_validado = widget.get()
        if not telefono_validado.isdigit():
            self.vista.lblOcultoTelefono.config(text="Error: El teléfono debe ser un número.", fg="red")
        else:
            self.vista.lblOcultoTelefono.config(text="")

    def validar_correo(self, event, widget): 
        correoValidado = widget.get()         
        if "@" not in correoValidado:
            self.vista.lblOcultoCorreo.config(text="Error: Formato NO válido (@?).", fg="red")
        else:
            self.vista.lblOcultoCorreo.config(text="")

    def diligenciar(self):
        nombre = self.vista.txtNombre.get()
        apellido = self.vista.txtApellido.get()
        cedula = self.vista.txtCedula.get()
        telefono = self.vista.txtTelefono.get()
        correo = self.vista.txtCorreo.get()

        if not (nombre and apellido and cedula and telefono and correo):
            messagebox.showerror("Error", "Todos los campos deben estar completos.")
            return

        if not nombre.replace(" ", "").isalpha():
            messagebox.showerror("Error", "El nombre solo debe contener letras.")
            return

        if not apellido.replace(" ", "").isalpha():
            messagebox.showerror("Error", "El apellido solo debe contener letras.")
            return

        if not cedula.isdigit():
            messagebox.showerror("Error", "La cédula debe ser un número.")
            return
        
        if not telefono.isdigit():
            messagebox.showerror("Error", "El teléfono debe ser un número.")
            return
        
        if "@" not in correo:
            messagebox.showerror("Error", "Formato NO válido (@?).")
            return

        messagebox.showinfo("Éxito", "Diligenciado correctamente.")

        self.cliente.nombre.set(nombre)
        self.cliente.apellido.set(apellido)
        self.cliente.cedula.set(cedula)
        self.cliente.telefono.set(telefono)
        self.cliente.correo.set(correo)

        data = {
            "nombre": nombre,
            "apellido": apellido,
            "cedula": cedula,
            "telefono": telefono,
            "correo": correo
        }

        response = requests.post("http://localhost:8000/v1/cliente", data=data)
        print(response.status_code)
        print(response.content)