import tkinter.messagebox as mb
import requests
from .comunicacion import Comunicacion

class Controladores():
    def __init__(self, vista):
        self.vista = vista
        self.url = 'http://localhost:8000/v1/papitas'


    def el_usuario_quiere_salir(self):
        if mb.askyesno("Salir de la Aplicación", "¿Seguro que deseas cerrar la App?"):
            self.vista.root.destroy()

    def validar_marca(self, event, widget):
        marcaValidada = widget.get()
        if not marcaValidada.isalpha():
            self.vista.labelOcultoNombre.config(text="Error: La marca solo debe contener letras.", fg="red")
        else:
             self.vista.labelOcultoNombre.config(text="")

    def validar_sabor(self, event, widget):
        apellidoValidado = widget.get()
        if not apellidoValidado.isalpha():
            self.vista.labelOcultoApellido.config(text="Error: El sabor solo debe contener letras.", fg= "red")
        else:
            self.vista.labelOcultoApellido.config(text="")

    def validar_color(self, event, widget):
        colorvalidado = widget.get()
        if not colorvalidado.isalpha():
            self.vista.labelEdadOculto.config(text="Error: El color solo debe contener letras.", fg= "red")
        else:
            self.vista.labelEdadOculto.config(text="")

    def validar_cantidad(self, event, widget):
        cantidadvalidada = widget.get()
        if not cantidadvalidada.isdigit():
            self.vista.labelEdadOculto.config(text="Error: La cantidad solo debe contener nuneros.", fg= "red")
        else:
            self.vista.labelEdadOculto.config(text="")

    def validar_id(self, event, widget):
        idvalidado = widget.get()
        if not idvalidado.isdigit():
            self.vista.labelIDOculto.config(text="Error: El ID solo debe contener nuneros.", fg= "red")
        else:
            self.vista.labelIDOculto.config(text="")

    def diligenciar(self):
        marca = self.vista.txtMarca.get()
        sabor = self.vista.txtSabor.get()
        color = self.vista.txtColor.get()
        cantidad = self.vista.txtCantidad.get()

        if not (marca and sabor and color and cantidad):
            mb.showerror("Error", "Todos los campos deben estar completos")
            return

        if not marca.isalpha():
            mb.showerror("Error", "El nombre solo debe contener letras")
            return
        
        if not sabor.isalpha():
            mb.showerror("Error", "El sabor solo debe contener letras")
            return
        
        if not color.isalpha():
            mb.showerror("Error", "El color solo debe contener letras")
            return
        
        if not cantidad.isdigit():
            mb.showerror("Error", "La cantidad solo debe contener numeros")
            return


        mb.showinfo("Éxito", "Formulario diligenciado correctamente.")

        data = {
        "marca":marca,
        "sabor":sabor,
        "color":color,
        "cantidad":cantidad
        }

        response = requests.post("http://127.0.0.1:8000/v1/papitas", data=data)
        print(response.status_code)
        print(response.content)   


    def boton_consultar(self, id):
        resultado = self.consultar(id)
        print(resultado)

    def boton_consultar_todo(self):
        marca = self.vista.txtMarca.get()
        sabor = self.vista.txtSabor.get()
        color = self.vista.txtColor.get()
        cantidad = self.vista.txtCantidad.get()
        resultado = self.consultar_todo(marca, sabor, color, cantidad)
        print(resultado)

    def boton_filtrar(self):
        marca = self.vista.txtMarca.get()
        sabor = self.vista.txtSabor.get()
        color = self.vista.txtColor.get()
        cantidad = self.vista.txtCantidad.get()
        resultados = self.consultar_todo(marca, sabor, color, cantidad)
        self.mostrar_resultado(resultados)

    def mostrar_resultado(self, resultados):
        for resultado in resultados:
            print(resultado)

    def consultar(self, id):
        resultado = requests.get(self.url + '/' + str(id))
        return resultado.json()
        
    def consultar_todo(self, marca, sabor, color, cantidad):
        url = self.url
        print(type(sabor))
        if marca != '':
            url = url + 'marca' + str(marca) + "&"
        if sabor  != '':
            url = url + 'sabor' + str(sabor) + "&"
        if color  != '':
            url = url + 'color' + str(color) + "&"
        if cantidad  != '':
            url = url + 'cantidad' + str(cantidad) + "&"
        print(url)
        resultado = requests.get(url)
        return resultado.json()

