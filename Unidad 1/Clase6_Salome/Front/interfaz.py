import tkinter
from tkinter.messagebox import askyesno
from tkinter import messagebox as mb
import requests

root = tkinter.Tk()
root.title("Datos Personales")
root.geometry("400x530")
root.resizable(0, 0)

marca = tkinter.StringVar()
sabor = tkinter.StringVar()
color = tkinter.StringVar()
cantidad = tkinter.StringVar()


labelTitulo = tkinter.Label(root, text="Diligencie el Formulario")
labelTitulo.grid(column=0, row=0, padx=15, pady=15, columnspan=2)

labelMarca = tkinter.Label(root, text="Marca")
labelMarca.grid(column=0, row=1, padx=20, pady=20)
txtMarca = tkinter.Entry(root, width=30, textvariable=marca)
txtMarca.grid(column=1, row=1)

labelOcultoNombre = tkinter.Label(root, text="")
labelOcultoNombre.grid(column=0, row=2, columnspan= 2)

labelSabor = tkinter.Label(root, text="Sabor")
labelSabor.grid(column=0, row=3, padx=20, pady=20)
txtSabor = tkinter.Entry(root, width=30, textvariable=sabor)
txtSabor.grid(column=1, row=3)

labelOcultoApellido = tkinter.Label(root, text="")
labelOcultoApellido.grid(column=0, row=4, columnspan= 2)

labelColor = tkinter.Label(root, text="Color")
labelColor.grid(column=0, row=5, padx=20, pady=20)
txtColor = tkinter.Entry(root, width=30, textvariable=color)
txtColor.grid(column=1, row=5)

labelCorreoOculto = tkinter.Label(root, text="")
labelCorreoOculto.grid(column=0, row=6, columnspan= 2)

labelCantidad = tkinter.Label(root, text="Cantidad")
labelCantidad.grid(column=0, row=7, padx=20, pady=20)
txtCantidad = tkinter.Entry(root, width=30, textvariable=cantidad)
txtCantidad.grid(column=1, row=7)

labelEdadOculto = tkinter.Label(root, text="")
labelEdadOculto.grid(column=0, row=8, columnspan= 2)


def el_usuario_quiere_salir():
    if askyesno("Salir de la Aplicación", "¿Seguro que deseas cerrar la App?"):
        root.destroy()

def validar_marca(event):
    marcaValidada = txtMarca.get()
    if not marcaValidada.isalpha():
        labelOcultoNombre.config(text="Error: La marca solo debe contener letras.", fg="red")
    else:
        labelOcultoNombre.config(text="")

def validar_sabor(event):
    apellidoValidado = txtSabor.get()
    if not apellidoValidado.isalpha():
        labelOcultoApellido.config(text="Error: El sabor solo debe contener letras.", fg= "red")
    else:
        labelOcultoApellido.config(text="")

def validar_color(event):
    colorvalidado = txtColor.get()
    if not colorvalidado.isalpha():
        labelEdadOculto.config(text="Error: El color solo debe contener letras.", fg= "red")
    else:
        labelEdadOculto.config(text="")

def validar_cantidad(event):
    cantidadvalidada = txtCantidad.get()
    if not cantidadvalidada.isdigit():
        labelEdadOculto.config(text="Error: La cantidad solo debe contener nuneros.", fg= "red")
    else:
        labelEdadOculto.config(text="")



def diligenciar(event):
    if not (txtMarca.get() and txtSabor.get() and txtColor.get() and txtCantidad.get()):
        mb.showerror("Error", "Todos los campos deben estar completos")
        return

    if not marca.get().isalpha():
        mb.showerror("Error", "El nombre solo debe contener letras")
    elif not sabor.get().isalpha():
        mb.showerror("Error", "El sabor solo debe contener letras")
    elif not color.get().isalpha():
        mb.showerror("Error", "El color solo debe contener letras")
    elif not cantidad.get().isdigit():
        mb.showerror("Error", "La cantidad solo debe contener numeros")
    else:
        mb.showinfo("Éxito", "Formulario diligenciado correctamente.")

    data = {
    "marca":marca.get(),
    "sabor":sabor.get(),
    "color":color.get(),
    "cantidad":cantidad.get()
    }

    response = requests.post("http://127.0.0.1:8000/v1/papitas", data=data)
    print(response.status_code)
    print(response.content)   

botonDiligenciar = tkinter.Button(root, text="Diligenciar")
botonDiligenciar.grid(column=0, row=11, columnspan=2, padx=15, pady=15)
botonDiligenciar.bind("<Button-1>", diligenciar)

txtMarca.bind("<KeyRelease>", validar_marca)
txtSabor.bind("<KeyRelease>", validar_sabor)
txtCantidad.bind("<KeyRelease>", validar_color)
txtCantidad.bind("<KeyRelease>", validar_cantidad)

root.protocol("WM_DELETE_WINDOW", el_usuario_quiere_salir)

root.mainloop()