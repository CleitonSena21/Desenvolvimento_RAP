import tkinter as tk
from tkinter import messagebox
import math

def calcular_raizes():
    try:

        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a == 0:
            messagebox.showerror("Erro", "O coeficiente 'a' não pode ser zero.")
            return
        
        discriminante = b**2 - 4*a*c
        
        if discriminante > 0:
            raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
            raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
            resultado = f"As raízes são: {raiz1:.2f} e {raiz2:.2f}"
        elif discriminante == 0:
            raiz = -b / (2 * a)
            resultado = f"A raiz dupla é: {raiz:.2f}"
        else:
            resultado = "Não há raízes reais."
        
        label_resultado.config(text=resultado)
    
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

janela = tk.Tk()
janela.title("Calculadora de Raízes")

label_a = tk.Label(janela, text="Coeficiente a:")
label_a.pack()

entry_a = tk.Entry(janela)
entry_a.pack()

label_b = tk.Label(janela, text="Coeficiente b:")
label_b.pack()

entry_b = tk.Entry(janela)
entry_b.pack()

label_c = tk.Label(janela, text="Coeficiente c:")
label_c.pack()

entry_c = tk.Entry(janela)
entry_c.pack()

button_calcular = tk.Button(janela, text="Calcular Raízes", command=calcular_raizes)
button_calcular.pack()

label_resultado = tk.Label(janela, text="")
label_resultado.pack()

janela.mainloop()