import tkinter
from tkinter.messagebox import askyesno

root = tkinter.Tk()
root.title("Datos Personales")
root.geometry("350x350")
root.resizable(0, 0)

nombre = tkinter.StringVar()
apellido = tkinter.StringVar()
correo = tkinter.StringVar()
edad = tkinter.StringVar()
fNacimiento = tkinter.StringVar()

labelNombre = tkinter.Label(root, text="Nombre")
labelNombre.grid(column=0, row=0, padx=20, pady=20)
txtNombre = tkinter.Entry(root, width=30, textvariable=nombre)
txtNombre.grid(column=1, row=0)

labelApellido = tkinter.Label(root, text="Apellido")
labelApellido.grid(column=0, row=1, padx=20, pady=20)
txtApellido = tkinter.Entry(root, width=30, textvariable=apellido)
txtApellido.grid(column=1, row=1)

labelCorreo = tkinter.Label(root, text="Correo")
labelCorreo.grid(column=0, row=2, padx=20, pady=20)
txtCorreo = tkinter.Entry(root, width=30, textvariable=correo)
txtCorreo.grid(column=1, row=2)

labelEdad = tkinter.Label(root, text="Edad")
labelEdad.grid(column=0, row=3, padx=20, pady=20)
txtEdad = tkinter.Entry(root, width=30, textvariable=edad)
txtEdad.grid(column=1, row=3)

labelFnacimiento = tkinter.Label(root, text="Fecha de Nacimiento")
labelFnacimiento.grid(column=0, row=4, padx=20, pady=20)
txtFnacimiento = tkinter.Entry(root, width=30, textvariable=fNacimiento)
txtFnacimiento.grid(column=1, row=4)

def el_usuario_quiere_salir():
    if askyesno("Salir de la Aplicación", "¿Seguro que deseas cerrar la App?"):
        root.destroy()

def validar_nombre(event):
    nombreValidado = txtNombre.get()
    if not nombreValidado.isalpha():
        print("Error: El nombre solo debe contener letras.")

def validar_apellido(event):
    apellidoValidado = txtApellido.get()
    if not apellidoValidado.isalpha():
        print("Error: El apellido solo debe contener letras.")

def validar_edad(event):
    edadValidada = txtEdad.get()
    if not edadValidada.isdigit():
        print("Error: La edad debe ser un número.")

def validar_fecha(event):
    fechaValidada = txtFnacimiento.get()
    if len(fechaValidada) == 2 or len(fechaValidada) == 5:
        txtFnacimiento.insert(tkinter.END, '/')
    for numero in fechaValidada:
        if not numero.isdigit() and numero != '/':
            print("Error: La fecha de nacimiento debe contener solo números.")
            break

def validar_correo(event):
    correoValidado = txtCorreo.get()
    caracteresCorreo = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.@"
    if any(caracter not in caracteresCorreo for caracter in correoValidado):
        print("Error: El correo solo permite 'Letras', 'Números', '@' y '.'")

def diligenciar(event):
    print("Diligenciado")

botonEnviar = tkinter.Button(root, text="Diligenciar")
botonEnviar.grid(column=0, row=5, columnspan=2, padx=15, pady=15)
botonEnviar.bind("<Button-1>", diligenciar)

txtNombre.bind("<FocusOut>", validar_nombre)
txtApellido.bind("<FocusOut>", validar_apellido)
txtEdad.bind("<FocusOut>", validar_edad)
txtFnacimiento.bind("<KeyRelease>", validar_fecha)
txtCorreo.bind("<FocusOut>", validar_correo)

root.protocol("WM_DELETE_WINDOW", el_usuario_quiere_salir)

root.mainloop()