# Recrear un btd

from torres import Dardero, TiraTachuelas, Canon, Hielo, SuperMono
from globos import GloboRojo, GloboAzul, GloboVerde, GloboAmarillo
from jugador import Jugador
from PIL import Image, ImageTk
import tkinter as tk
from tkinter.messagebox import showerror

# crear la clase interfaz
class Interfaz(object):
    def __init__(self, root, jugador):
        # configuracion de la ventana
        self.root = root
        self.root.title("Bloonsd TD python")
        self.root.resizable(0,0)

        # crear al jugador
        self.jugador = jugador

        # archivos con los assets
        self.pasto_raw = Image.open("assets/pasto.png")
        self.pasto_redimencionado = self.pasto_raw.resize((25,25))
        self.pasto = ImageTk.PhotoImage(self.pasto_redimencionado)

        self.camino_raw = Image.open("assets/camino.png")
        self.camino_redimencionado = self.camino_raw.resize((25,25))
        self.camino = ImageTk.PhotoImage(self.camino_redimencionado)

        self.dardero_raw = Image.open("assets/dardero.png")
        self.dardero_redimencionado = self.dardero_raw.resize((25,25))
        self.dardero = ImageTk.PhotoImage(self.dardero_redimencionado)

        self.tiratachuelas_raw = Image.open("assets/tiratachuelas.png")
        self.tiratachuelas_redimencionado = self.tiratachuelas_raw.resize((25,25))
        self.tiratachuelas = ImageTk.PhotoImage(self.tiratachuelas_redimencionado)

        self.canon_raw = Image.open("assets/canon.png")
        self.canon_redimencionado = self.canon_raw.resize((25,25))
        self.canon = ImageTk.PhotoImage(self.canon_redimencionado)

        self.hielo_raw = Image.open("assets/hielo.png")
        self.hielo_redimencionado = self.hielo_raw.resize((25,25))
        self.hielo = ImageTk.PhotoImage(self.hielo_redimencionado)

        self.supermono_raw = Image.open("assets/supermono.png")
        self.supermono_redimencionado = self.supermono_raw.resize((25,25))
        self.supermono = ImageTk.PhotoImage(self.supermono_redimencionado)

        self.moneda_raw = Image.open("assets/moneda.png")
        self.moneda_redimencionado = self.moneda_raw.resize((25,25))
        self.moneda = ImageTk.PhotoImage(self.moneda_redimencionado)

        self.corazon_raw = Image.open("assets/corazon.png")
        self.corazon_redimencionado = self.corazon_raw.resize((25,25))
        self.corazon = ImageTk.PhotoImage(self.corazon_redimencionado)

        # crear frame para el mapa
        self.mapa = tk.Frame(self.root)
        self.mapa.grid(row=1, column=0)

        # crear frame para el menu de las torres
        self.torres_menu = tk.Frame(self.root)
        self.torres_menu.grid(row=0, column=0)

        # crear frame con el dinero actual, vidas y ronda
        self.datos = tk.Frame(self.root)
        self.datos.grid(row=2, column=0)

        # bucle para crear el pasto (donde se ponen las torres)
        self.layout = ((0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7), (0,8), (0,9),
                       (1,0), (1,1), (1,2), (1,7), (1,8), (1,9),
                       (2,0), (2,1), (2,4), (2,5), (2,8), (2,9),
                       (3,3), (3,4), (3,5), (3,6),
                       (4,0), (4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (4,7), (4,8), (4,9),
                       )
        for x, y in self.layout:
            tk.Button(self.mapa, width=25, height=25, image=self.pasto,
                      command=lambda fila=x, columna=y: self.poner_torre(fila, columna)).grid(row=x, column=y)

        # bucle para crear el camino (donde pasan los globos)
        self.layout = ((1,3), (1,4), (1,5), (1,6),
                       (2,2), (2,3), (2,6), (2,7),
                       (3,0), (3,1), (3,2), (3,7), (3,8), (3,9)
                       )
        for x, y in self.layout:
            tk.Label(self.mapa, width=25, height=25, image=self.camino).grid(row=x, column=y)


        # botones para elegir la torre
        self.torre_id = tk.IntVar()
        self.layout = ((0, self.dardero, 1), (1, self.tiratachuelas, 2), (2, self.canon, 3), (3, self.hielo, 4), (4, self.supermono, 5))
        for y, imagen, id in self.layout:
            tk.Radiobutton(self.torres_menu, image=imagen, variable=self.torre_id, value=id).grid(row=0, column=y)

        # label con los datos de la partida
        self.dinero_imagen = tk.Label(self.datos, image=self.moneda)
        self.dinero_texto = tk.Label(self.datos, text=self.jugador.dinero)
        self.dinero_imagen.grid(row=0, column=0)
        self.dinero_texto.grid(row=0, column=1)

        self.vidas_imagen = tk.Label(self.datos, image=self.corazon)
        self.vidas_texto = tk.Label(self.datos, text=self.jugador.vidas)
        self.vidas_imagen.grid(row=0, column=2)
        self.vidas_texto.grid(row=0, column=3)


    # metodo poner torre
    def poner_torre(self, fila, columna):
        x, y = fila, columna
        torre = self.torre_id.get()
        dardero = Dardero()
        tiratachuelas = TiraTachuelas()
        canon = Canon()
        hielo = Hielo()
        supermono = SuperMono()
        if torre == 1 and self.jugador.dinero >= dardero.costo:
            tk.Button(self.mapa, image=self.dardero).grid(row=x, column=y)
            self.jugador.dinero -= dardero.costo
            self.dinero_texto.config(text=self.jugador.dinero)
            self.torre_id.set(0)
        elif torre == 2 and self.jugador.dinero >= tiratachuelas.costo:
            tk.Button(self.mapa, image=self.tiratachuelas).grid(row=x, column=y)
            self.jugador.dinero -= tiratachuelas.costo
            self.dinero_texto.config(text=self.jugador.dinero)
            self.torre_id.set(0)
        elif torre == 3 and self.jugador.dinero >= canon.costo:
            tk.Button(self.mapa, image=self.canon).grid(row=x, column=y)
            self.jugador.dinero -= canon.costo
            self.dinero_texto.config(text=self.jugador.dinero)
            self.torre_id.set(0)
        elif torre == 4 and self.jugador.dinero >= hielo.costo:
            tk.Button(self.mapa, image=self.hielo).grid(row=x, column=y)
            self.jugador.dinero -= hielo.costo
            self.dinero_texto.config(text=self.jugador.dinero)
            self.torre_id.set(0)
        elif torre == 5 and self.jugador.dinero >= supermono.costo:
            tk.Button(self.mapa, image=self.supermono).grid(row=x, column=y)
            self.jugador.dinero -= supermono.costo
            self.dinero_texto.config(text=self.jugador.dinero)
            self.torre_id.set(0)
        elif torre == 0:
            pass
        else:
            showerror("Dinero insuficiente", "No tienes dinero suficiente para comprar esta torre")
            self.torre_id.set(0)

    # metodo ejecutar
    def ejecutar(self):
        self.root.mainloop()

# crear la ventana
screen = tk.Tk()

# crear al jugador
jugador = Jugador(500, 100)

# objeto de la clase Interfaz
a = Interfaz(screen, jugador)
a.ejecutar()
