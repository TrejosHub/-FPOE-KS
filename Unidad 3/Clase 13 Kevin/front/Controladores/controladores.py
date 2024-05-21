import tkinter.messagebox as messagebox
import requests

class Controladores:
    def __init__(self, vista):
        self.vista = vista
        self.url = "http://localhost:8000/v1/silla"

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

        messagebox.showinfo("Éxito", "Formulario diligenciado correctamente.")
        data = {
            "material": material,
            "altura": altura,
            "peso": peso,
            "estilo": estilo
        }

        response = requests.post("http://localhost:8000/v1/silla", data=data)
        print(response.status_code)
        print(response.content)

    def consultar(self, id):
        resultado = requests.get(self.url + '/' + str(id))
        return resultado.json()
    
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