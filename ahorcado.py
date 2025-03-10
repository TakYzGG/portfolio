# Ahorcado en python

from random import randint
from os import system

def mostrar_persona(fase):
    if fase == 1:
        print(" ", r"_" * 12)
        print(r" |", " " * 10, r"|")
        print(r" |", " " * 10, r"|")
        print(r" |")
        print(r" |")
        print(r" |")
        print(r" |")
        print(r" |")
        print(r" |")
        print("---")

    if fase == 2:
        print(" ", r"_" * 12)
        print(r" |", " " * 10, r"|")
        print(r" |", " " * 10, r"|")
        print(r" |", " " * 10, "O")
        print(r" |")
        print(r" |")
        print(r" |")
        print(r" |")
        print(r" |")
        print("---")

    if fase == 3:
        print(" ", r"_" * 12)
        print(r" |", " " * 10, r"|")
        print(r" |", " " * 10, r"|")
        print(r" |", " " * 10, "O")
        print(r" |", " " * 10, "|")
        print(r" |")
        print(r" |")
        print(r" |")
        print(r" |")
        print("---")

    if fase == 4:
        print(" ", r"_" * 12)
        print(r" |", " " * 10, r"|")
        print(r" |", " " * 10, r"|")
        print(r" |", " " * 10, "O")
        print(r" |", " " * 9, "/|")
        print(r" |")
        print(r" |")
        print(r" |")
        print(r" |")
        print("---")

    if fase == 5:
        print(" ", r"_" * 12)
        print(r" |", " " * 10, r"|")
        print(r" |", " " * 10, r"|")
        print(r" |", " " * 10, "O")
        print(r" |", " " * 9, "/|\\")
        print(r" |")
        print(r" |")
        print(r" |")
        print(r" |")
        print("---")

    if fase == 6:
        print(" ", r"_" * 12)
        print(r" |", " " * 10, r"|")
        print(r" |", " " * 10, r"|")
        print(r" |", " " * 10, "O")
        print(r" |", " " * 9, "/|\\")
        print(r" |", " " * 9, "/")
        print(r" |")
        print(r" |")
        print(r" |")
        print("---")

    if fase == 7:
        print(" ", r"_" * 12)
        print(r" |", " " * 10, r"|")
        print(r" |", " " * 10, r"|")
        print(r" |", " " * 10, "O")
        print(r" |", " " * 9, "/|\\")
        print(r" |", " " * 9, "/ \\")
        print(r" |")
        print(r" |")
        print(r" |")
        print("---")

def elegir_palabra(lista_palabras):
    x = randint(0, len(lista_palabras) -1)
    palabra = lista_palabras[x]
    return palabra

def mostrar_palabra(palabra):
    palabra_oculta = "-" * len(palabra)
    return palabra_oculta

def actualizar_palabra(palabra, palabra_oculta, letra):
    nuevo_estado = ""

    for i in range(len(palabra)):
        if palabra[i] == letra:
            # Si la letra adivinada está en la palabra, la mostramos
            nuevo_estado += letra
        else:
            # Si no, dejamos lo que ya estaba (guion o letra descubierta antes)
            nuevo_estado += palabra_oculta[i]

    return nuevo_estado

def pedir_letra():
    letra = input("Letra: ")
    return letra

lista_palabras = [
    "montaña",
    "caballo",
    "ventana",
    "librero",
    "murcielago",
    "pintura",
    "cuchillo",
    "espejo",
    "relojero",
    "cultura",
    "paraguas",
    "palmera",
    "frutilla",
    "cueva",
    "semilla"
]

fase = 1
letras_usadas = []

palabra = elegir_palabra(lista_palabras)
palabra_oculta = mostrar_palabra(palabra)

while True:
    system("clear")
    mostrar_persona(fase)
    print()
    print(palabra_oculta)
    print(f"Letras usadas: {letras_usadas}")
    print()

    letra = pedir_letra()

    # Si la letra ya fue usada:
    if letra in letras_usadas:
        print("Ya usaste esa letra. Intenta otra.")
        a = input("Preciona ENTER para continuar")
        continue
    else:
        letras_usadas.append(letra)

    # Si la letra está en la palabra
    if letra in palabra:
        nueva_palabra_oculta = actualizar_palabra(palabra, palabra_oculta, letra)

        # Si no cambió, no pasa nada
        if nueva_palabra_oculta == palabra_oculta:
            print(f"La letra '{letra}' ya estaba descubierta.")
            a = input("Preciona ENTER para continuar")
        else:
            palabra_oculta = nueva_palabra_oculta
            print(f"¡Bien! La letra '{letra}' está en la palabra.")
            a = input("Preciona ENTER para continuar")

    else:
        print(f"La letra '{letra}' no está en la palabra.")
        a = input("Preciona ENTER para continuar")
        fase += 1

    # Ganaste
    if palabra_oculta == palabra:
        print("\n¡Felicidades! Adivinaste la palabra:", palabra)
        a = input("Preciona ENTER para continuar")
        break

    # Perdiste
    if fase >= 7:
        system("clear")
        mostrar_persona(fase)
        print("\n¡Perdiste! La palabra era:", palabra)
        a = input("Preciona ENTER para continuar")
        break
