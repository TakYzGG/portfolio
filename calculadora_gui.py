# Write a Python program to design a simple calculator application using Tkinter with buttons for numbers and arithmetic operations. 

# impornar tkinter
import tkinter as tk

# funciones de los botones
def actualizar_calc(valor):
    texto_actual = display_var.get()
    if texto_actual == "0": display_var.set(valor)
    else: display_var.set(texto_actual + valor)

def calcular_resultado():
    try:
        resultado = eval(display_var.get())
        display_var.set(resultado)
    except:
        display_var.set("Error")

def limpiar_pantalla():
    display_var.set("0")


# crear ventana principal
screen = tk.Tk()
screen.title("Ejercicio 13")
screen.resizable(0,0)

# fuente y colores
fuente = ("Ubuntu Mono", 16, "bold")

bg = "#151515"
fg = "#ffffff"

bg_boton = "#2979ff"
fg_boton = "#151515"

bg_boton_p = "#00e5ff"

# config de la ventana
screen.config(bg=bg)

# label para mostrar las operaciones
display_var = tk.StringVar()
display_var.set("0")

display_label = tk.Label(screen, textvariable=display_var, font=fuente,
                         bg=bg, fg=fg, anchor="e", padx=10)
display_label.grid(row=0, column=0, columnspan=4)

# crear botones
boton_layout = [("1",1,0), ("2",1,1), ("3",1,2), ("+",1,3),
                ("4",2,0), ("5",2,1), ("6",2,2), ("-",2,3),
                ("7",3,0), ("8",3,1), ("9",3,2), ("*",3,3),
                ("0",4,0), (".",4,1), ("=",4,2), ("/",4,3)]

for texto, fila, columna in boton_layout:
    boton = tk.Button(screen, text=texto, font=fuente, bg=bg_boton, fg=fg_boton, activebackground=bg_boton_p,
                      activeforeground=fg_boton, relief="solid",
                      command=lambda t=texto: actualizar_calc(t) if t != "=" else calcular_resultado())
    boton.grid(row=fila, column=columna)

# boton para limpiar la pantalla
limpiar_pantalla = tk.Button(text="Limpiar", font=fuente, bg="#d500f9", fg=fg_boton, activebackground="#ff1744",
                             activeforeground=fg_boton, relief="solid", command=limpiar_pantalla)
limpiar_pantalla.grid(row=5, column=0, columnspan=3)

# bucle principal de la ventana
screen.mainloop()
