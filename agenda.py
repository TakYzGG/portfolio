import tkinter as tk
from tkinter.messagebox import showerror

# crear ventana principal
screen = tk.Tk()
screen.title("Agenda")
screen.resizable(0,0)

# colores y fuente
fondo = "#282726"
texto = "#d6cab0"
fondo_alt = "#54504c"
fuente = ("Ubuntu Mono", 10, "bold")

padx = 2
pady = 2

screen.config(bg=fondo)

# crear variables de contral
nombre = tk.StringVar()
apellido = tk.StringVar()
correo = tk.StringVar()
telefono = tk.StringVar()
agregar = tk.StringVar()
eliminar = tk.StringVar()
count = 1

# crear frames para organizar el ui
izquierda = tk.Frame(screen, bg=fondo)
izquierda.pack(side=tk.LEFT)

derecha = tk.Frame(screen, bg=fondo)
derecha.pack(side=tk.RIGHT)

# pedir datos al usuario
titulo_izquierda = tk.Label(izquierda, text="Datos", bg=fondo, fg=texto, font=fuente)
titulo_izquierda.grid(row=0, column=0, padx=padx, pady=pady, sticky="ew")

label_nombre = tk.Label(izquierda, text="Ingresar nombre: ", bg=fondo, fg=texto, font=fuente)
label_nombre.grid(row=1, column=0, padx=padx, pady=pady,)
entry_nombre = tk.Entry(izquierda, textvariable=nombre, bg=fondo_alt, fg=texto, font=fuente)
entry_nombre.grid(row=1, column=1, padx=padx, pady=pady)

label_apellido = tk.Label(izquierda, text="Ingresar apellido: ", bg=fondo, fg=texto, font=fuente)
label_apellido.grid(row=2, column=0, padx=padx, pady=pady)
entry_apellido = tk.Entry(izquierda, textvariable=apellido, bg=fondo_alt, fg=texto, font=fuente)
entry_apellido.grid(row=2, column=1, padx=padx, pady=pady)

label_correo = tk.Label(izquierda, text="Ingresar correo: ", bg=fondo, fg=texto, font=fuente)
label_correo.grid(row=3, column=0, padx=padx, pady=pady)
entry_correo = tk.Entry(izquierda, textvariable=correo, bg=fondo_alt, fg=texto, font=fuente)
entry_correo.grid(row=3, column=1, padx=padx, pady=pady)

label_telefono = tk.Label(izquierda, text="Ingresar telefono: ", bg=fondo, fg=texto, font=fuente)
label_telefono.grid(row=4, column=0, padx=padx, pady=pady)
entry_telefono = tk.Entry(izquierda, textvariable=telefono, bg=fondo_alt, fg=texto, font=fuente)
entry_telefono.grid(row=4, column=1, padx=padx, pady=pady)

# crear un separador
tk.Label(screen, bg=fondo, bd=6).pack()

# crear la agenda
titulo_derecha = tk.Label(derecha, text="Agenda", bg=fondo, fg=texto, font=fuente)
titulo_derecha.grid(row=0, column=0, columnspan=3, padx=padx, pady=pady, sticky="ew")

fechas = tk.Listbox(derecha, width=50, bg=fondo_alt, fg=texto, font=fuente)
fechas.grid(row=1, column=0, columnspan=3, padx=padx, pady=pady)

# crear una funcion para agregar elementos
def agregar_elementos():
    global count
    nom = nombre.get()
    ape = apellido.get()
    cor = correo.get()
    tel = telefono.get()
    fechas.insert(tk.END, f"{count}. {nom}, {ape}, {cor}, {tel}")
    count += 1
    
    nombre.set("")
    apellido.set("")
    correo.set("")
    telefono.set("")

elemento_nuevo_boton = tk.Button(izquierda, text="Agregar", bg=fondo, fg=texto, activebackground=fondo_alt, activeforeground=texto, font=fuente, relief="solid", command=agregar_elementos)
elemento_nuevo_boton.grid(row=5, column=0, columnspan=2, sticky="e", padx=padx, pady=pady)

# crear una funcion para eliminar elementos
def eliminar_elementos():
    global count
    elementos = fechas.get(0, tk.END)
    index = int(eliminar.get()) - 1

    if len(elementos) > index: fechas.delete(index)
    else: showerror("Error", "El elemento no esta en la agenda")
    eliminar.set("")
    count -= 1

elemento_eliminar_label = tk.Label(derecha, text="Elemento a eliminar: ", bg=fondo, fg=texto, font=fuente)
elemento_eliminar_label.grid(row=3, column=0, padx=padx, pady=pady)

elemento_eliminar_entry = tk.Entry(derecha, textvariable=eliminar, bg=fondo_alt, fg=texto, font=fuente)
elemento_eliminar_entry.grid(row=3, column=1, padx=padx, pady=pady)

elemento_eliminar_boton = tk.Button(derecha, text="Eliminar", bg=fondo, fg=texto, activebackground=fondo_alt, activeforeground=texto, font=fuente, relief="solid", command=eliminar_elementos)
elemento_eliminar_boton.grid(row=3,column=2, padx=padx, pady=pady)

# bucle principal
screen.mainloop()
