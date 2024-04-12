#CLASE 6 KEVIN

import tkinter
from tkinter.messagebox import askyesno, showerror, showinfo
import requests

root = tkinter.Tk()
root.title("API Silla")
root.geometry("350x450")
root.resizable(0, 0)

material = tkinter.StringVar()
altura = tkinter.StringVar()  
peso = tkinter.StringVar()    
estilo = tkinter.StringVar()

labelTitulo = tkinter.Label(root, text="Datos de la Silla")
labelTitulo.grid(column=0, row=0, padx=15, pady=15, columnspan=2)

labelMaterial = tkinter.Label(root, text="Material")
labelMaterial.grid(column=0, row=1, padx=20, pady=20)
txtMaterial = tkinter.Entry(root, width=30, textvariable=material)
txtMaterial.grid(column=1, row=1)

labelOcultoMaterial = tkinter.Label(root, text="")
labelOcultoMaterial.grid(column=0, row=2, columnspan=2)

labelAltura = tkinter.Label(root, text="Altura (cms)")
labelAltura.grid(column=0, row=3, padx=20, pady=20)
txtAltura = tkinter.Entry(root, width=30, textvariable=altura)
txtAltura.grid(column=1, row=3)

labelOcultoAltura = tkinter.Label(root, text="")
labelOcultoAltura.grid(column=0, row=4, columnspan=2)

labelPeso = tkinter.Label(root, text="Peso (kg)")
labelPeso.grid(column=0, row=5, padx=20, pady=20)
txtPeso = tkinter.Entry(root, width=30, textvariable=peso)
txtPeso.grid(column=1, row=5)

labelPesoOculto = tkinter.Label(root, text="")
labelPesoOculto.grid(column=0, row=6, columnspan=2)

labelEstilo = tkinter.Label(root, text="Estilo")
labelEstilo.grid(column=0, row=7, padx=20, pady=20)
txtEstilo = tkinter.Entry(root, width=30, textvariable=estilo)
txtEstilo.grid(column=1, row=7)

labelEstiloOculto = tkinter.Label(root, text="")
labelEstiloOculto.grid(column=0, row=8, columnspan=2)

def el_usuario_quiere_salir():
    if askyesno("Salir de la Aplicación", "¿Seguro que deseas cerrar la App?"):
        root.destroy()

def validar_material(event):
    materialValidado = txtMaterial.get()
    if not materialValidado.isalpha():
        labelOcultoMaterial.config(
            text="Error: El material solo debe contener letras.", fg="red")
    else:
        labelOcultoMaterial.config(text="")

def validar_altura(event):
    alturaValidada = txtAltura.get()
    if not alturaValidada.replace('.', '', 1).isdigit():
        labelOcultoAltura.config(
            text="Error: La altura debe ser un número decimal (.)", fg="red")
    else:
        labelOcultoAltura.config(text="")

def validar_peso(event):
    pesoValidado = txtPeso.get()
    if not pesoValidado.replace('.', '', 1).isdigit():  
        labelPesoOculto.config(
            text="Error: El peso debe ser un número decimal (.)", fg="red")
    else:
        labelPesoOculto.config(text="")

def validar_estilo(event):
    estiloValidado = txtEstilo.get()
    if not estiloValidado.isalpha():
        labelEstiloOculto.config(
            text="Error: El estilo solo debe contener letras.", fg="red")
    else:
        labelEstiloOculto.config(text="")

def diligenciar(event):
    if not (txtMaterial.get() and txtAltura.get() and txtPeso.get() and txtEstilo.get()):
        showerror("Error", "Todos los campos deben estar completos")
        return

    if not material.get().isalpha():
        showerror("Error", "El material solo debe contener letras")
        return

    if not estilo.get().isalpha():
        showerror("Error", "El estilo solo debe contener letras")
        return

    if not txtPeso.get().replace('.', '', 1).isdigit():
        showerror("Error", "El peso debe ser un número decimal (.)")
        return

    if not txtAltura.get().replace('.', '', 1).isdigit(): 
        showerror("Error", "La altura debe ser un número decimal (.)")
        return

    showinfo("Éxito", "Formulario diligenciado correctamente.")
    data = {
        "material": material.get(),
        "altura": altura.get(),
        "peso": peso.get(),
        "estilo": estilo.get()
    }

    response = requests.post("http://localhost:8000/v1/silla", data=data)
    print(response.status_code)
    print(response.content)

botonDiligenciar = tkinter.Button(root, text="Diligenciar")
botonDiligenciar.grid(column=0, row=11, columnspan=2, padx=15, pady=15)
botonDiligenciar.bind("<Button-1>", diligenciar)

txtMaterial.bind("<KeyRelease>", validar_material)
txtAltura.bind("<KeyRelease>", validar_altura)
txtEstilo.bind("<KeyRelease>", validar_estilo)
txtPeso.bind("<KeyRelease>", validar_peso)

root.protocol("WM_DELETE_WINDOW", el_usuario_quiere_salir)

root.mainloop()