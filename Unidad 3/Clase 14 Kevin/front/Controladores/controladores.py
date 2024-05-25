import tkinter.messagebox as messagebox
import tkinter
import requests
from Vistas.tabla import Tabla
import tkinter as tk
class Controladores:
    def __init__(self, vista):
        self.vista = vista
        self.url = "http://localhost:8000/v1/silla"
        self.tabla = Tabla

    def el_usuario_quiere_salir(self):
        if messagebox.askyesno("Salir de la Aplicación", "¿Seguro que deseas cerrar la App?"):
            self.vista.root.destroy()
    
    def validar_material(self, event, widget):
        materialValidado = widget.get()
        if not materialValidado.isalpha():
            self.vista.labelOcultoMaterial.config(text="Error: El material solo debe contener letras.", fg="red")
        else:
            self.vista.labelOcultoMaterial.config(text="")
    
    def validar_altura(self, event, widget):
        alturaValidada = widget.get()
        if not alturaValidada.replace('.', '', 1).isdigit():
            self.vista.labelOcultoAltura.config(text="Error: La altura debe ser un número decimal (.)", fg="red")
        else:
            self.vista.labelOcultoAltura.config(text="")
    
    def validar_peso(self, event, widget):
        pesoValidado = widget.get()
        if not pesoValidado.replace('.', '', 1).isdigit():  
            self.vista.labelPesoOculto.config(text="Error: El peso debe ser un número decimal (.)", fg="red")
        else:
            self.vista.labelPesoOculto.config(text="")
    
    def validar_estilo(self, event, widget):
        estiloValidado = widget.get()
        if not estiloValidado.isalpha():
            self.vista.labelEstiloOculto.config(text="Error: El estilo solo debe contener letras.", fg="red")
        else:
            self.vista.labelEstiloOculto.config(text="")

    def validar_id(self, event, widget):
        idValidado = widget.get()
        if not idValidado.isdigit():
            self.vista.labelIDOculto.config(text="Error: El ID debe ser un número.", fg="red")
        else:
            self.vista.labelIDOculto.config(text="")

    def diligenciar(self):
        material = self.vista.txtMaterial.get()
        altura = self.vista.txtAltura.get()
        peso = self.vista.txtPeso.get()
        estilo = self.vista.txtEstilo.get()

        if not (material and altura and peso and estilo):
            messagebox.showerror("Error", "Todos los campos deben estar completos")
            return

        if not material.isalpha():
            messagebox.showerror("Error", "El material solo debe contener letras")
            return

        if not estilo.isalpha():
            messagebox.showerror("Error", "El estilo solo debe contener letras")
            return

        if not peso.replace('.', '', 1).isdigit():
            messagebox.showerror("Error", "El peso debe ser un número decimal (.)")
            return

        if not altura.replace('.', '', 1).isdigit():
            messagebox.showerror("Error", "La altura debe ser un número decimal (.)")
            return

        data = {
            "material": material,
            "altura": altura,
            "peso": peso,
            "estilo": estilo
        }

        response = requests.post("http://localhost:8000/v1/silla", data=data)
        #print(response.status_code)
        #print(response.content)
        messagebox.showinfo("Éxito", "Guardado correctamente.")

        self.vista.txtMaterial.delete(0, tkinter.END)
        self.vista.txtAltura.delete(0, tkinter.END)
        self.vista.txtEstilo.delete(0, tkinter.END)
        self.vista.txtPeso.delete(0, tkinter.END)
        self.vista.txtID.delete(0, tkinter.END)
        self.vista.txtMaterial.focus_set()

        self.boton_consultar_todo()

    def actualizar(self, id, material, altura, peso, estilo):
        id = self.vista.txtID.get()
        material = self.vista.txtMaterial.get()
        altura = self.vista.txtAltura.get()
        peso = self.vista.txtPeso.get()
        estilo = self.vista.txtEstilo.get()

        if not (material and altura and peso and estilo):
            messagebox.showerror("Error", "Todos los campos deben estar completos")
            return

        if not material.isalpha():
            messagebox.showerror("Error", "El material solo debe contener letras")
            return

        if not estilo.isalpha():
            messagebox.showerror("Error", "El estilo solo debe contener letras")
            return

        if not peso.replace('.', '', 1).isdigit():
            messagebox.showerror("Error", "El peso debe ser un número decimal (.)")
            return

        if not altura.replace('.', '', 1).isdigit():
            messagebox.showerror("Error", "La altura debe ser un número decimal (.)")
            return

        data = {
            "material": material,
            "altura": altura,
            "peso": peso,
            "estilo": estilo
        }

        response = requests.put(self.url + '/' + id + '/', data=data)
        #print(response.status_code)
        #print(response.content)
        messagebox.showinfo("Éxito", "Actualizado correctamente.")

        self.vista.txtMaterial.delete(0, tkinter.END)
        self.vista.txtAltura.delete(0, tkinter.END)
        self.vista.txtEstilo.delete(0, tkinter.END)
        self.vista.txtPeso.delete(0, tkinter.END)
        self.vista.txtID.delete(0, tkinter.END)
        self.vista.txtMaterial.focus_set()

        self.boton_consultar_todo()

    def boton_consultar(self, id):
        data = []
        resultado = self.consultar(id)

        if isinstance(resultado, dict):
            data.append((resultado.get('id'), resultado.get('material'), resultado.get('altura'), resultado.get('peso'), resultado.get('estilo')))

        self.vista.tabla.refrescar(data)

        self.vista.txtID.delete(0, tkinter.END)
        self.vista.txtMaterial.focus_set()
        #print(resultado)

    def boton_consultar_todo(self):
        material = self.vista.txtMaterial.get()
        altura = self.vista.txtAltura.get()
        peso = self.vista.txtPeso.get()
        estilo = self.vista.txtEstilo.get()

        data = []
        resultado = self.consultar_todo(material, altura, peso, estilo)
        for elemento in resultado:
            data.append((elemento.get('id'), elemento.get('material'), elemento.get('altura'), elemento.get('peso'), elemento.get('estilo')))
        self.vista.tabla.refrescar(data)
        #print(resultado)

    def boton_filtrar(self):
        material = self.vista.txtMaterial.get()
        altura = self.vista.txtAltura.get()
        peso = self.vista.txtPeso.get()
        estilo = self.vista.txtEstilo.get()

        data = []
        resultado = self.consultar_todo(material, altura, peso, estilo)
        for elemento in resultado:
            data.append((elemento.get('id'), elemento.get('material'), elemento.get('altura'), elemento.get('peso'), elemento.get('estilo')))
        self.vista.tabla.refrescar(data)

        self.vista.txtMaterial.delete(0, tkinter.END)
        self.vista.txtAltura.delete(0, tkinter.END)
        self.vista.txtEstilo.delete(0, tkinter.END)
        self.vista.txtPeso.delete(0, tkinter.END)
        self.vista.txtID.delete(0, tkinter.END)
        self.vista.txtMaterial.focus_set()

    def consultar(self, id):
        resultado = requests.get(self.url + '/' + str(id))
        return resultado.json()
    
    def eliminar(self, id):
        resultado = requests.delete(self.url + '/' + str(id))
        return resultado.status_code
    
    def consultar_todo(self, material, altura, peso, estilo):
        url = self.url + "?"
        if material:
            url += "material=" + material + "&"
        if altura:
            url += "altura=" + altura + "&"
        if peso:
            url += "peso=" + peso + "&"
        if estilo:
            url += "estilo=" + estilo + "&"
        print(url)
        resultado = requests.get(url)
        return resultado.json()