import tkinter
from tkinter.messagebox import askyesno
from tkinter import messagebox as mb

root = tkinter.Tk()
root.title("Datos Personales")
root.geometry("400x530")
root.resizable(0, 0)

nombre = tkinter.StringVar()
apellido = tkinter.StringVar()
correo = tkinter.StringVar()
edad = tkinter.StringVar()
fNacimiento = tkinter.StringVar()

labelTitulo = tkinter.Label(root, text="Diligencie el Formulario")
labelTitulo.grid(column=0, row=0, padx=15, pady=15, columnspan=2)

labelNombre = tkinter.Label(root, text="Nombre")
labelNombre.grid(column=0, row=1, padx=20, pady=20)
txtNombre = tkinter.Entry(root, width=30, textvariable=nombre)
txtNombre.grid(column=1, row=1)

labelOcultoNombre = tkinter.Label(root, text="")
labelOcultoNombre.grid(column=0, row=2, columnspan= 2)

labelApellido = tkinter.Label(root, text="Apellido")
labelApellido.grid(column=0, row=3, padx=20, pady=20)
txtApellido = tkinter.Entry(root, width=30, textvariable=apellido)
txtApellido.grid(column=1, row=3)

labelOcultoApellido = tkinter.Label(root, text="")
labelOcultoApellido.grid(column=0, row=4, columnspan= 2)

labelCorreo = tkinter.Label(root, text="Correo")
labelCorreo.grid(column=0, row=5, padx=20, pady=20)
txtCorreo = tkinter.Entry(root, width=30, textvariable=correo)
txtCorreo.grid(column=1, row=5)

labelCorreoOculto = tkinter.Label(root, text="")
labelCorreoOculto.grid(column=0, row=6, columnspan= 2)

labelEdad = tkinter.Label(root, text="Edad")
labelEdad.grid(column=0, row=7, padx=20, pady=20)
txtEdad = tkinter.Entry(root, width=30, textvariable=edad)
txtEdad.grid(column=1, row=7)

labelEdadOculto = tkinter.Label(root, text="")
labelEdadOculto.grid(column=0, row=8, columnspan= 2)

labelFnacimiento = tkinter.Label(root, text="Fecha de Nacimiento")
labelFnacimiento.grid(column=0, row=9, padx=20, pady=20)
txtFnacimiento = tkinter.Entry(root, width=30, textvariable=fNacimiento)
txtFnacimiento.grid(column=1, row=9)

labelNacimientoOculto = tkinter.Label(root, text="")
labelNacimientoOculto.grid(column=0, row=10,columnspan= 2)

def el_usuario_quiere_salir():
    if askyesno("Salir de la Aplicación", "¿Seguro que deseas cerrar la App?"):
        root.destroy()

def validar_nombre(event):
    nombreValidado = txtNombre.get()
    if not nombreValidado.isalpha():
        labelOcultoNombre.config(text="Error: El nombre solo debe contener letras.", fg="red")
    else:
        labelOcultoNombre.config(text="")

def validar_apellido(event):
    apellidoValidado = txtApellido.get()
    if not apellidoValidado.isalpha():
        labelOcultoApellido.config(text="Error: El apellido solo debe contener letras.", fg= "red")
    else:
        labelOcultoApellido.config(text="")

def validar_edad(event):
    edadValidada = txtEdad.get()
    if not edadValidada.isdigit():
        labelEdadOculto.config(text="Error: La edad debe ser un número.", fg= "red")
    else:
        labelEdadOculto.config(text="")

def validar_fecha(event):
    fechaValidada = txtFnacimiento.get()
    if len(fechaValidada) == 2 or len(fechaValidada) == 5:
        txtFnacimiento.insert(tkinter.END, '/')
    for numero in fechaValidada:
        if not numero.isdigit() and numero != '/':
            labelNacimientoOculto.config(text="Error: La fecha de nacimiento debe contener solo números.", fg= "red")
            break
    else:
        labelNacimientoOculto.config(text="")

def validar_correo(event):
    correoValidado = txtCorreo.get()
    caracteresCorreo = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.@"
    if any(caracter not in caracteresCorreo for caracter in correoValidado):
        labelCorreoOculto.config(text="Error: El correo solo permite 'Letras', 'Números', '@' y '.'", fg= "red")
    else:
        labelCorreoOculto.config(text="")

def diligenciar(event):
    if not (txtNombre.get() and txtApellido.get() and txtCorreo.get() and txtEdad.get() and txtFnacimiento.get()):
        mb.showerror("Error", "Todos los campos deben estar completos")
        return

    if not nombre.get().isalpha():
        mb.showerror("Error", "El nombre solo debe contener letras")
    elif not apellido.get().isalpha():
        mb.showerror("Error", "El apellido solo debe contener letras")
    elif not edad.get().isdigit():
        mb.showerror("Error", "La edad debe ser un número")
    elif "@" not in correo.get() or "." not in correo.get():
        mb.showerror("Error", "El correo no es válido o está incompleto")
    else:
        partes_fecha = fNacimiento.get().split('/')
        if not (len(partes_fecha) == 3 and all(numero.isdigit() for numero in partes_fecha)):
            mb.showerror("Error", "La fecha de nacimiento no es válida (Recuerde, debe ser formato DD/MM/AAAA)")
        else:
            mb.showinfo("Éxito", "Formulario diligenciado correctamente.")

botonDiligenciar = tkinter.Button(root, text="Diligenciar")
botonDiligenciar.grid(column=0, row=11, columnspan=2, padx=15, pady=15)
botonDiligenciar.bind("<Button-1>", diligenciar)

txtNombre.bind("<KeyRelease>", validar_nombre)
txtApellido.bind("<KeyRelease>", validar_apellido)
txtEdad.bind("<KeyRelease>", validar_edad)
txtFnacimiento.bind("<KeyRelease>", validar_fecha)
txtCorreo.bind("<KeyRelease>", validar_correo)

root.protocol("WM_DELETE_WINDOW", el_usuario_quiere_salir)

root.mainloop()