import tkinter as tk
from tkinter import messagebox

def click_boton(event):
    texto = event.widget.cget("text")
    if texto == "=":
        try:
            resultado = eval(str(pantalla.get()))
            pantalla.delete(0, tk.END)
            pantalla.insert(tk.END, resultado)
        except Exception as e:
            messagebox.showerror("Error", "Operación inválida")
            pantalla.delete(0, tk.END)
    elif texto == "C":
        pantalla.delete(0, tk.END)
    else:
        pantalla.insert(tk.END, texto)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Básica")

# Crear la pantalla de la calculadora
pantalla = tk.Entry(ventana, font="Arial 20", bd=5, relief=tk.SUNKEN, justify=tk.RIGHT)
pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Crear los botones
botones = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

fila = 1
columna = 0

for boton in botones:
    b = tk.Button(ventana, text=boton, font="Arial 18", width=5, height=2, relief=tk.RAISED)
    b.grid(row=fila, column=columna, padx=5, pady=5)
    b.bind("<Button-1>", click_boton)
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

# Ejecutar el bucle principal
ventana.mainloop()