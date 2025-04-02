# Transformar coordenadas del nether al overword
import tkinter as tk
from tkinter.messagebox import showerror

def coords_nether():
    error = False
    x = entrys[0]
    y = entrys[1]

    try:
        x = int(x.get())
        y = int(y.get())
    except:
        error = True

    if not error: resultado_overword.config(text=f"Coordenadas en el nether: X: {int(x / 8)}, Y: {int(y / 8)}")
    elif error: showerror("Error 01", "No se pueden poner letras en las coordenadas")

def coords_overword():
    error = False
    x = entrys[2]
    y = entrys[3]

    try:
        x = int(x.get())
        y = int(y.get())
    except:
        error = True

    if not error: resultado_nether.config(text=f"Coordenadas en el overword: X: {int(x * 8)}, Y: {int(y * 8)}")
    elif error: showerror("Error 01", "No se pueden poner letras en las coordenadas")

# crear la ventana del programa
screen = tk.Tk()
screen.title("Calcular coordenadas minecraft")

# Actualizar la ventana para obtener su tamaño real
screen.update_idletasks()

# Obtener tamaño de la ventana
x_ventana = screen.winfo_width()
y_ventana = screen.winfo_height()

# Obtener tamaño de la pantalla
x_pantalla = screen.winfo_screenwidth()
y_pantalla = screen.winfo_screenheight()

# Calcular coordenadas para centrar
x = (x_pantalla // 2) - (x_ventana // 2)
y = (y_pantalla // 2) - (y_ventana // 2)

# Aplicar geometría
screen.geometry(f"+{x}+{y}")

# fuente y colores
fuente = ("Ubuntu Mono", 10, "bold")

bg = "#2C3333"
bg_alt = "#395B64"
fg = "#E7F6F2"
fg_alt = "#262828"
extra = "#A5C9CA"

padx = 4
pady = 4

# config de la ventana
screen.config(bg=bg)

# crear labels para x, y
label_layout = (("X overword: ", 0, 0),
                ("Y overword: ", 1, 0),
                #("Cordenadas en el nether: ", 0, 2),
                ("", 2, 0),
                ("X nether: ", 3, 0),
                ("Y nether: ", 4, 0))
                #("Cordenadas en el overword: ", 3, 2))

for texto, fila, columna in label_layout:
    label = tk.Label(screen, text=texto, font=fuente, bg=bg, fg=fg)
    label.grid(row=fila, column=columna, padx=padx, pady=pady)

# crear entradas para poner x, y
entrys = []

entry_layout = ((0, 1), # x overword
                (1, 1), # y overword
                (3, 1), # x nether
                (4, 1)) # y nether

for fila, columna in entry_layout:
    entry = tk.Entry(screen, width=6, font=fuente, bg=bg_alt, fg=fg)
    entry.grid(row=fila, column=columna, padx=padx, pady=pady)
    entrys.append(entry)

# crear label para mostrar el resultado de las coords
resultado_overword = tk.Label(screen, text="Coordenadas en el nether", font=fuente, bg=bg, fg=fg)
resultado_overword.grid(row=0, column=2, padx=padx, pady=pady)

resultado_nether = tk.Label(screen, text="Coordenadas en el overword", font=fuente, bg=bg, fg=fg)
resultado_nether.grid(row=3, column=2, padx=padx, pady=pady)

# crear botones para calcular las coordenadas
boton_overword = tk.Button(screen, text="Calcular coordenadas", command=coords_nether, relief="solid", font=fuente, bg=bg_alt, fg=fg, activebackground=extra, activeforeground=fg_alt)
boton_overword.grid(row=1, column=2, padx=padx, pady=pady)

boton_nether = tk.Button(screen, text="Calcular coordenadas", command=coords_overword, relief="solid", font=fuente, bg=bg_alt, fg=fg, activebackground=extra, activeforeground=fg_alt)
boton_nether.grid(row=4, column=2, padx=padx, pady=pady)

# bucle principal de la ventana
screen.mainloop()
