import tkinter.messagebox as messagebox
import requests
import tkinter
from Modelos.cliente import Clientes
from Vistas.tabla_cliente import TablaCliente

class ValidarRegistarClientes:
    def __init__(self, vista):
        self.vista = vista
        self.cliente = Clientes("", "", "", "", "")
        self.url = "http://localhost:8000/v1/cliente"

    def validar_nombre(self, event, widget):
        nombre_validado = widget.get()
        if not nombre_validado.replace(" ", "").isalpha():
            self.vista.lblOcultoNombre.config(text="Error: El nombre solo debe contener letras.", fg="red")
        else:
            self.vista.lblOcultoNombre.config(text="")

    def validar_apellido(self, event, widget):
        apellido_validado = widget.get()
        if not apellido_validado.replace(" ", "").isalpha():
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
        correo_validado = widget.get()
        if "@" not in correo_validado:
            self.vista.lblOcultoCorreo.config(text="Error: Formato NO válido (@?).", fg="red")
        else:
            self.vista.lblOcultoCorreo.config(text="")

    def diligenciar_cliente(self):
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

        response = requests.post(self.url, data=data)
        messagebox.showinfo("Éxito", "Diligenciado correctamente.")

        self.vista.txtNombre.delete(0, tkinter.END)
        self.vista.txtApellido.delete(0, tkinter.END)
        self.vista.txtCedula.delete(0, tkinter.END)
        self.vista.txtTelefono.delete(0, tkinter.END)
        self.vista.txtCorreo.delete(0, tkinter.END)
        self.vista.txtIDCliente.delete(0, tkinter.END)
        self.vista.txtNombre.focus_set()

        self.boton_consultar_todo_cliente()

    def actualizar_cliente(self, id, nombre, apellido, cedula, telefono, correo):
        id = self.vista.txtIDCliente.get()
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

        response = requests.put(self.url + '/' + id + '/', data=data)
        messagebox.showinfo("Éxito", "Actualizado correctamente.")

        self.vista.txtNombre.delete(0, tkinter.END)
        self.vista.txtApellido.delete(0, tkinter.END)
        self.vista.txtCedula.delete(0, tkinter.END)
        self.vista.txtTelefono.delete(0, tkinter.END)
        self.vista.txtCorreo.delete(0, tkinter.END)
        self.vista.txtIDCliente.delete(0, tkinter.END)
        self.vista.txtNombre.focus_set()

        self.boton_consultar_todo_cliente()

    def consultar_cliente(self, cedula):
        resultado = requests.get(self.url + '/' + str(cedula))
        return resultado.json()

    def eliminar_cliente(self, cedula):
        resultado = requests.delete(self.url + '/' + str(cedula))
        return resultado.status_code

    def consultar_todo_clientes(self, nombre, apellido, cedula, telefono, correo):
        url = self.url + "?"
        if nombre:
            url += "nombre=" + nombre + "&"
        if apellido:
            url += "apellido=" + apellido + "&"
        if cedula:
            url += "cedula=" + cedula + "&"
        if telefono:
            url += "telefono=" + telefono + "&"
        if correo:
            url += "correo=" + correo + "&"

        print(url)
        resultado = requests.get(url)
        return resultado.json()

    def boton_consultar_todo_cliente(self):
        nombre = self.vista.txtNombre.get()
        apellido = self.vista.txtApellido.get()
        cedula = self.vista.txtCedula.get()
        telefono = self.vista.txtTelefono.get()
        correo = self.vista.txtCorreo.get()

        data = []
        resultado = self.consultar_todo_clientes(nombre, apellido, cedula, telefono, correo)
        for elemento in resultado:
            data.append((elemento.get('id'), elemento.get('nombre'), elemento.get('apellido'), elemento.get('cedula'), elemento.get('telefono'), elemento.get('correo')))
        self.vista.tabla.refrescar(data)

    def boton_consultar_cedula(self, cedula):
        cedula = self.vista.txtCedula.get()

        data = []
        resultado = self.filtrar_cedula_cliente(cedula)
        for elemento in resultado:
            data.append((elemento.get('id'), elemento.get('nombre'), elemento.get('apellido'), elemento.get('cedula'), elemento.get('telefono'), elemento.get('correo')))
        self.vista.tabla.refrescar(data)

        if resultado:
            messagebox.showinfo("Exito", "Cliente Encontrado")
        else:
            messagebox.showwarning("Error", "Cliente no encontrado")

        self.vista.txtNombre.delete(0, tkinter.END)
        self.vista.txtApellido.delete(0, tkinter.END)
        self.vista.txtCedula.delete(0, tkinter.END)
        self.vista.txtTelefono.delete(0, tkinter.END)
        self.vista.txtCorreo.delete(0, tkinter.END)
        self.vista.txtIDCliente.delete(0, tkinter.END)
        self.vista.txtNombre.focus_set()

    def boton_filtrar_cliente(self):
        nombre = self.vista.txtNombre.get()
        apellido = self.vista.txtApellido.get()
        cedula = self.vista.txtCedula.get()
        telefono = self.vista.txtTelefono.get()
        correo = self.vista.txtCorreo.get()
        
        data = []
        resultado = self.consultar_todo_clientes(nombre, apellido, cedula, telefono, correo)
        for elemento in resultado:
            data.append((elemento.get('id'), elemento.get('nombre'), elemento.get('apellido'), elemento.get('cedula'), elemento.get('telefono'), elemento.get('correo')))
        self.vista.tabla.refrescar(data)

        if resultado:
            messagebox.showinfo("Exito", "Cliente Encontrado")
        else:
            messagebox.showwarning("Error", "Cliente no encontrado")

        self.vista.txtNombre.delete(0, tkinter.END)
        self.vista.txtApellido.delete(0, tkinter.END)
        self.vista.txtCedula.delete(0, tkinter.END)
        self.vista.txtTelefono.delete(0, tkinter.END)
        self.vista.txtCorreo.delete(0, tkinter.END)
        self.vista.txtIDCliente.delete(0, tkinter.END)
        self.vista.txtNombre.focus_set()

    def boton_eliminar_cliente(self, id):
        resultado = requests.delete(self.url + '/' + str(id))
        return resultado.status_code

    def filtrar_cedula_cliente(self, cedula):
        url = self.url + "?"
        if cedula:
            url += "cedula=" + cedula + "&"

        print(url)
        resultado = requests.get(url)
        return resultado.json()