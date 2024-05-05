import tkinter as tk

class Modelos():
    def __init__(self, marca, sabor, color, cantidad):
        self.marca = tk.StringVar(value=marca)
        self.sabor = tk.StringVar(value=sabor)
        self.color = tk.StringVar(value=color)
        self.cantidad = tk.StringVar(value=cantidad)