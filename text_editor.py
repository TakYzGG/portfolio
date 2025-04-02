import tkinter as tk
from tkinter.messagebox import showinfo, showwarning
from tkinter import filedialog
from os import path

# funcion para abrir
def abrir(event=None):
    global ruta
    ruta = filedialog.askopenfilename(title="Abrir archivo")
    texto.delete("1.0", tk.END)
    nombre_archivo.config(text=path.basename(ruta))
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            texto.insert(tk.INSERT, linea)

# funcion para crear un archivo nuevo
def nuevo(event=None):
    texto.delete("1.0", tk.END)
    nombre_archivo.config(text="Nuevo")

# funcion para guardar
def guardar(event=None):
    global ruta
    if ruta:
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(texto.get("1.0", tk.END))
    else: guardar_como()

# funcion para guardar como
def guardar_como(event=None):
    global ruta
    ruta = filedialog.asksaveasfilename(title="Guardar archivo")
    if ruta:
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(texto.get("1.0", tk.END))
    else: showwarning("CUIDADO!!!", "No guardaste el archivo")

# funcion para cortar
def cortar(event=None):
    texto.event_generate("<<Cut>>")

# funcion para copiar
def copiar(event=None):
    texto.event_generate("<<Copy>>")

# funcion para pegar
def pegar(event=None):
    texto.event_generate("<<Paste>>")

# funcion para ver la info del programa
def mostrar_info():
    showinfo("Version", f"Version: {version}")

# funcion para personalizar la app
def personalizar(opcion):
    estilos = {
        1: {"fondo": "#282828", "text_color": "#ebdbb2", "fondo_alt": "#383838"},
        2: {"fondo": "#151515", "text_color": "#ffffff", "fondo_alt": "#252525"},
        3: {"fondo": "#2e3440", "text_color": "#d8dee9", "fondo_alt": "#81a1c1"},
    }

    if opcion in estilos:
        tema = estilos[opcion]
        screen.config(bg=tema["fondo"])
        texto.config(bg=tema["fondo_alt"], fg=tema["text_color"])
        nombre_archivo.config(bg=tema["fondo"], fg=tema["text_color"])
        menubar.config(bg=tema["fondo"], fg=tema["text_color"], activebackground=tema["fondo_alt"], activeforeground=tema["text_color"])
        archivomenu.config(bg=tema["fondo"], fg=tema["text_color"], activebackground=tema["fondo_alt"], activeforeground=tema["text_color"])
        editarmenu.config(bg=tema["fondo"], fg=tema["text_color"], activebackground=tema["fondo_alt"], activeforeground=tema["text_color"])
        personalizarmenu.config(bg=tema["fondo"], fg=tema["text_color"], activebackground=tema["fondo_alt"], activeforeground=tema["text_color"])
        acercamenu.config(bg=tema["fondo"], fg=tema["text_color"], activebackground=tema["fondo_alt"], activeforeground=tema["text_color"])



# variables
program_name = "Editor de texto"
version = 1.0
ruta = ""

# crear la ventana principal
screen = tk.Tk()
screen.title(program_name)
screen.resizable(0,0)

# colores y fuente
fondo = "#282726"
text_color = "#d6cab0"
fondo_alt = "#54504c"
fuente = ("Ubuntu Mono", 10, "bold")

padx = 2
pady = 2

screen.config(bg=fondo)

# crear menu
menubar = tk.Menu(screen, bg=fondo, fg=text_color, activebackground=fondo_alt, activeforeground=text_color, font=fuente)
screen.config(menu=menubar)

# menu para archivos
archivomenu = tk.Menu(menubar, tearoff=0, bg=fondo, fg=text_color, activebackground=fondo_alt, activeforeground=text_color, font=fuente)
archivomenu.add_command(label="Nuevo", command=nuevo)
archivomenu.add_command(label="Abrir", command=abrir)
archivomenu.add_command(label="Guardar", command=guardar)
archivomenu.add_command(label="Guardar como", command=guardar_como)

# menu para editar
editarmenu = tk.Menu(menubar, tearoff=0, bg=fondo, fg=text_color, activebackground=fondo_alt, activeforeground=text_color, font=fuente)
editarmenu.add_command(label="Cortar", command=cortar)
editarmenu.add_command(label="Copiar", command=copiar)
editarmenu.add_command(label="Pegar", command=pegar)

# menu para personalizar el editor
personalizarmenu = tk.Menu(menubar, tearoff=0, bg=fondo, fg=text_color, activebackground=fondo_alt, activeforeground=text_color, font=fuente)
personalizarmenu.add_command(label="Tema: Gruvbox", command=lambda: personalizar(1))
personalizarmenu.add_command(label="Tema: Minimal", command=lambda: personalizar(2))
personalizarmenu.add_command(label="Tema: Nord", command=lambda: personalizar(3))

# menu acerca de
acercamenu = tk.Menu(menubar, tearoff=0, bg=fondo, fg=text_color, activebackground=fondo_alt, activeforeground=text_color, font=fuente)
acercamenu.add_command(label="Version", command=mostrar_info)

# poner menus en menubar
menubar.add_cascade(label="Archivo", menu=archivomenu)
menubar.add_cascade(label="Editar", menu=editarmenu)
menubar.add_cascade(label="Personalizar", menu=personalizarmenu)
menubar.add_cascade(label="Acerca de", menu=acercamenu)

# crear un Text
texto = tk.Text(screen, bg=fondo_alt, fg=text_color, font=fuente)
texto.grid(row=0, column=0, padx=padx, pady=pady)

# crear un label para mostrar el nombre del archivo
nombre_archivo = tk.Label(screen, bg=fondo, fg=text_color, font=fuente)
nombre_archivo.grid(row=1, column=0, padx=padx, pady=pady, sticky="w")

# atajos de teclado
screen.bind("<Control-n>", nuevo)
screen.bind("<Control-o>", abrir)
screen.bind("<Control-s>", guardar)

screen.bind("<Control-x>", cortar)
screen.bind("<Control-c>", copiar)
screen.bind("<Control-v>", pegar)

# bucle principal
screen.mainloop()
