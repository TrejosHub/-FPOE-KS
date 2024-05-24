import tkinter as tk

class Modelos:
    def __init__(self, material, altura, peso, estilo, id):
        self.material = tk.StringVar(value=material)
        self.altura = tk.StringVar(value=altura)
        self.peso = tk.StringVar(value=peso)
        self.estilo = tk.StringVar(value=estilo)
        self.id = tk.StringVar(value=id)